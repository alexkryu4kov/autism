from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

from algo.experiment import Experiment
from database.models import Picture,Game
from mail.mail import Mailer


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://autist:pass@localhost:5432/postgres'
db = SQLAlchemy(app)
db.create_all()


@app.route('/pictures', methods=['GET','POST'])
def return_picture():
    exp = Experiment()
    if request.method == 'GET':
        db.session.add(Picture(id =0, name='1', category='animal', picture='vk.com'))
        db.session.commit()
        return 'success'
    if request.method == 'POST':
        pictures = db.session.query(Picture)
        for picture in pictures:
            return picture.picture
        return jsonify(exp.choose_elem())


@app.route('/metrics', methods=['GET', 'POST'])
def send_mail():
    mail = Mailer('login', 'password')
    if request.method == 'GET':
        return jsonify(mail.login, mail.password)


if __name__ == '__main__':
    app.run(debug=True)


@app.errorhandler()
def handle_bad_request(e):
    return 'bad request!', 400
