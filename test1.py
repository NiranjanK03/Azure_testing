#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install azure-storage-blob
# !pip install xlrd


# In[2]:


# !pip install --upgrade pip --user


# In[3]:


# !pip uninstall azure


# In[4]:


# !pip uninstall azure-storage-file-share


# In[5]:


# !pip install azure-storage-file-share --pre --user


# In[6]:


# !pip freeze > requirements.txt


# In[7]:


# !cat requirements.txt


# In[8]:


import os, uuid
from io import StringIO
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
# from azure.identity import DefaultAzureCredential


# In[44]:


connection_string  = 'DefaultEndpointsProtocol=https;AccountName=graybardata;AccountKey=V+zUSJhOAVNU62mk55jRtwWNucjJ7ndkLvMGg/t0sLPEr0P4w9y3GphpXJ/2O56jIyfwHa2o7e8PtAI0MRyCCw==;EndpointSuffix=core.windows.net'
account_name = 'graybardata'
account_key = 'V+zUSJhOAVNU62mk55jRtwWNucjJ7ndkLvMGg/t0sLPEr0P4w9y3GphpXJ/2O56jIyfwHa2o7e8PtAI0MRyCCw=='
container_name = 'csvfiles'
blob_name = 'Schneider_one_to_many.xlsx'
from azure.storage.blob import ContainerClient

container = ContainerClient.from_connection_string(conn_str=connection_string, container_name="csvfiles")

blob_list = container.list_blobs()
for blob in blob_list:
    print(blob.name + '\n')


# In[10]:


from azure.storage.blob import BlobClient

blob = BlobClient.from_connection_string(conn_str=connection_string, container_name="csvfiles", blob_name="Schneider_one_to_many.xlsx")

with open("./Schneider_one_to_many.xlsx", "wb") as my_blob:
    blob_data = blob.download_blob()
    blob_data.readinto(my_blob)
# import pandas as pd
# df = pd.read_excel('Schneider_one_to_many.xlsx')
# df


# In[50]:


from azure.storage.blob import generate_blob_sas, AccountSasPermissions

# def scan_product():
url = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}"
sas_token = generate_blob_sas(
    account_name=account_name,
    account_key=account_key,
    container_name=container_name,
    blob_name=blob_name,
    permission=AccountSasPermissions(read=True),
    expiry=datetime.utcnow() + timedelta(hours=1)
)

url_with_sas = f"{url}?{sas_token}"
print(url_with_sas)


# In[43]:


# from azure.storage.fileshare import generate_account_sas, ResourceTypes, AccountSasPermissions
# sas_token = generate_account_sas(
#     account_name,
#     access_key,
#     resource_types=ResourceTypes(service=True),
#     permission=AccountSasPermissions(read=True),
#     expiry=datetime.utcnow() + timedelta(hours=1)
# )
# print(sas_token)
# sas_url = 'https://graybardata.blob.core.windows.net/csvfiles/Schneider_one_to_many.xlsx?' + sas_token


# In[51]:


import pandas as pd 
print(source)
df = pd.read_excel(url_with_sas)
print(df.head())


# In[ ]:


df.to_csv('test.csv', index = False)


# In[ ]:


blob_service_client = BlobServiceClient.from_connection_string('DefaultEndpointsProtocol=https;AccountName=graybardata;AccountKey=V+zUSJhOAVNU62mk55jRtwWNucjJ7ndkLvMGg/t0sLPEr0P4w9y3GphpXJ/2O56jIyfwHa2o7e8PtAI0MRyCCw==;EndpointSuffix=core.windows.net')
blob_client = blob_service_client.get_blob_client(container='test', blob='test.csv')
with open('test.csv', "rb") as data:
    blob_client.upload_blob(data)


# In[ ]:




