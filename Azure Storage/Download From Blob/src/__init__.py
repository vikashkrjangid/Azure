from  download_from_azure_blob_stream import *

blob_con_string= 'DefaultEndpointsProtocol=https;AccountName=vikashstorage;AccountKey=1psvKXn97QY89JUsBQ/54209m0RvveBjkbqkAqjuU5fuJFOzgTbBExCZy8smdL+xxytSowTpHBOyUdM9eJtSbg==;EndpointSuffix=core.windows.net'
container_name= 'mycontainer'
blob_name='empdata.csv'
download_file='dowloaded_data_file.csv'

download(blob_con_string,container_name,blob_name,download_file)