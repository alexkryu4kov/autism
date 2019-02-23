from flask import Flask
from flask import request, jsonify

from algo.experiment import Experiment
from database import db,models
from mail.mail import Mailer


app = Flask(__name__)


@app.route('/pictures', methods=['GET', 'POST'])
def return_picture():
    exp = Experiment()
    session
    if request.method == 'GET':
        return 'Lukyan petuh'
    if request.method == 'POST':
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
