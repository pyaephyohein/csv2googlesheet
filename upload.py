from cgi import test
from curses import raw
import google_auth_oauthlib
import gspread
import os
from httplib2 import Credentials
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from dateutil.relativedelta import relativedelta
import dotenv
import sys

dotenv.load_dotenv()

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]


one_year_from_now = datetime.datetime.now() + relativedelta(years=0)
date_formated = one_year_from_now.strftime("%d-%m-%Y(%-I: %-M)")
credentials = ServiceAccountCredentials.from_json_keyfile_name("secret.json", scope)
sheet = gspread.authorize(credentials)
rawsheet = sheet.open(os.getenv("RAW_SHEET"))
formatedsheet = sheet.open(os.getenv("FORMATED_SHEET"))
# opengooglesheet = sheet.open_by_key('1OY64Ud0fZaftuAJMoMVDX54-qFhYRCqqpoSkJob2Jd4')
formatedsheet.add_worksheet(title=date_formated, rows= 10000, cols= 100)

def main (argv):
    inputfile = str(argv[0])
    with open(inputfile, 'rb') as file:
        content = file.read()
        sheet.import_csv(rawsheet.id, content)
# print(opengooglesheet.worksheet(title=date_formated))
    allvalues = rawsheet.worksheet("Raw").get_all_values()
    formatedsheet.worksheet(title=date_formated).update(allvalues)

if __name__ == "__main__":
   main(sys.argv[1:])