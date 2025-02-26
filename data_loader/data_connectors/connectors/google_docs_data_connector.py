import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import Resource, build
from googleapiclient.errors import HttpError

from data_loader.data_connectors.data_connector import DataConnector

SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]


class GoogleDocsDataConnector(DataConnector):
    def __init__(self, credentials_path: str = None) -> None:
        self.service: Resource = self.connect(credentials_path)

    def connect(self, credentials_path: str = None):
        try:
            with open(credentials_path, "r") as file:
                credentials_dict = json.load(file)
                creds = Credentials(**credentials_dict)
        except FileNotFoundError:
            raise Exception(f"Error: File not found at path: {credentials_path}")
        except json.JSONDecodeError:
            raise Exception(f"Error: Invalid JSON format in file: {credentials_path}")
        finally:
            service: Resource = build("drive", "v3", credentials=creds)
            return service

    def extract(self):
        pass

    def list_files(self):
        results = (
            self.service.files()
            .list(pageSize=10, fields="nextPageToken, files(id, name)")
            .execute()
        )

        items = results.get("files")
