from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine('sqlite:///bible-sqlite.db')
#print(engine.table_names())
connection = engine.connect()

"""
metadata = MetaData()
jobs = Table('Jobs', metadata, autoload=True,autoload_with=engine)
print(repr(jobs))
"""

"""
stmt = 'SELECT * from Jobs'
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()
first_row= results[0]
print(first_row)
print(first_row.keys())
print(first_row.Applied)
"""

metadata = MetaData()
jobs = Table('t_kjv', metadata, autoload=True,autoload_with=engine)
stmt = select([jobs])
#print(stmt)
results = connection.execute(stmt).fetchall()
print(results)