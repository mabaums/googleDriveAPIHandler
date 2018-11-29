from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
from auth import get_creds
SCOPES = 'https://www.googleapis.com/auth/drive'

def keywordSearchFile(keyword):
    service = get_creds()
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name, createdTime)",  q=("name contains " + "'" + keyword + "'")).execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
        return item["id"]

def dateSearchFile(date):
    service = get_creds()
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name, createdTime)",
        q=("name contains " + "'" + keyword + "'")).execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
        return item["id"]