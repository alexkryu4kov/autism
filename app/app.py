from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

from algo.experiment import Experiment
from database.models import Picture, User
from mail.mail import Mailer
from metrics.metrics import Metric

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://autist:pass@localhost:5432/postgres'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
db.create_all()


@app.route('/api/links', methods=['GET'])
def return_link():
    exp = Experiment()
    if request.method == 'GET':
        return jsonify({'links':exp.choose_elem(2)[0]})


@app.route('/api/words', methods=['GET'])
def return_word():
    exp = Experiment()
    if request.method == 'GET':
        return jsonify({'words': exp.choose_elem(2)[1]})


@app.route('/seva', methods=['POST'])
def get_info():
    return request.args['level'], request.args['mode']


@app.route('/api/metrics', methods=['GET', 'POST'])
def send_metrics():
    if request.method == 'GET':
        metric = Metric('Andrew', 600, 100, 0.5)
        return jsonify({'name': metric.name, 'time': metric.time, 'amount': metric.amount, 'quality': metric.quality})

    if request.method == 'POST':
        pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)


@app.errorhandler()
def handle_bad_request(e):
    return 'bad request!', 400
