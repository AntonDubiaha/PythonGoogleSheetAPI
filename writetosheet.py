from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


# File obtained from Google Developer Console
CREDENTIALS_FILE = 'calcium-ember-411712-632c0ca10ef1.json'
# Google Sheets document ID (can be obtained from its URL on the spreadsheet)
spreadsheet_id = '1GYANbpDsJ6hS4S3xf-Qs95c8lAROkM6AlzAFuoUccDQ'

# Authorize and obtain service - an instance of access to the API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

with open('charvalues.txt', 'r', encoding="utf-8") as file:
    char_values = [line.strip() for line in file]

# Prepare data for updating the table
update_data = {
    "valueInputOption": "USER_ENTERED",
    "data": [
        {
            "range": "A3:A" + str(len(char_values) + 2),
            "majorDimension": "COLUMNS",
            "values": [char_values]
        }
    ]
}

# Update the table
values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body=update_data
).execute()
