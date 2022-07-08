from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for, Response
from .extensions import mongo

core = Blueprint('core', __name__)


@core.route('/', methods=['GET'])
def index():
    user_collection = mongo.db.users
    users = user_collection.find_one_or_404()

    print(users.values())

    data = {
        "id": users['_id'],
        "username": users['username'],
        "email": users['email'],
        "phone": users['phone']
    }

    print(data)

    return {"data": data}


@core.route('/users', methods=['GET', 'POST'])
def UserPage():
    user = mongo.db.users
    if request.method == 'POST':
        email = request.form.get('email')
        phone = request.form.get('phone')
        username = request.form.get('username')

        user.insert_one({'email': email, 'phone': phone, 'username': username})

        print(email)
