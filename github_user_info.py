import requests
import json
from datetime import datetime
import os  # для работы с путями

# Список пользователей GitHub
usernames = ["ilkona1", "torvalds", "octocat"]

results = {}

for username in usernames:
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    data = response.json()

    data["request_date"] = datetime.now().isoformat()

    results[username] = {
        "name": data.get("name"),
        "login": data.get("login"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "request_date": data["request_date"]
    }

# Путь к файлу рядом с этим скриптом
script_dir = os.path.dirname(os.path.abspath(__file__))  # папка скрипта
file_path = os.path.join(script_dir, "result.json")

# Сохраняем результат
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print(f"Данные получены и сохранены в {file_path}")
