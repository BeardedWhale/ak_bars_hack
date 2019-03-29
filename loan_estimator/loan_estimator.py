from flask import Blueprint, flash, redirect, render_template, request, url_for

bp = Blueprint('loan_estimator', __name__)

@bp.route('/')
def index():
    return "Hello from akbars hack backend!"

@bp.route('/test', methods=["POST"])
def test():
    json = request.get_json()
    return "Hello from test" if json == None else ''.join(dict(json))