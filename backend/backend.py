from flask import Flask, render_template

import secret
import shared
from routes.MyMessageRoute import MyMessageRoute

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = secret.SQLALCHEMY_DATABASE_URI
shared.db.init_app(app)
app.register_blueprint(MyMessageRoute)


@app.route('/', methods=['GET'])
def drop_and_create():
    shared.db.drop_all()
    shared.db.create_all()
    return render_template('pages/index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
