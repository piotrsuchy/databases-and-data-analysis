from sqlalchemy import create_engine
import psycopg2 as pg
import pandas as pd

db_string = "postgresql://wbauer_adb:adb2020@pgsql-196447.vipserv.org:5432/wbauer_adb"

db = create_engine(db_string)

connection_sqlalchemy = db.connect()