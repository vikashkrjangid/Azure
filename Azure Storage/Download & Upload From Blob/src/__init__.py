from  download_upload_from_azure_blob import *

blob_con_string= 'DefaultEndpointsProtocol=https;AccountName=********;AccountKey=*****************************************;EndpointSuffix=core.windows.net'
container_name= 'mycontainer'
blob_name='empdata.csv'
download_file='dowloaded_data_file.csv'

download(blob_con_string,container_name,blob_name,download_file)

local_full_file_path='dowloaded_data_file.csv'
upload_full_file_path='uploaded_data_file.csv'

upload(blob_con_string,container_name,upload_full_file_path,local_full_file_path)