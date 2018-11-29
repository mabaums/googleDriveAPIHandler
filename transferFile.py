from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
from listFile import listFile
from uploadFile import uploadFile
from downloadFile import downloadFile
from createFolder import createFolder
from searchFile import keywordSearchFile
from monthToString import monthToString
import dateutil.parser
from auth import get_creds
SCOPES = 'https://www.googleapis.com/auth/drive'


def transferFile(file_id, new_folder_id):
    print("Transfering file: " + file_id + " to folder: " + new_folder_id)
    drive_service = get_creds()
    file = drive_service.files().get(fileId=file_id,
                                     fields='parents').execute()
    try:
        previous_parents = ",".join(file.get('parents'))
    except TypeError:
        print('no parents')
        previous_parents = None
    drive_service.files().update(fileId=file_id,
                                 removeParents=previous_parents,
                                 addParents=new_folder_id,
                                 fields='id, parents').execute()


def transfer_by_date():
    print("Transfering all files to respective month/year folders")
    drive_service = get_creds()
    results = drive_service.files().list(
        pageSize=1000, fields="nextPageToken, files(createdTime, id, name)", q="mimeType = 'application/vnd.google-apps.document'").execute()
    items = results.get('files', [])
    for i in range(0,(len(items)-1)):
        file_date = items[i]["createdTime"]
        fileId = items[i]["id"]
        file_date = dateutil.parser.parse(file_date)
        file_month = file_date.month
        file_year = file_date.year
        file_month = monthToString(file_month)

        file_year = str(file_year)
        month_year = file_year + " " + file_month
        folderId = date_search_file(month_year)
        transferFile(fileId, folderId)


def date_search_file(month_year):
    service = get_creds()
    results = service.files().list(
        pageSize=100, fields="nextPageToken, files(id, name, createdTime)",  q=("name contains " + "'" + month_year
                                                                                + "'")).execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        for item in items:
            (u'{0} ({1})'.format(item['name'], item['id']))
        return item["id"]

if __name__ == "__main__":
    transfer_by_date()