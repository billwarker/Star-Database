from Files.file_io import LeanDownloader, _convert_xml_to_xlsx
from models import LeanOrder, AmazonOrder, StarInventory, SBWInventory

from amazon_parser import AmazonParser
from order_parser import OrderParser
from inventory_updater import InventoryUpdater

import datetime
from datetime import timedelta, date
from settings import psql, amzn_settings, DOWNLOAD_DIR, STAR_PAYLOAD
from settings import SBW_PAYLOAD, CHROMEDRIVER, INVENTORY_DIR
import os

if __name__ == '__main__':
	
	# Download data

	os.makedirs(INVENTORY_DIR, exist_ok=True)
	
	name1 = "STAR Inventory {}".format(datetime.date.today().strftime("%m-%d-%Y"))
	name2 = "SBW Inventory {}".format(datetime.date.today().strftime("%m-%d-%Y"))
	name3 = "STAR Orders {}".format(datetime.date.today().strftime("%m-%d-%Y"))
	
	downloader = LeanDownloader(CHROMEDRIVER)
	downloader.login(STAR_PAYLOAD)
	star_inventory = _convert_xml_to_xlsx(downloader.download_inventory(DOWNLOAD_DIR), name1, INVENTORY_DIR)

	downloader.logout()
	downloader.login(SBW_PAYLOAD)
	sbw_inventory = _convert_xml_to_xlsx(downloader.download_inventory(DOWNLOAD_DIR), name2, INVENTORY_DIR)
	
	downloader.logout()
	downloader.login(STAR_PAYLOAD)
	star_orders = downloader.download_all_orders(DOWNLOAD_DIR)

	downloader.close()

	# Update postgres

	inventory_updater = InventoryUpdater(psql)
	inventory_updater.update_star(star_inventory)
	inventory_updater.update_sbw(sbw_inventory)

	lean_order_parser = OrderParser(psql)
	lean_order_parser.update(star_orders)






