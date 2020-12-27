from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow() # Flask-Marshmallowの利用設定

def init_db(app):
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/todoitems.db"
  db.init_app(app)
  return db
  
def init_schema(app):  # Flask-Marshmallowオブジェクトをappオブジェクトで初期化
  ma.init_app(app)
  
class EventItem(db.Model):
	__tablename__ = "eventitem"
	name = db.Column(db.String(20), nullable=False)
	event = db.Column(db.String(100), nullable=False)
	event_id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(200), nullable=True)
	url = db.Column(db.String(100), nullable=False)
	year = db.Column(db.Integer, nullable=False)
	day = db.Column(db.Integer, nullable=False)
	time = db.Column(db.Integer, nullable=False)
	
class ItemSchema(ma.Schema):
	class Meta:
		fields = ("name", "event", "event_id", "text", "url", "year", "day", "time")
		
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
	
	
