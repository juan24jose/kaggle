import boto3
import os

#instiantiate a client

client = boto3.client('s3')

#retrieve all bucket Metadad
response = client.list_buckets()

#loop through bucket data and display bucket names
for b in response['Buckets']:
    print(b['Name'])

print(os.getcwd())