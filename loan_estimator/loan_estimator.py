from flask import Blueprint, flash, redirect, render_template, request, url_for, jsonify
from loan_estimator.finder import Finder
from loan_estimator.utils import cars_to_json

bp = Blueprint('loan_estimator', __name__)

@bp.route('/')
def index():
    return render_template("index.html")
    # return "Hello from akbars hack backend!"

@bp.route('/api/estimate', methods=["POST"])
def estimate():
    result = {}
    # Send empty json if no results were found
    json = request.get_json()
    print("REQUEST RECEIVED...")
    print("SENDING REQUESTS TO API AND EVALUATE THEM...")
    # # print(type(json))
    finder = Finder()
    top_ads, price = finder.find_car_price(json)
    print("DONE!")
    # print("Result:", price)
    result = cars_to_json(top_ads, price)
    # print(str(json))

    return jsonify(result)
    # return jsonify(
    #     {
    # 		"bestprice": "374718484",
    # 		"bestvariants": {
    # 			"info1": {
    # 				"id": "1",
    # 				"Двигатель": "Дизель",
    # 				"Марка": "BMW",
    #                 # "Ссылка": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjjtv2hrKnhAhWwy6YKHRLRB2QQjRx6BAgBEAU&url=https%3A%2F%2Fbugaga.ru%2Fjokes%2F1146744172-foto-prikoly-i-kartinki.html&psig=AOvVaw0j3AxioA8lvBeP0rH5olLP&ust=1554017449100132"
    # 			},

    # 			"info2": {
    # 				"id": "2",
    # 				"Двигатель": "Дизель",
    # 				"Марка": "BMW",
    # 				"Пробег": "200"
    # 			}
    # 		}
    # 	}
    # )