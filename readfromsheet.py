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


id_products = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='Печи, буржуйки, булерьяны!A3:A228',
    majorDimension='COLUMNS'
).execute()

values_to_write = id_products.get('values', [])

file_name = "id_products.txt"
with open(file_name, "w") as file:
    for row in values_to_write:
        for value in row:
            file.write(f"{int(value)}\n")
