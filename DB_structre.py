from enum import unique
from peewee import *
db = SqliteDatabase('library.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})

#intity Framework

class Category(Model):
    Category_name=CharField(null=True)
    #Parent_Category=
    class Meta:
        database=db

class Publisher(Model):
    Name=CharField(null=True,unique=True)
    Location=CharField(null=True)
    class Meta:
        database=db

class Author(Model):
    Name=CharField(null=True,unique=True)
    Location=CharField(null=True)
    class Meta:
        database=db

class Books(Model):
    Code=CharField(null=True, unique=True)
    Title=CharField(null=True)
    Category=ForeignKeyField(Category , backref='Category',null=True)
    Author=ForeignKeyField(Author, backref='Author',null=True)
    Publisher=ForeignKeyField(Publisher,backref='Publisher',null=True)
    Price=DecimalField(null=True)
    Image=CharField(null=True)
    Date=DateTimeField(null=True)
    class Meta:
        database=db

class Clients(Model):
    Name=CharField(null=True)
    Email=CharField(null=True,unique=True)
    Phone_number=IntegerField(null=True)
    National_ID=IntegerField(null=True,unique=True)
    class Meta:
        database=db

class Employee(Model):
    Name=CharField(null=True)
    Email=CharField(null=True,unique=True)
    National_ID=IntegerField(null=True,unique=True)
    Phone=IntegerField(null=True)
    Priority=IntegerField(null=True)
    class Meta:
        database=db

class Branch(Model):
    Name=CharField(null=True)
    Code=CharField(null=True)
    Location=CharField(null=True)
    class Meta:
        database=db


DAILY_ACTION=(
    (1,'Rent'),
    (2,'Retrieve')
)
class Daily_movements(Model):
    Name=ForeignKeyField(Books,backref='Name',null=True)
    Code=CharField(null=True,unique=True)
    Client=ForeignKeyField(Clients,backref='Client',null=True)
    Action= CharField(null=True, choices=DAILY_ACTION)
    From=DateTimeField(null=True)
    To=DateTimeField(null=True)
    class Meta:
        database=db

HISTORY_ACTION=(
    (1,'login'),
    (3,'create'),
    (4,'Update'),
    (5,'Remove')
)
class History(Model):
    User=ForeignKeyField(Employee,backref='User',null=True)
    Action=CharField(choices=HISTORY_ACTION) #Choices
    Table=CharField()  #Choices
    Date=DateTimeField(null=True)
    Branch=ForeignKeyField(Branch,backref='Branch',null=True)
    class Meta:
        database=db


db.connect()
db.create_tables([Category,Author,Publisher,Books,Clients,Employee,Branch,Daily_movements,History])