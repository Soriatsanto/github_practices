from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SERVER_URL = "postgresql+psycopg2://soriattarif_user:O5XtGAgu4gpEFoYb0w5L3dfVIiCf0dgo@dpg-dc380c0m7kps73dfrlh0-a.oregon-postgres.render.com/soriattarif"
#SERVER_URL = "mysql+pymysql://root:root@localhost:3306/githubs"
engine = create_engine(SERVER_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()
