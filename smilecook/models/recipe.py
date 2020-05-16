recipe_list = []


def get_last_id():

    if not recipe_list:
        return 1

    return len(recipe_list) + 1


class Recipe:

    def __init__(self, name, description, num_of_servings, cook_time, directions):
        self.id = get_last_id()
        self.name = name
        self.description = description
        self.num_of_servings = num_of_servings
        self.cook_time = cook_time
        self.directions = directions
        self.is_publish = False



    @property
    def data(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'num_of_servings': self.num_of_servings,
            'cook_time': self.cook_time,
            'directions': self.directions,
           'is_publish': self.is_publish
       }