import json
import requests

update_info_json_path = "/src/update_info.json"


class Updater():
    def __init__(self, project_path: str):
        # self._project_path = project_path
        self._project_path = "E:\\Repos\\Python\\Discord_Bot_For_LGSM\\testing"
        self._update_info_file_data = self._load_update_info()

    def _load_update_info(self):
        with open(self._project_path + update_info_json_path, "r") as file:
            return json.loads(file.read())

    def _update_info_json_data(self):
        with open(self._project_path + update_info_json_path, "w") as file:
            data = self._get_new_info_json_data()
            file.write(data)

    def _get_new_info_json_data(self):
        print("requesting new update info")
        new_data = requests.get(self._update_info_file_data["update_file_url"])
        return new_data.text

    def get_version(self):
        return self._update_info_file_data["version"]

    def _up_to_date(self):
        raw_update_info = requests.get(self._update_info_file_data["update_file_url"])
        update_info = json.loads(raw_update_info.text)
        if update_info["version"] == self.get_version():
            return True
        else:
            return False

    def _get_new_file_data(self):
        new_data = {}
        for file, data in self._update_info_file_data["file_data"].items():
            print(f"fetching new data for {file}")
            new_raw_file_data = requests.get(data["url"])
            new_data[file] = new_raw_file_data.text
        return new_data

    def _write_to_files(self, file_data):
        for name, data in file_data.items():
            print(f"writing new data to {name}")
            with open(self._project_path + self._update_info_file_data["file_data"][name]["path"], "wb") as file:
                file.write(data.encode("utf-8"))

    def start(self):
        if not self._up_to_date():
            self._update()
        else:
            pass

    def _update(self):
        print("Starting update")
        self._update_info_json_data()
        file_data = self._get_new_file_data()
        self._write_to_files(file_data)
        print("done")
