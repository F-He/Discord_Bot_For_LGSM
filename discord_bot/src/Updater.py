import json
import requests


class Updater():
    def __init__(self, project_path: str):
        self._project_path = project_path
        self._file_data = self._load_data()
        self.get_new_file_data()

    def _load_data(self):
        with open(self._project_path + "/src/update_info.json", "r") as file:
            return json.loads(file.read())

    def get_version(self):
        return self._file_data["version"]

    def check_version(self):
        raw_update_info = requests.get(self._file_data["update_file_url"])
        update_info = json.loads(raw_update_info.text)
        print(update_info["version"])
        if update_info["version"] == self.get_version():
            print("up to date")
        else:
            print("update is available")

    def get_new_file_data(self):
        new_data = {}
        for file, data in self._file_data["file_data"].items():
            new_raw_file_data = requests.get(data["url"])
            new_data[file] = new_raw_file_data.text
            print(new_data[file])
