from __future__ import print_function
from auth import get_creds
from apiclient.http import MediaFileUpload

def uploadFile(file_name):
    drive_service = get_creds()
    file_metadata = {'name': file_name}
    media = MediaFileUpload(file_name,
                            mimetype='image/jpeg')
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print
    'File ID: %s' % file.get('id')
