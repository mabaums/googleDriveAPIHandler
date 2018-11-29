from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
from apiclient.http import MediaIoBaseDownload
from auth import get_creds
import io

def downloadFile(file_id,filepath):
    drive_service = get_creds()
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print
        "Download %d%%." % int(status.progress() * 100)
    with io.open(filepath, 'wb') as f:
        fh.seek(0)
        f.write(fh.read())