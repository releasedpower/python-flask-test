from app import app, db
from app.models import Region
from flask import Flask, jsonify,render_template, request

@app.route('/')
def index():
    regions = Region.query.all()
    region_data = [{"id": region.id, "name": region.name} for region in regions]
    return jsonify({"regions": region_data}) 