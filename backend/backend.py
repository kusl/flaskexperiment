from datetime import datetime, timedelta

from flask import Flask, render_template, make_response, request, jsonify

import secret
import shared
from my_message.MyVisitor import MyVisitor
from routes.MyMessageRoute import MyMessageRoute
from routes.MyVisitorRoute import MyVisitorRoute

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = secret.SQLALCHEMY_DATABASE_URI
shared.db.init_app(app)
app.register_blueprint(MyMessageRoute)
app.register_blueprint(MyVisitorRoute)


@app.route('/', methods=['GET'])
def get_home():
    from my_message.MyVisitor import save_visitor
    save_visitor(this_request=request)
    return render_template('pages/index.html')


@app.route('/clear', methods=['GET'])
def clear():
    try:
        searchword = request.args.get('key', '')
        if "hunter2" == searchword:
            shared.db.drop_all()
            shared.db.create_all()
            from my_message.MyVisitor import save_visitor
            save_visitor(this_request=request)
            return jsonify({"status": "success"})
        return jsonify({"status": "unauthorized"})
    except KeyError:
        return jsonify({"status": "failed"})


@app.route('/get')
def get_visitors():
    results = MyVisitor.query.all()
    if results is None:
        return jsonify({"error": "There is no visitor"})
    all_visitors = [visitor.serialize for visitor in results]
    return jsonify(all_visitors)


# a route for generating sitemap.xml
@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Generate sitemap.xml. Makes a list of urls and date modified."""
    from my_message.MyVisitor import save_visitor
    save_visitor(this_request=request)
    pages = []
    ten_days_ago = (datetime.now() - timedelta(days=10)).date().isoformat()
    # static pages
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments) == 0:
            pages.append(
                [f"http://45.55.240.4{rule.rule}", ten_days_ago]
            )
    sitemap_xml = render_template('pages/sitemap.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
