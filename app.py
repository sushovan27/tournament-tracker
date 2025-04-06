from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from decimal import Decimal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_donation():
    name = request.form['name']
    amount = Decimal(request.form['amount'])
    if amount <= 0 or not name.strip():
        return "Invalid input: Name cannot be empty, and amount must be positive.", 400
    new_donation = Donation(name=name, amount=amount)
    db.session.add(new_donation)
    db.session.commit()
    return redirect(url_for('thanks'))

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/view')
def view_donations():
    donations = Donation.query.all()
    return render_template('view.html', donations=donations)

if __name__ == '__main__':
    app.run(debug=True)