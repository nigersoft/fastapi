from sqlalchemy import create_engine, MetaData

#engine = create_engine("mysql+pymysql://root:Lcdcei2016@localhost:3306/storedb")
ssl_args = {'ssl': {'ca':'/etc/ssl/certs/ca-certificates.crt'}}
engine = create_engine('mysql+pymysql://pcktmog5y6uy1jri1ysm:pscale_pw_1vcuRLgP4ezZWUOcr4jDzdTDBt6oXi4C7IPINTcQwzC@us-east.connect.psdb.cloud:3306/storedb',connect_args=ssl_args)

meta = MetaData()

cnx= engine.connect()