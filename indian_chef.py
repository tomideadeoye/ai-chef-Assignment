class IndianChef:
    def __init__(self):
        self.description = "Young and spirited Indian cook that loves to make Biryani."

    def process_input(self, input_text):
        if ',' in input_text: 
            return self.suggest_dish(input_text)
        elif input_text.lower().endswith('recipe'):
            return self.give_recipe(input_text)
        elif "recipe for" in input_text.lower():
            return self.criticize_recipe(input_text)
        else:
            return "Please provide a list of ingredients, a dish name for the recipe, or a recipe to criticize."

    def suggest_dish(self, ingredients):
        return "With these ingredients, you can make a wonderful Biryani."

    def give_recipe(self, dish_name):
        return "Here is a recipe for a delicious Biryani: ..."

    def criticize_recipe(self, recipe):
        return "This Biryani recipe is good, but here's how it can be improved: ..."