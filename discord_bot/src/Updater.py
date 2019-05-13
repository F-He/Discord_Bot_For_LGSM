import json


class Updater():
    def __init__(self, project_path: str):
        self._project_path = project_path
        self._file_data = self._load_data()

    def _load_data(self):
        with open(self._project_path + "/src/update_info.json", "r") as file:
            return json.loads(file.read())


    def get_version(self):
        return self._file_data["version"]
