from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

titles = Table(
   'titles', meta, 
   Column('id', String, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
)
meta.create_all(engine)