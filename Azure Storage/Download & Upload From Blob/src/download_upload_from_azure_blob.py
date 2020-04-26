from azure.storage.blob import BlockBlobService
from io import BytesIO
from io import StringIO

def download(blob_con_string,container_name,blob_name,download_file):
    blob_service =  BlockBlobService(connection_string=blob_con_string)
    data_stream = BytesIO()
    blob_service.get_blob_to_stream(container_name=container_name,blob_name=blob_name,stream=data_stream)
    with open(download_file,'wb') as out:
        out.write(data_stream.getvalue())
    out.close()

def upload(blob_con_string,container_name,upload_full_file_path,local_full_file_path):
    blob_service =  BlockBlobService(connection_string=blob_con_string)
    blob_service.create_blob_from_path(container_name, upload_full_file_path,local_full_file_path)
