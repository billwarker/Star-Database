from datetime import timedelta, date
import time
from mws import mws
from amazon_functions import _order_data, _product_data
from settings import psql, amzn_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import AmazonOrder
from sqlalchemy.ext.declarative import declarative_base

class AmazonParser:
	
	def __init__(self, settings):
		# Import settings
		self.settings = settings
		# Connect to Postgres
		self.engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(
											psql['user'], psql['password'],
											psql['host'], psql['port'],
											psql['database']))
		self.Base = declarative_base()
		Session = sessionmaker(bind=self.engine)
		self.session = Session()
		# Connect to Amazon API
		self.api = mws.Orders(self.settings['ACCESS_KEY'],
								self.settings['SECRET_KEY'],
								self.settings['SELLER_ID'],
								region='CA')
		self.order_dict = {}

	def _daterange(self, start_date, end_date):
		for n in range(int((end_date - start_date).days)):
			yield start_date + timedelta(n)

	def _get_order_data(self, date):
			day_before = (date + timedelta(-1)).strftime('%Y-%m-%d')
			day_after = (date + timedelta(1)).strftime('%Y-%m-%d')
			listed_orders = self.api.list_orders(
										marketplaceids=self.settings['MARKETPLACE'],
										created_after=day_before,
										created_before = day_after)
			order_batch = set()
			update_batch = set()
			order_count = 0
			update_count = 0

			try:
				orders = listed_orders.parsed['Orders']['Order']		
				if type(orders) != list:
					orders = [orders]

				for order in orders:
					order_id = order['AmazonOrderId']['value']
					order_data = _order_data(order)
					self.order_dict[order_id] = order_data

					if len(self.session.query(AmazonOrder.order_id).\
						filter(AmazonOrder.order_id == order_id).all()) > 0:
							update_batch.add(order_id)
							update_count += 1
					else:
						order_batch.add(order_id)
						order_count += 1

				print('\nFound {} new orders for {}'.format(order_count,
						date.strftime('%Y-%m-%d')))
				print('Found {} updated orders for {}\n'.format(update_count,
						date.strftime('%Y-%m-%d')))				
				return order_batch, update_batch

			except KeyError:
				print("No orders for {}".format(date.strftime('%Y-%m-%d')))
				return order_batch, update_batch

	def _get_product_data(self, order):
			order_data = self.order_dict[order]
			order_items = self.api.list_order_items(order).\
									parsed["OrderItems"]["OrderItem"]

			if type(order_items) != list:
				order_items = [order_items]
			
			order_objs = []

			for item in order_items:
				product_data = _product_data(item)
				order_obj = AmazonOrder(order_id = order,
					marketplace_id = order_data['marketplace_id'],
					num_items_shipped = order_data['num_items_shipped'],
					num_items_unshipped = order_data['num_items_unshipped'],
					order_status = order_data['order_status'],
					order_total_amount = order_data['order_total_amount'],
					order_total_currency_code = order_data['order_total_currency_code'],
					purchase_date = order_data['purchase_date'],
					sales_channel = order_data['sales_channel'],
					shipping_address_line1 = order_data['shipping_address_line1'],
					shipping_address_city = order_data['shipping_address_city'],
					shipping_address_country = order_data['shipping_address_country'],
					shipping_address_name = order_data['shipping_address_name'],
					shipping_address_postal = order_data['shipping_address_postal'],
					shipping_address_region = order_data['shipping_address_region'],
					asin = product_data['asin'],
					item_price = product_data['item_price'],
					item_tax = product_data['item_tax'],
					order_item_id = product_data['order_item_id'],
					product_info_num_items = product_data['product_info_num_items'],
					promo_discount_amount = product_data['promo_discount_amount'],
					promotion_id = product_data['promotion_id'],
					qty_ordered = product_data['qty_ordered'],
					qty_shipped = product_data['qty_shipped'],
					seller_sku = product_data['seller_sku'])

				order_objs.append(order_obj)
				return order_objs
	
	def _add_orders(self, order_objs):
		for line_item in order_objs:
			self.session.add(line_item)
			print("Added {} ({})".format(line_item.order_id,
										line_item.seller_sku))

	def _update_orders(self, order_objs):
		for line_item in order_objs:
			line_item_dict = line_item.__dict__
			line_item_dict.pop('_sa_instance_state')

			self.session.query(AmazonOrder).\
				filter(AmazonOrder.order_id == line_item.order_id).\
				filter(AmazonOrder.order_id == line_item.seller_sku).\
				update(line_item_dict)
			print("Updated {} ({})".format(line_item.order_id,
										line_item.seller_sku))

	def run(self, start_date, end_date):
		print("\nCompiling orders from {} to {}...\n".format(start_date.isoformat(),
															end_date.isoformat()))
		order_history = self._daterange(start_date, end_date)
		date_count = 0
		for date in list(order_history):
			try:
				order_batch, update_batch = self._get_order_data(date)
				date_count += 1
			except mws.MWSError:
				throttled = True
				while throttled:
					print('Throttling requests for 60s')
					time.sleep(60)
					try:
						order_batch, update_batch = self._get_order_data(date)
						date_count += 1
						throttled = False
					except mws.MWSError:
						continue

			for order in order_batch:
				try:
					order_line_items = self._get_product_data(order)
					self._add_orders(order_line_items)
				except mws.MWSError:
					throttled = True
					while throttled:
						print('Throttling requests for {}s'.\
								format(self.settings['THROTTLE_TIME']))
						time.sleep(self.settings['THROTTLE_TIME'])
						try:
							self._get_product_data(order)
							throttled = False
						except mws.MWSError:
							continue
			self.session.commit()
			print('New orders committed')

			for order in update_batch:
				try:
					order_line_items = self._get_product_data(order)
					self._update_orders(order_line_items)
				except mws.MWSError:
					throttled = True
					while throttled:
						print('Throttling requests for {}s'.\
								format(self.settings['THROTTLE_TIME']))
						time.sleep(self.settings['THROTTLE_TIME'])
						try:
							order_line_items = self._get_product_data(order)
							self._update_orders(order_line_items)
							throttled = False
						except mws.MWSError:
							continue
			self.session.commit()
			print('Updated orders committed')

if __name__ == '__main__':
	
	start_date = date(2017, 1, 1) # As far back as amazon api goes
	end_date = date.today()
	
	parser = AmazonParser(amzn_settings)
	parser.run(start_date, end_date)