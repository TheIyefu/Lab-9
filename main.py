import flask 
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/test_db7'
db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    visit_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"City(name='{self.name}', visit_date='{self.visit_date}')"


@app.route('/')
def index():
    cities = City.query.all()
    return render_template('index.html', cities=cities)


@app.route('/add', methods=['POST'])
def add():
    name = request.form['city']
    visit_date = request.form['date']

    city = City(name=name, visit_date=visit_date)
    db.session.add(city)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)
