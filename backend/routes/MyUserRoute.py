from flask import Blueprint, jsonify, render_template

from my_message.MyUser import MyUser

MyUserRoute = Blueprint('my_user_route', __name__)


@MyUserRoute.route('/api/v0/user/all')
def get_all_users():
    from my_message.MyVisitor import save_visitor
    from flask import request
    save_visitor(this_request=request)
    results = MyUser.query.all()
    if results is None:
        return jsonify({"error": "There is no user"})
    all_users = [user.serialize for user in results]
    return jsonify(all_users)

@MyUserRoute.route('/api/v0/user/add')
def add_user():
    from my_message.MyVisitor import save_visitor
    from flask import request
    save_visitor(this_request=request)
    from my_message.MyUser import create_random_user
    create_random_user().save()
    return jsonify({"Status": "Success"})
