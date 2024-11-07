from flask import Flask, jsonify, render_template, request
import json
import random

app = Flask(__name__)

with open('data.json', 'r') as f:
    food_data = json.load(f)

def get_random_foods(num_foods=5):
    """Returns a list of random food items with their ingredients."""
    selected_foods = random.sample(food_data, num_foods)
    return [{'id': food[0], 'name': food[1].split(",")[0].lower(), 'ingredients': [ i.replace("INGREDIENTS:","").strip() for i in food[2]], 'data': food[3]} for food in selected_foods]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_foods')
def get_foods_route():
    foods = get_random_foods()
    return jsonify({"foods": foods})


if __name__ == '__main__':
    app.run(debug=True)