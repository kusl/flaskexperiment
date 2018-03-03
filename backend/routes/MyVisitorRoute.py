from flask import Blueprint, jsonify

from my_message.MyVisitor import MyVisitor

MyVisitorRoute = Blueprint('my_visitor_route', __name__)


@MyVisitorRoute.route('/api/v0/visitor')
def get_visitors():
    from my_message.MyVisitor import save_visitor
    from flask import request
    save_visitor(this_request=request)
    results = MyVisitor.query.all()
    if results is None:
        return jsonify({"error": "There is no visitor"})
    all_visitors = [visitor.serialize for visitor in results]
    return jsonify(all_visitors)


@MyVisitorRoute.route('/visitors')
def display_visitors():
    from my_message.MyVisitor import save_visitor
    from flask import request
    save_visitor(this_request=request)
    results = MyVisitor.query.all()
    print(results)
    if results is None:
        return jsonify({"error": "There is no visitor"})
    all_visitors = [visitor.serialize for visitor in results]
    from flask import render_template
    return render_template("pages/visitors.html", visitors=results)
