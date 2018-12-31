from sqlalchemy import create_engine,ForeignKey,Column,Date,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref,sessionmaker

db = "sqlite:///people.db"
Base = declarative_base()

class Person(Base):
	__tablename__ = "person"
	id = Column(Integer, primary_key=True)
	name = Column(String(250),nullable=False)
	
class Address(Base):
	__tablename__ = "address"
	id = Column(Integer, primary_key=True)
	street_name = Column(String(250))
	street_number = Column(String(250))
	post_code = Column(String(250),nullable=False)
	person_id = Column(Integer,ForeignKey('person.id'))
	person = relationship(Person)

engine = create_engine(db,echo=True) #echo prints queries
Base.metadata.create_all(engine)
db_session = sessionmaker(bind=engine)
session = db_session()

new_person = Person(name = 'Joe')
session.add(new_person)
session.commit()

new_address = Address(post_code = '00000',person=new_person)
session.add(new_address)
session.commit()
