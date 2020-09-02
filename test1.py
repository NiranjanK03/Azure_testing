#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip install azure-storage-blob
# !pip install xlrd


# In[ ]:


# !pip install --upgrade pip --user


# In[ ]:


# !pip uninstall azure


# In[ ]:


# !pip uninstall azure-storage-file-share


# In[ ]:


# !pip install azure-storage-file-share --pre --user


# In[ ]:


# !pip freeze > requirements.txt


# In[ ]:


# !cat requirements.txt


# In[ ]:


import os, uuid
from io import StringIO
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
# from azure.identity import DefaultAzureCredential


# In[ ]:


connection_string  = 'DefaultEndpointsProtocol=https;AccountName=graybardata;AccountKey=V+zUSJhOAVNU62mk55jRtwWNucjJ7ndkLvMGg/t0sLPEr0P4w9y3GphpXJ/2O56jIyfwHa2o7e8PtAI0MRyCCw==;EndpointSuffix=core.windows.net'
account_name = 'graybardata'
access_key = 'V+zUSJhOAVNU62mk55jRtwWNucjJ7ndkLvMGg/t0sLPEr0P4w9y3GphpXJ/2O56jIyfwHa2o7e8PtAI0MRyCCw=='
from azure.storage.blob import ContainerClient

container = ContainerClient.from_connection_string(conn_str=connection_string, container_name="csvfiles")

blob_list = container.list_blobs()
for blob in blob_list:
    print(blob.name + '\n')


# In[ ]:


from azure.storage.blob import BlobClient

blob = BlobClient.from_connection_string(conn_str=connection_string, container_name="csvfiles", blob_name="Schneider_one_to_many.xlsx")

with open("./Schneider_one_to_many.xlsx", "wb") as my_blob:
    blob_data = blob.download_blob()
    blob_data.readinto(my_blob)
# import pandas as pd
# df = pd.read_excel('Schneider_one_to_many.xlsx')
# df


# In[ ]:


import azure.storage.fileshare
from azure.storage.fileshare import ShareServiceClient
share_service_client = ShareServiceClient.from_connection_string(self.connection_string)

# Create a SAS token to use to authenticate a new client
from azure.storage.fileshare import generate_account_sas, ResourceTypes, AccountSasPermissions

sas_token = generate_account_sas(
    self.account_name,
    self.access_key,
    resource_types=ResourceTypes(service=True),
    permission=AccountSasPermissions(read=True),
    expiry=datetime.utcnow() + timedelta(hours=1)
)


# In[ ]:


import pandas as pd 
source = str(sas_token)
df = pd.read_excel(source)
print(df.head())


# In[ ]:


df.to_csv('test.csv', index = False)


# In[ ]:


blob_service_client = BlobServiceClient.from_connection_string('DefaultEndpointsProtocol=https;AccountName=graybardata;AccountKey=V+zUSJhOAVNU62mk55jRtwWNucjJ7ndkLvMGg/t0sLPEr0P4w9y3GphpXJ/2O56jIyfwHa2o7e8PtAI0MRyCCw==;EndpointSuffix=core.windows.net')
blob_client = blob_service_client.get_blob_client(container='test', blob='test.csv')
with open('test.csv', "rb") as data:
    blob_client.upload_blob(data)


# In[ ]:




