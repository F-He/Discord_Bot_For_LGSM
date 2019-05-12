class Updater():
    def __init__(self, project_path: str):
        self._project_path = project_path
        self._file_data = {
            "main.py": {
                "path": "/main.py",
                "url": "https://raw.githubusercontent.com/F-He/Discord_Bot_For_LGSM/master/discord_bot/main.py?token=AGGAI2E5Y57C6547LJFA45K44F7JO"
                },
            "Config.py": {
                "path": "/src/Config.py",
                "url": ""
                },
            "Embeds.py": {
                "path": "/src/Embeds.py",
                "url": ""
                },
            "Server.py": {
                "path": "/src/Server.py",
                "url": ""
                },
            "Updater.py": {
                "path": "/src/Updater.py",
                "url": ""
                },
            "Utils.py": {
                "path": "/src/Utils.py",
                "url": ""
                },
            "isOnline": {
                "path": "/src/sh/isOnline",
                "url": ""
                },
        }
