from chefs import IndianChef, ItalianChef, FrenchChef, MexicanChef, JapaneseChef
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
def get_chef(chef_name, api_key):
    chef_classes = {
        'indian': IndianChef,
        'italian': ItalianChef,
        'french': FrenchChef,
        'mexican': MexicanChef,
        'japanese': JapaneseChef
    }
    chef_class = chef_classes.get(chef_name.lower())
    if chef_class:
        return chef_class(api_key)
    else:
        return None

def main():
    api_key = openai_api_key
    chef_name = input("Choose your chef (Indian, Italian, French, Mexican, Japanese): ")
    chef = get_chef(chef_name, api_key)
    if chef is None:
        print("Chef not found.")
        return

    input_text = input("Enter your ingredients, dish name for the recipe, or recipe to criticize: ")
    response = chef.process_input(input_text)
    print(response)

if __name__ == "__main__":
    main()
