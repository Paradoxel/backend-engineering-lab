import requests
BASE_URL = "https://official-joke-api.appspot.com/random_joke"

class JokeClinet:
    def fetch(self):
        data = requests.get(BASE_URL).json()
        return data

    def format(self):
        format_data = self.fetch()
        return f"{format_data["setup"]} - {format_data["punchline"]}"

    def show(self):
        print(self.format())

j = JokeClinet()
j.show()