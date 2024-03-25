import openai

class Chef:
    def __init__(self, api_key, personality):
        openai.api_key = api_key
        self.personality = personality

    def process_input(self, input_text):
        if ',' in input_text:
            prompt = f"{self.personality}, suggest a dish using these ingredients: {input_text}"
        elif input_text.lower().endswith('recipe'):
            prompt = f"{self.personality}, provide a recipe for {input_text[:-7]}"
        elif "recipe for" in input_text.lower():
            prompt = f"{self.personality}, critique this recipe: {input_text}"
        else:
            return "Please provide a list of ingredients, a dish name for the recipe, or a recipe to criticize."

        return self.query_openai(prompt)

    def query_openai(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )
        content = []
        for chunk in response:
            content.append(chunk.choices[0].delta.get('content', ''))
        return ''.join(content)



class IndianChef(Chef):
    def __init__(self, api_key):
        super().__init__(api_key, "I'm a young and spirited Indian cook that loves to make Biryani")

class ItalianChef(Chef):
    def __init__(self, api_key):
        super().__init__(api_key, "I'm a wise and experienced Italian chef that loves to make pasta")

class FrenchChef(Chef):
    def __init__(self, api_key):
        super().__init__(api_key, "I'm a focused and detail-oriented vegan French chef")

class MexicanChef(Chef):
    def __init__(self, api_key):
        super().__init__(api_key, "I'm a fun and energetic Mexican chef who loves spicy food")

class JapaneseChef(Chef):
    def __init__(self, api_key):
        super().__init__(api_key, "I'm an innovative and creative Japanese chef who enjoys making sushi")