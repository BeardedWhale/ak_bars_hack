from flask import Blueprint, flash, redirect, render_template, request, url_for, jsonify

bp = Blueprint('loan_estimator', __name__)

@bp.route('/')
def index():
    return "Hello from akbars hack backend!"

@bp.route('/test', methods=["POST"])
def test():
    # Send empty json if no results were found
    json = request.get_json()
    print(json)
    return jsonify(
        {
    		"bestprice": "374718484",
    		"bestvariants": {
    			"info1": {
    				"id": "1",
    				"Двигатель": "Дизель",
    				"Марка": "BMW"
    			},

    			"info2": {
    				"id": "2",
    				"Двигатель": "Дизель",
    				"Марка": "BMW",
    				"Пробег": "200"
    			}
    		}
    	}
    )
    # return "Hello from test" if json == None else ''.join(dict(json))