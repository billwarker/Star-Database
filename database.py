from sqlalchemy import create_engine
from models import Base, AmazonOrder, LeanOrder, StarInventory, SBWInventory
from settings import psql

engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(
									psql['user'], psql['password'],
									psql['host'], psql['port'],
									psql['database']))
def init_db():
	response = input("Reset Lean? [y]")
	if response == 'y':
		LeanOrder.__table__.drop(engine)
	
	response = input("Reset Amazon? [y]")
	if response == 'y':
		AmazonOrder.__table__.drop(engine)
	
	response = input("Reset Lean Inventory? [y]")
	if response == 'y':
		StarInventory.__table__.drop(engine)
	response = input("Reset SBW Inventory? [y]")
	if response == 'y':
		SBWInventory.__table__.drop(engine)
	
	Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
	init_db()