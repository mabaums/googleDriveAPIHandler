from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
from auth import get_creds
from datetime import datetime, timezone, timedelta
from listFile import oldestFile
from monthToString import monthToString
from dateutil.relativedelta import relativedelta

def createFolder(name):
    drive_service = get_creds()
    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()
    print
    'Folder ID: %s' % file.get('id')

def createDateFolders(oldest_date):
    print("Creating folders by month/year")
    oldest_date = oldest_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    current_date = datetime.now(timezone.utc)
    while oldest_date < current_date:
        createFolder("%s %s" %(monthToString(oldest_date.month), oldest_date.year))
        print("created folder %s %s" %(monthToString(oldest_date.month), oldest_date.year))
        oldest_date = oldest_date + relativedelta(months=1)