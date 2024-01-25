from pprint import pprint
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

def update_spreadsheet(file_name, column, offset=1, sheet_name=""):
    CREDENTIALS_FILE = 'calcium-ember-411712-632c0ca10ef1.json'
    spreadsheet_id = '1GYANbpDsJ6hS4S3xf-Qs95c8lAROkM6AlzAFuoUccDQ'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

    with open(file_name, 'r', encoding="utf-8") as file:
        char_values = [line.strip() for line in file]

    update_data = {
        "valueInputOption": "USER_ENTERED",
        "data": [
            {
                "range": f"{sheet_name}!{column}{offset}:{column}{offset + len(char_values) - 1}",
                "majorDimension": "COLUMNS",
                "values": [char_values]
            }
        ]
    }

    values = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body=update_data
    ).execute()

# Example
# update_spreadsheet('charvalues3.txt', 'E', 3, "Печи, буржуйки, булерьяны")
