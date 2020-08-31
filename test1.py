#!/usr/bin/env python
# coding: utf-8

# In[33]:


get_ipython().system('pip3 install azure-storage-blob')
get_ipython().system('pip install xlrd')


# In[8]:


get_ipython().system('pip install azure-storage-file')


# In[22]:


import os, uuid
from io import StringIO
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
# from azure.identity import DefaultAzureCredential


# In[16]:


get_ipython().system('pip freeze')


# In[ ]:


# from azure.storage.blob import BlobServiceClient

# service = BlobServiceClient(account_url="DefaultEndpointsProtocol=https;AccountName=graybardata;AccountKey=hOOZv/LxplEi8W5FIaPgF8mSajjIDFHvYViXfS04Msje7NRUmDYB4xY76yqFOYGIBOACl+dGF+fidaFgwAmX2w==;EndpointSuffix=core.windows.net", credential=credential)


# In[ ]:


# block_blob_service = BlockBlobService(account_name='meetpythonstorage', account_key='duOguiKnYb6ZEbJC6BftWqA2lcH67dWkmCSEJj+KxOTOHCNPeV7r4oO6feTw7gSSoFGKHryL4yqSVWlEkm6jWg==')


# In[ ]:


# blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
# container_client = blob_service_client.get_container_client("graybardata")


# In[17]:


connection_string  = 'DefaultEndpointsProtocol=https;AccountName=graybardata;AccountKey=V+zUSJhOAVNU62mk55jRtwWNucjJ7ndkLvMGg/t0sLPEr0P4w9y3GphpXJ/2O56jIyfwHa2o7e8PtAI0MRyCCw==;EndpointSuffix=core.windows.net'
from azure.storage.blob import ContainerClient

container = ContainerClient.from_connection_string(conn_str=connection_string, container_name="csvfiles")

blob_list = container.list_blobs()
for blob in blob_list:
    print(blob.name + '\n')


# In[18]:


block_blob_service = BlobServiceClient(account_url='https://graybardata.blob.core.windows.net/csvfiles')

blob = block_blob_service.get_blob_as_bytes('csvfiles', 'Schneider_one_to_many.xlsx')
print(blob.content)


# In[34]:


from azure.storage.blob import BlobClient

blob = BlobClient.from_connection_string(conn_str=connection_string, container_name="csvfiles", blob_name="Schneider_one_to_many.xlsx")

with open("./Schneider_one_to_many.xlsx", "wb") as my_blob:
    blob_data = blob.download_blob()
    blob_data.readinto(my_blob)
import pandas as pd
df = pd.read_excel('Schneider_one_to_many.xlsx')
df


# In[38]:


import pandas as pd 
source = 'https://graybardata.blob.core.windows.net/csvfiles/Schneider_one_to_many.xlsx?sp=r&st=2020-08-30T17:20:23Z&se=2020-08-31T01:20:23Z&spr=https&sv=2019-12-12&sr=b&sig=st2XbS7v8rSA39eddxD7Ng61%2BUdvs%2Bp5kHZDsw%2BicTI%3D'
df = pd.read_excel(source)
print(df.head())


# In[40]:


df.to_csv('test.csv', index = False)


# In[41]:


blob_service_client = BlobServiceClient.from_connection_string('DefaultEndpointsProtocol=https;AccountName=graybardata;AccountKey=V+zUSJhOAVNU62mk55jRtwWNucjJ7ndkLvMGg/t0sLPEr0P4w9y3GphpXJ/2O56jIyfwHa2o7e8PtAI0MRyCCw==;EndpointSuffix=core.windows.net')
blob_client = blob_service_client.get_blob_client(container='test', blob='test.csv')
with open('test.csv', "rb") as data:
    blob_client.upload_blob(data)


# In[ ]:




