from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Lcdcei2016@localhost:3306/storedb")

meta = MetaData()

cnx= engine.connect()