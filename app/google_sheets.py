import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("../credentials.json", scopes)
gc = gspread.authorize(credentials)

spreadsheet = gc.open_by_key("14Ju7XOkv9_x7uxdEyCEOgzD7EJuVXtc_54zvCutGu54")

sheet = spreadsheet.worksheet("Автопостинг")

def get_data():
    data = sheet.get_values(value_render_option="FORMULA")
    return data



