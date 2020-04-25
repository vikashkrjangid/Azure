from azure.storage.blob import BlockBlobService
from io import BytesIO
from io import StringIO

def download(blob_con_string,container_name,blob_name,download_file_path):
    blob_service =  BlockBlobService(connection_string=blob_con_string)
    stream = BytesIO()
    download_data = blob_service.get_blob_to_text(container_name=container_name,blob_name=blob_name).content
    with open(download_file_path, "w+") as download_file:
        download_file.write(download_data)
    download_file.close()