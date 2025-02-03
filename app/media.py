import os

import requests


def download_images(url_list, folder="../media"):
    """
    Запросом скачиваем фотографии и нумеруем их от 1 до ...
    :param список ссылко для скачивания (функция из google_sheets.py):
    :param папка для сохранения (установлена по умолчанию):
    """
    os.makedirs(folder, exist_ok=True)

    for i, url in enumerate(url_list, start=1):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            file_path = os.path.join(folder, f"{i}.jpg")
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)

