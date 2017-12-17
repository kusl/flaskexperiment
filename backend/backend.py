import uuid
from datetime import datetime, timedelta

from flask import Flask, render_template, make_response, request, jsonify

import secret
import shared
from my_message.MyVisitor import MyVisitor
from routes.MyMessageRoute import MyMessageRoute

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = secret.SQLALCHEMY_DATABASE_URI
shared.db.init_app(app)
app.register_blueprint(MyMessageRoute)


@app.route('/', methods=['GET'])
def drop_and_create():
    visitor = MyVisitor(visitor_id=uuid.uuid4(),
                        visitor_ip=request.remote_addr,
                        visit_time=datetime.now(),
                        visitor_info="{}")
    visitor.save()
    return render_template('pages/index.html')


@app.route('/clear', methods=['GET'])
def clear():
    shared.db.drop_all()
    shared.db.create_all()
    return jsonify({"status": "success"})


@app.route('/get')
def get_first_visitor():
    results = MyVisitor.query.all()
    if results is None:
        return jsonify({"error": "There is no visitor"})
    visitors = []
    for result in results:
        print(result.ip)
        visitors.append(result.ip)
    return jsonify(visitors)


# a route for generating sitemap.xml
@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Generate sitemap.xml. Makes a list of urls and date modified."""
    pages = []
    ten_days_ago = (datetime.now() - timedelta(days=10)).date().isoformat()
    # static pages
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments) == 0:
            pages.append(
                [f"http://45.55.240.4{rule.rule}", ten_days_ago]
            )
    #
    # # user model pages
    # users = User.query.order_by(User.modified_time).all()
    # for user in users:
    #     url = url_for('user.pub', name=user.name)
    #     modified_time = user.modified_time.date().isoformat()
    #     pages.append([url, modified_time])

    sitemap_xml = render_template('pages/sitemap.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
