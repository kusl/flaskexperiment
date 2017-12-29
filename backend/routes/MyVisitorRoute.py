from flask import Blueprint, jsonify

from my_message.MyVisitor import MyVisitor

MyVisitorRoute = Blueprint('my_visitor_route', __name__)


@MyVisitorRoute.route('/api/v0/visitor')
def get_visitors():
    results = MyVisitor.query.all()
    if results is None:
        return jsonify({"error": "There is no visitor"})
    all_visitors = [visitor.serialize for visitor in results]
    return jsonify(all_visitors)
