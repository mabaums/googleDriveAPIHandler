from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools

# If modifying these scopes, delete the file token_two.json.
SCOPES = 'https://www.googleapis.com/auth/drive'


def get_creds():
    store = oauth_file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        try:
            creds = tools.run_flow(flow, store)
        except Exception as e:
            print("hello")
    service = build('drive', 'v3', http=creds.authorize(Http()))
    return service

