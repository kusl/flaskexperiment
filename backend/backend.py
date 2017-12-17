from flask import Flask, render_template, make_response, request
from datetime import datetime, timedelta
import secret
import shared
from routes.MyMessageRoute import MyMessageRoute

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = secret.SQLALCHEMY_DATABASE_URI
shared.db.init_app(app)
app.register_blueprint(MyMessageRoute)


@app.route('/', methods=['GET'])
def drop_and_create():
    request_ip = request.remote_addr

    print(request_ip)
    shared.db.drop_all()
    shared.db.create_all()
    return render_template('pages/index.html')


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
