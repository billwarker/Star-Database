from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import (Column, DateTime, ForeignKey,
						Integer, String, Boolean, Float,
						func)

from sqlalchemy.orm import backref, relationship
from settings import psql

engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(
						psql['user'], psql['password'],
						psql['host'], psql['port'],
						psql['database']))
Base = declarative_base()

class AmazonOrder(Base):
	__tablename__ = 'amazon_orders'
	
	id = Column(Integer, primary_key=True)

	# order info

	order_id = Column(String)
	#buyer_email = Column(String)
	#earliest_ship_date = Column(String)
	#fulfillment_channel = Column(String)
	#business_order = Column(Boolean)
	#prime_order = Column(Boolean)
	#replacement_order = Column(Boolean)
	#last_update_date = Column(String)
	#latest_ship_date = Column(String)
	marketplace_id = Column(String)
	num_items_shipped = Column(Integer)
	num_items_unshipped = Column(Integer)
	order_status = Column(String)
	order_total_amount = Column(Float)
	order_total_currency_code = Column(String)
	#order_type = Column(String)
	#payment_method = Column(String)
	purchase_date = Column(DateTime)
	sales_channel = Column(String)
	#seller_order_id = Column(String)
	#ship_service_level = Column(String)
	#ship_service_level_cat = Column(String)
	shipping_address_line1 = Column(String)
	shipping_address_city = Column(String)
	shipping_address_country = Column(String)
	shipping_address_name = Column(String)
	shipping_address_postal = Column(String)
	shipping_address_region = Column(String)

	# product info

	asin = Column(String)
	item_price = Column(Float)
	#item_price_currency_code = Column(String)
	item_tax = Column(Float)
	#item_tax_currency_code = Column(String)
	order_item_id = Column(String)
	product_info_num_items = Column(Integer)
	promo_discount_amount = Column(Float)
	#promo_discount_currency_code = Column(String)
	promotion_id = Column(String)
	qty_ordered = Column(Integer)
	qty_shipped = Column(Integer)
	seller_sku = Column(String)
	#shipping_discount_amount = Column(Integer)
	#shipping_discount_currency_code = Column(String)
	#shipping_price_amount = Column(Integer)
	#shipping_price_currency_code = Column(String)
	#shipping_tax_amount = Column(Integer)
	#shipping_tax_currency_code = Column(String)

class LeanOrder(Base):
	__tablename__ = 'lean_orders'

	id = Column(Integer, primary_key=True)
	order_id = Column(Integer)

	client_order = Column(String)
	end_client_order_no = Column(String)
	destination = Column(String)
	created_on = Column(DateTime)
	order_status = Column(String)
	ship_date = Column(DateTime)
	item = Column(String)
	upc = Column(String)
	qty = Column(Integer)
	ship_qty = Column(Integer)
	carrier = Column(String)
	tracking_no = Column(String)
	retailer = Column(String)
	province = Column(String)
	city = Column(String)
	customer_name = Column(String)

class StarInventory(Base):
	__tablename__ = 'star_inventory'

	item_num = Column(Integer, primary_key=True)
	item_sku = Column(String)
	item_desc = Column(String)
	item_inv = Column(Integer)
	item_upc = Column(String)

class SBWInventory(Base):
	__tablename__ = 'sbw_inventory'

	item_num = Column(Integer, primary_key=True)
	item_sku = Column(String)
	item_desc = Column(String)
	item_inv = Column(Integer)
	item_upc = Column(String)