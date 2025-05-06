import os
import json


class PlayerManager:
    def __init__(self, filename="players.json"):
        self.filename = filename
        self.path_base = "../memory"
        self.file_path = os.path.abspath(os.path.join(self.path_base, filename))
        self.players: list[dict] = self.load_players()

    def load_players(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_players(self):
        with open(self.file_path, "w") as file:
            json.dump(self.players, file, indent=4)

    def add_player(self, name, score=0):
        self.players.append({"name": name, "score": score})
        self.save_players()

    def get_player(self, name):
        for player in self.players:
            if player["name"] == name:
                return player
        return None

    def get_all_players(self):
        return self.players


player_manager = PlayerManager()
