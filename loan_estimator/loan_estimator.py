from flask import Blueprint, flash, redirect, render_template, request, url_for, jsonify

bp = Blueprint('loan_estimator', __name__)

@bp.route('/')
def index():
    return render_template("index.html")
    # return "Hello from akbars hack backend!"

@bp.route('/api/estimate', methods=["POST"])
def estimate():
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
    				"Марка": "BMW",
                    # "Ссылка": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjjtv2hrKnhAhWwy6YKHRLRB2QQjRx6BAgBEAU&url=https%3A%2F%2Fbugaga.ru%2Fjokes%2F1146744172-foto-prikoly-i-kartinki.html&psig=AOvVaw0j3AxioA8lvBeP0rH5olLP&ust=1554017449100132"
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