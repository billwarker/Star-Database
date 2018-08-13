def _order_data(order):
	order_data = {}
	order_data['amazon_order_id'] = order["AmazonOrderId"]["value"]
	try:
		order_data['buyer_email'] = order['BuyerEmail']['value']
	except KeyError:
		order_data['buyer_email'] = None
	try:
		order_data['earliest_ship_date'] = order['EarliestShipDate']['value']
	except KeyError:
		order_data['earliest_ship_date'] = None
	try:
		order_data['fulfillment_channel'] = order['FulfillmentChannel']['value']
	except KeyError:
		order_data['fulfillment_channel'] = None
	try:
		order_data['business_order'] = order['IsBusinessOrder']['value']
	except KeyError:
		order_data['business_order'] = None
	try:
		order_data['premium_order'] = order['IsPremiumOrder']['value']
	except KeyError:
		order_data['premium_order'] = None
	try:
		order_data['prime_order'] = order["IsPrime"]["value"]
	except KeyError:
		order_data['prime_order'] = None
	try:
		order_data['replacement_order'] = order['IsReplacementOrder']['value']
	except KeyError:
		order_data['replacement_order'] = None
	try:
		order_data['last_update_date'] = order["LastUpdateDate"]["value"]
	except KeyError:
		order_data['last_update_date'] = None
	try:
		order_data['latest_ship_date'] = order["LatestShipDate"]["value"]
	except KeyError:
		order_data['latest_ship_date'] = None
	try:
		order_data['marketplace_id'] = order["MarketPlaceId"]['value']
	except KeyError:
		order_data['marketplace_id'] = None
	try:
		order_data['num_items_shipped'] = int(order["NumberOfItemsShipped"]["value"])
	except KeyError:
		order_data['num_items_shipped'] = None
	try:
		order_data['num_items_unshipped'] = int(order["NumberOfItemsUnshipped"]["value"])
	except KeyError:
		order_data['num_items_unshipped'] = None
	try:
		order_data['order_status'] = order["OrderStatus"]["value"]
	except KeyError:
		order_data['order_status'] = None
	try:
		order_data['order_total_amount'] = float(order["OrderTotal"]["Amount"]["value"])
	except KeyError:
		order_data['order_total_amount'] = None
	try:
		order_data['order_total_currency_code'] = order["OrderTotal"]["CurrencyCode"]["value"]
	except KeyError:
		order_data['order_total_currency_code'] = None
	try:
		order_data['order_type'] = order["OrderType"]["value"]
	except KeyError:
		order_data['order_type'] = None
	try:
		order_data['payment_method'] = order["PaymentMethod"]["value"]
	except KeyError:
		order_data['payment_method'] = None
	try:
		order_data['purchase_date'] = order["PurchaseDate"]["value"]
	except KeyError:
		order_data['purchase_date'] = None
	try:
		order_data['sales_channel'] = order["SalesChannel"]["value"]
	except KeyError:
		order_data['sales_channel'] = None
	try:
		order_data['seller_order_id'] = order["SellerOrderId"]["value"]
	except KeyError:
		order_data['seller_order_id'] = None
	try:
		order_data['ship_service_level'] = order["ShipServiceLevel"]["value"]
	except KeyError:
		order_data['ship_service_level'] = None
	try:
		order_data['ship_service_level_cat'] = order["ShipServiceLevelCategory"]["value"]
	except KeyError:
		order_data['ship_service_level_cat'] = None
	try:
		order_data['shipping_address_line1'] = order["ShippingAddress"]["AddressLine1"]["value"]
	except KeyError:
		order_data['shipping_address_line1'] = None
	try:
		order_data['shipping_address_city'] = order["ShippingAddress"]["City"]["value"]
	except KeyError:
		order_data['shipping_address_city'] = None
	try:
		order_data['shipping_address_country'] = order["ShippingAddress"]["CountryCode"]["value"]
	except KeyError:
		order_data['shipping_address_country'] = None
	try:
		order_data['shipping_address_name'] = order["ShippingAddress"]["Name"]["value"]
	except KeyError:
		order_data['shipping_address_name'] = None
	try:
		order_data['shipping_address_postal'] = order["ShippingAddress"]["PostalCode"]["value"]
	except KeyError:
		order_data['shipping_address_postal'] = None
	try:
		order_data['shipping_address_region'] = order["ShippingAddress"]["StateOrRegion"]["value"]
	except KeyError:
		order_data['shipping_address_region'] = None

	return order_data

def _product_data(item):
	product_data = {}
	product_data['asin'] = item['ASIN']['value']
	try:
		product_data['item_price'] = float(item['ItemPrice']['Amount']['value'])
	except KeyError:
		product_data['item_price'] = None
	try:
		product_data['item_price_currency_code'] = item['ItemPrice']['CurrencyCode']['value']
	except KeyError:
		product_data['item_price_currency_code'] = None
	try:
		product_data['item_tax'] = float(item['ItemTax']['Amount']['value'])
	except KeyError:
		product_data['item_tax'] = None
	try:
		product_data['item_tax_currency_code'] = item['ItemTax']['CurrencyCode']['value']
	except KeyError:
		product_data['item_tax_currency_code'] = None
	try:
		product_data['order_item_id'] = item['OrderItemId']['value']
	except KeyError:
		product_data['order_item_id'] = None
	try:
		product_data['product_info_num_items'] = int(item['ProductInfo']['NumberOfItems']["value"])
	except KeyError:
		product_data['product_info_num_items'] = None
	try:
		product_data['promo_discount_amount'] = float(item['PromotionDiscount']["Amount"]["value"])
	except KeyError:
		product_data['promo_discount_amount'] = None
	try:
		product_data['promo_discount_currency_code'] = item['PromotionDiscount']["CurrencyCode"]["value"]
	except KeyError:
		product_data['promo_discount_currency_code'] = None
	try:
		product_data['promotion_id'] = item["PromotionIds"]["PromotionId"]["value"]
	except KeyError:
		product_data['promotion_id'] = None
	try:
		product_data['qty_ordered'] = int(item["QuantityOrdered"]["value"])
	except KeyError:
		product_data['qty_ordered'] = None
	try:
		product_data['qty_shipped'] = int(item["QuantityShipped"]["value"])
	except KeyError:
		product_data['qty_shipped'] = None
	try:
		product_data['seller_sku'] = item["SellerSKU"]["value"]
	except KeyError:
		product_data['seller_sku'] = None
	try:
		product_data['shipping_discount_amount'] = float(item["ShippingDiscount"]["Amount"]["value"])
	except KeyError:
		product_data['shipping_discount_amount'] = None
	try:
		product_data['shipping_discount_currency_code'] = item["ShippingDiscount"]["CurrencyCode"]["value"]
	except KeyError:
		product_data['shipping_discount_currency_code'] = None
	try:
		product_data['shipping_price_amount'] = float(item["ShippingPrice"]["Amount"]["value"])
	except KeyError:
		product_data['shipping_price_amount'] = None
	try:
		product_data['shipping_price_currency_code'] = item["ShippingPrice"]["CurrencyCode"]["value"]
	except KeyError:
		product_data['shipping_price_currency_code'] = None
	try:
		product_data['shipping_tax_amount'] = float(item["ShippingTax"]["Amount"]["value"])
	except KeyError:
		product_data['shipping_tax_amount'] = None
	try:
		product_data['shipping_tax_currency_code'] = item["ShippingTax"]["CurrencyCode"]["value"]
	except KeyError:
		product_data['shipping_tax_currency_code'] = None

	return product_data