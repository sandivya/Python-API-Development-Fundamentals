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


@app.route('/recipes', methods=['POST'])
def create_recipe():
    labour = request.get_json()
    recipe_name = labour.get('name')
    recipe_description = labour.get('description')

    recipe = {
        'id': len(recipes)+1,
        'name': recipe_name,
        'description': recipe_description
    }

    recipes.append(recipe)
    return jsonify(recipe), HTTPStatus.CREATED


@app.route('/recipes/<int:recipe_id>', methods=['POST'])
def update_recipe(recipe_id):

    present_dish = next((dish for dish in recipes if dish['id'] == recipe_id), None)

    if not present_dish:
        return jsonify({'message': 'DISH NOT FOUND'}), HTTPStatus.NOT_FOUND
    else:
        labour = request.get_json()

        recipes.update({
            'name': labour.get('name'),
            'description': labour.get('description')
        })

        return jsonify(recipes)


@app.route('/recipes/delet/<int:recipe_id>', methods=['GET'])
def delete_recipes(recipe_id):

    if request.method == "DELETE":

        dish = next((dish for dish in recipes if dish['id'] == recipe_id), None)

        if not dish:
            return jsonify({'message': 'Dish does not exist'}),  HTTPStatus.NOT_FOUND
        else:
            recipes.remove(dish)

        return {}, HTTPStatus.NO_CONTENT

if __name__ == "__main__":
    app.run()

