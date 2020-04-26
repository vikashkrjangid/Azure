import os, uuid, sys
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings

def download_file_from_directory(storage_account_name,storage_account_key,my_file_system,my_directory,local_download_to_full_path,adls_download_from_full_path):
    try:
        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
        "https", storage_account_name), credential=storage_account_key)
        
        file_system_client = service_client.get_file_system_client(file_system=my_file_system)
        
        directory_client = file_system_client.get_directory_client(my_directory)
      
        local_file = open(local_download_to_full_path,'wb')

        file_client = directory_client.get_file_client(adls_download_from_full_path)

        download = file_client.download_file()

        downloaded_bytes = download.readall()

        local_file.write(downloaded_bytes)

        local_file.close()

    except Exception as e:
     print(e)
