from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# 
import database

# Configure application
app = Flask(__name__)

# ensure database sqlite 
# app.config['SECRET_KEY'] = 'test'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_log.db'

# db = SQLAlchemy(app)
# db.init_app(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/day")
def day():
    return render_template("day.html")

@app.route("/add_food", methods=["GET", "POST"])
def add_food():
    if request.method == "POST":
        name = request.form.get('food-name')
        protein = int(request.form.get('protein'))
        carbohydrates = int(request.form.get("carbohydrates"))
        fat = int(request.form.get('fat'))

        calories = protein * 4 + carbohydrates * 4 + fat * 9
        # Insert into food table
        database.add_food(name, protein, carbohydrates, fat, calories)
    
    # Select * from food
    get_food = database.get_food()
    # else:
    return render_template("add_food.html", get_food=get_food)


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
