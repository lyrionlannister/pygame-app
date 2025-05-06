import os
import json


class ScoreManager:

    def __init__(self, filename="memory.json"):
        self.filename = filename
        self.file_path = os.path.join(os.path.dirname(__file__), filename)
        print(f"File path: {self.file_path}")
        self.scores: list = self.load_scores()

    def load_scores(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_scores(self):
        with open(self.filename, "w") as file:
            json.dump(self.scores, file)

    def add_score(self, name, score):
        self.scores[name] = score
        self.save_scores()

    def get_score(self, name):
        return self.scores.get(name, None)

    def get_all_scores(self):
        return self.scores


score_manager = ScoreManager()
