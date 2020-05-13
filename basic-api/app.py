from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

recipes = [{'id': 1, 'name': 'Egg Salad', 'description': 'egg nd leafy things'},
           {'id': 2, 'name': 'Paneer Tikka', 'description': 'Paneer nd coal'}]


@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify({'data': recipes})


@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):

    try:
        next_dish = next((dish for dish in recipes if dish['id'] == recipe_id), None)
    except Exception as E:
        print("An exception occurred : ", E)


    if next_dish:
        return jsonify(next_dish)
    else:
        return jsonify({'message': 'Dish not found'}), HTTPStatus.NOT_FOUND

if __name__ == "__main__":
    app.run()

