from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
from listFile import listFile, oldestFile, cleanEmptyFolders
from uploadFile import uploadFile
from downloadFile import downloadFile
from createFolder import createFolder, createDateFolders
from searchFile import keywordSearchFile,dateSearchFile
from transferFile import transferFile, transfer_by_date
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--list", help="Lists all files by pages", action="store_true")
parser.add_argument("-u", "--upload", help="Uploads a particular file", action="store")
parser.add_argument("-d", "--download", help="Downloads a particular file", action="store")
parser.add_argument("-t", "--transfer", help="Transfers file from one folder to another", action="store")
parser.add_argument("-s", "--search", help="Searches files by keyword", action="store")
parser.add_argument("-i", "--superSort", help="Sorts all files into folders by Month/Year", action="store_true")
args = parser.parse_args()


# If modifying these scopes, delete the file token_two.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

if args.list:
    listFile()

if args.upload:
    file_name = args.upload
    uploadFile(file_name)

if args.search:
    keyword = args.search
    keywordSearchFile(keyword)

if args.download:
    file_to_download = args.download

if args.superSort:
    cleanEmptyFolders()
    oldest_date = oldestFile()
    createDateFolders(oldest_date)
    transfer_by_date()
    cleanEmptyFolders()

if args.transfer:
    transfer_string = args.transfer
    transfer_array = transfer_string.split(',')
    transfer_file = transfer_array[0]
    transfer_destination = transfer_array[1]
    transfer_file_id = keywordSearchFile(transfer_file)
    transfer_destination_id = keywordSearchFile(transfer_destination)
    transferFile(transfer_file_id, transfer_destination_id)