from  download_from_azure_data_lake import *

storage_account_name="************"
storage_account_key="***************************"

download_file_from_directory(storage_account_name,storage_account_key,"myfilesystem","folder","data.docx","data.docx")