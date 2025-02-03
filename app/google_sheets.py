import os

import dotenv
import gspread
import re

from oauth2client.service_account import ServiceAccountCredentials

dotenv.load_dotenv()

# Подключение Гугл Таблицы
scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("../credentials.json", scopes)
gc = gspread.authorize(credentials)
spreadsheet = gc.open_by_key(os.getenv("TABLE_ID"))
sheet = spreadsheet.worksheet("Автопостинг")


def get_data():
    """
    Получает все данные таблицы
    https://docs.google.com/spreadsheets/d/14Ju7XOkv9_x7uxdEyCEOgzD7EJuVXtc_54zvCutGu54/edit?gid=231521991#gid=231521991
    Листа Автопостинг - с помощью creds (google sheets api) - читать доку + выдать доступ к сервисному аккаунту на редактирование (можно и на чтение)
    :return: все данные в виде матрицы (список списков)
    """
    data = sheet.get_values(value_render_option="FORMULA")
    return data


def convert_to_download_url(cell_value):
    """
    Из ссылки таблицы '=IMAGE(URL)' делает ссылку на скачивание фото с гугл диска, используя regular expressions
    :param формула для показа фото в гугл таблицах:
    :return: ссылка для скачивания
    """
    match = re.search(r'IMAGE\("https://drive\.google\.com/uc\?export=view&id=([^"]+)"\)', cell_value)
    if match:
        file_id = match.group(1)
        return f"https://drive.google.com/uc?export=download&id={file_id}"
    return cell_value


def brease_row(row: list):
    """
    Разделяет строку таблицы на более удобные значения
    :param список из get_data:
    :return: готовые отдельные параметры (номер телефона, ссылка на группу для отправки сообщения, текст сообщения и список ссылок для скачивания)
    """
    phone = row[2]
    channels = row[3].split('\n')
    message = row[4]
    images_row = row[5:]
    images = list()

    for image in images_row:
        images.append(convert_to_download_url(image))

    return phone, channels, message, images
