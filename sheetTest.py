import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('bot-test-4b7ed705e867.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('gspreadSample').sheet1

wks.update_acell('A1', 'World!')
print(wks.acell('A1'))
