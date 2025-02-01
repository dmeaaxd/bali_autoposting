import os

import dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

dotenv.load_dotenv()

scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("../credentials.json", scopes)
gc = gspread.authorize(credentials)

spreadsheet = gc.open_by_key(os.getenv("TABLE_ID"))

sheet = spreadsheet.worksheet("Автопостинг")

def get_data():
    data = sheet.get_values(value_render_option="FORMULA")
    return data



