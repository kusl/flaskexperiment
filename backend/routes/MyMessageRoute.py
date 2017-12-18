from flask import Blueprint, jsonify, render_template

from my_message.MyMessage import MyMessage

MyMessageRoute = Blueprint('my_message_route', __name__)


@MyMessageRoute.route('/api/v0/my_message/first')
def get_first_message():
    result = MyMessage.query.first()
    if result is None:
        return jsonify({"error": "There is no message"})
    return jsonify(result.serialize)


@MyMessageRoute.route('/api/v0/my_message/add')
def hello_world():
    from my_message.MyMessage import create_random_message
    create_random_message().save()
    return render_template("pages/add.html")
