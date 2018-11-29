from __future__ import print_function
from auth import get_creds
import dateutil.parser
from datetime import datetime, timezone
import requests

# If modifying these scopes, delete the file token_two.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

def listFile():
    service = get_creds()
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name, mimeType)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1}) {2}'.format(item['name'], item['id'], item['mimeType']))

def oldestFile():
    oldest_date = datetime.now(timezone.utc)
    oldest_date = oldest_date.isoformat()
    oldest_date = dateutil.parser.parse(oldest_date)
    service = get_creds()
    results = service.files().list(
        pageSize=1000, fields="nextPageToken, files(createdTime)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        for item in items:
            string_date_test = item["createdTime"]
            formatted_date_test = dateutil.parser.parse(string_date_test)
            formatted_date_test = formatted_date_test
            if formatted_date_test < oldest_date:
                oldest_date = formatted_date_test
        return oldest_date


def cleanEmptyFolders():
    print("Deleting all empty folders")
    service = get_creds()
    results = service.files().list(
        pageSize=500, fields="nextPageToken, files(id, name)", q="mimeType = 'application/vnd.google-apps.folder' ").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        for item in items:
            response = service.files().list(q=("'%s' in parents"%(item['id'])),
                                            spaces='drive',
                                            fields='files(id, name, parents)').execute()
            if len(response["files"]) == 0:
                print("Deleted %s" % (item['id']))
                service.files().delete(fileId=item['id']).execute()



if __name__ == "__main__":
    cleanEmptyFolders()