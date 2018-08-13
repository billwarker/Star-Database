### SETTINGS
import os
### path to star_interactive.db

CHROMEDRIVER = os.path.abspath(os.path.join(os.path.dirname( __file__ ),
											'Files',
											'chromedriver.exe'))

DOWNLOAD_DIR = r'C:\path\to\downloads'

INVENTORY_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ),
	'Inventory Sheets'))

STAR_PAYLOAD = {'username': r'dog', 'userpassword': r'woof'}

SBW_PAYLOAD = {'username': r'cat', 'userpassword': r'meow'}

# Amazon OrderParser

amzn_settings = {
			'ACCESS_KEY':'your_access_key',
			'SELLER_ID':'your_seller_id',
			'SECRET_KEY':'your_secret_key',
			'MARKETPLACE': ['A2EUQ1WTGCTBG2', 'ATVPDKIKX0DER'], # CA, US
			'THROTTLE_TIME': 3
			}

# PostgreSQL connection

psql = {"user": "your_username",
		"password": "your_password",
		"host": "your_host",
		"port": "your_port",
		"database": "your_db"}