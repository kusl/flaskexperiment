from flask import Flask, render_template, request

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
