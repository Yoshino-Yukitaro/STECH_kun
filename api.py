from flask import Flask, request, url_for, jsonify
#from db import EventItem, init_db, init_schema
#from db import item_schema, items_schema

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/api/events',methods=['GET'])
def api_get():
	#items = EventItem.query.all()
	items = {
	"name": "太郎",
	"event": "忘年会",
	"url":"https://hoge.co.jp",
	"year":2022,
	"day":12,
	"time":18
	}
	return jsonify(items)
	#return items_schema.jsonify(items)
	
@app.route('/api/events/<int:event_id>',methods=['GET'])
def api_id_get(event_id):
	item = EventItem.query.filter_by(event_id=event_id).first_or_404()
	return item_schema.jsonify(item)
	

@app.route('/api/events',methods=['POST'])
def api_add():
	if not "name" in request.json:
		return "error"
	if not "event" in request.json:
		return "error"
	if not "url" in request.json:
		return "error"
	if not "year" in request.json:
		return "error"
	if not "day" in request.json:
		return "error"
	if not "time" in request.json:
		return "error"
	#item = EventItem(name=request.json["name"],event=request.json["event"],text=requets.json["text"],url=request.json["url"],year=request.json["year"],day=request.json["day"],time=request.json["time"])
	items = {
	"name" :request.json["name"],
	"event" :request.json["event"],
	"url" :request.json["url"],
	"year" :request.json["year"],
	"day" :request.json["day"],
	"time" :request.json["time"],
	}
	#db.session.add(item)
	#db.session.commit()
	#return item_schema.jsonify(item)
	return jsonify(items)
	
#@app.route('/api/events/<int:event_id>',methods=['DELETE'])
#def api_delete(event_id):
#	item = EventItem.query.filter_by(event_id=event_id).first_or_404()
#	db.session.delete(item)
#	db.session.commit()
#	return jsonify({"result": True})
	
if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
	
