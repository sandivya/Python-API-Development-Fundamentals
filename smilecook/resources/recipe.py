import sys
import json
from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus
from models.recipe import Recipe, recipe_list


class RecipeListResource(Resource):

    def get(self):

        data = []
        for recipe in recipe_list:
            if recipe.is_publish is True:
                data.append(recipe)

        return {'data': data}, HTTPStatus.OK


    def post(self):

        data = request.get_json()

        recipe = Recipe(name=data['name'],
                        description=data['description'],
                        num_of_servings=data['num_of_servings'],
                        cook_time=data['cook_time'],
                        directions=data['directions']
                        )

        recipe_list.append(recipe)

        return recipe.data, HTTPStatus.CREATED


class RecipeResource(Resource):

    def get(self, recipe_id):

        recipe = next((dish for dish in recipe_list if dish.id == recipe_id and dish.is_publish is True), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        return recipe.data, HTTPStatus.OK

    def put(self, recipe_id):

        data = request.get_json()

        recipe = next((dish for dish in recipe_list if dish.id == recipe_id), None)

        if recipe is None:
            return {'message', 'Recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.name = data['name']
        recipe.description = data['description']
        recipe.num_of_servings = data['num_of_servings']
        recipe.cook_time = data['cook_time']
        recipe.directions = data['directions']

        return recipe.data, HTTPStatus.OK


class RecipePublish(Resource):

    def put(self, recipe_id):

        recipe_update = ""

        print(list(recipe_list))

        for dish in list(recipe_list):
            if dish.id == recipe_id:
                recipe_update = dish

        if recipe_update is None:
            return {'message': 'Recipe not found'}, HTTPStatus.NOT_FOUND

        recipe_update.is_publish = True

        return {'message': 'Recipe published'}, HTTPStatus.NO_CONTENT

    def delete(self, recipe_id):

        recipe = next((dish for dish in recipe_list if dish.id == recipe_id), None)

        if recipe is None:
            return {'message': 'Recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = False

        return {'message': 'Recipe Unpublished'}, HTTPStatus.NO_CONTENT



