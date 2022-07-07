import google_auth_oauthlib
import gspread
import os
from httplib2 import Credentials
from oauth2client.service_account import ServiceAccountCredentials
import dotenv

dotenv.load_dotenv()

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("secret.json", scope)
sheet = gspread.authorize(credentials)

opengooglesheet = sheet.open(os.getenv("SHEET_NAME"))

with open("./data/"+os.getenv('data_csv'), 'rb') as file:
    content = file.read()
    sheet.import_csv(opengooglesheet.id, data=content)
