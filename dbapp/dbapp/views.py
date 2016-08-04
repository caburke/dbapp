from flask import jsonify
from flask import render_template
import json

from dbapp import app, engine
from dbapp.models import actors
from dbapp.utils import table_to_json


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/models')
def models():
    return ', '.join(engine.table_names())


@app.route('/actors')
def display_actors():
    res = engine.execute(actors.select()).fetchall()
    return jsonify(res)


@app.route('/datatable')
def display_datatable():

    columns = actors.columns.keys()

    return render_template('datatable.html', columns=columns)


@app.route('/get_json', methods=['GET', 'POST'])
def get_json():

    res = engine.execute(actors.select()).fetchall()

    return table_to_json(res)
