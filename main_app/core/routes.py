from flask import Blueprint, jsonify, redirect, render_template, request, url_for, session
from .extensions import mongo


core = Blueprint('core', __name__)


# @core.route('/', methods=['GET'])
# def index():
#     user_collection = mongo.db.users

#     # print(user_collection.count_documents())

#     final_data = []
#     for i in user_collection.find({}):
#         data = {
#             "id": str(i['_id']),
#             "username": i['username'],
#             "email": i['email'],
#             "phone": i['phone']
#         }

#         final_data.append(data)

#     return jsonify(final_data)


# @core.route('/users', methods=['GET', 'POST'])
# def UserPage():
#     user = mongo.db.users
#     if request.method == 'POST':
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         username = request.form.get('username')

#         user.insert_one({'email': email, 'phone': phone, 'username': username})

#     return render_template('user.html')


# @core.route('/login', methods=['GET', 'POST'])
# def login():

#     User = mongo.db.users

#     form = LoginForm()

#     if form.validate_on_submit():
#         user = User.find_one_or_404({'email': form.email.data})

#         if user:
#             login_user(user)

#             return redirect(url_for('users.html'))

#     return render_template('login.html', form=form)


@ core.route('/')
def index():

    if 'email' in session:

        return f'You are logged in as {session["email"]}'

    return 'Not logged in'


@ core.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':

        users = mongo.db.users

        login_user = users.find_one_or_404({'email': request.form['email']})

        if login_user:

            session['email'] = request.form['email']

            return redirect(url_for('core.index'))

    return render_template('login.html')


@ core.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':

        users = mongo.db.users

        existing_user = users.find_one({'email': request.form['email']})

        if existing_user is None:

            users.insert_one(
                {'email': request.form['email'], 'phone': request.form['phone'], 'username': request.form['username']})

            session['email'] = request.form['email']

            return redirect(url_for('core.register'))

        return 'That email already exists'

    return render_template('user.html')


@ core.route('/logout')
def logout():

    session.pop('email', None)


@ core.route('/messages', methods=['GET', 'POST'])
def messages():
    message_collection = mongo.db.messages

    if request.method == 'POST':

        message_collection.insert_one(
            {'sender': request.form['sender'],
             'receiver': request.form['receiver'], 'text': request.form['text']},
        )

        return redirect(url_for('core.messages'))

    messages = mongo.db.messages
    final_data = []
    for i in messages.find({}):
        data = {
            "id": str(i['_id']),
            "sender": i['sender'],
            "receiver": i['receiver'],
            "text": i['text']
        }

        final_data.append(data)

    print(final_data)

    return jsonify(final_data)

    # return render_template('message.html', data=final_data)


@ core.route('/messages/sender', methods=['GET', 'POST'])
def filtered_messages_sender():

    messages = mongo.db.messages

    if request.method == 'POST':
        
        sender = request.form.get('sender')

        print(sender)

    final_data = []
    for i in messages.find({'sender': sender}):
        data = {
            "id": str(i['_id']),
            "sender": i['sender'],
            "receiver": i['receiver'],
            "text": i['text']
        }

        final_data.append(data)

    print(final_data)

    return jsonify(final_data)


@ core.route('/messages/receiver', methods=['GET', 'POST'])
def filtered_messages_receiver():

    messages = mongo.db.messages

    if request.method == 'POST':

        receiver = request.form.get('receiver')

    final_data = []
    for i in messages.find({'receiver': receiver}):
        data = {
            "id": str(i['_id']),
            "sender": i['sender'],
            "receiver": i['receiver'],
            "text": i['text']
        }

        final_data.append(data)

    print(final_data)

    return jsonify(final_data)


@ core.route('/messages/filter', methods=['GET', 'POST'])
def filtered_messages():

    messages = mongo.db.messages

    if request.method == 'POST':

        sender = request.form.get('sender')
        receiver = request.form.get('receiver')

    final_data = []
    for i in messages.find({'sender': sender, "receiver": receiver}):
        data = {
            "id": str(i['_id']),
            "sender": i['sender'],
            "receiver": i['receiver'],
            "text": i['text']
        }

        final_data.append(data)

    print(final_data)

    return jsonify(final_data)
