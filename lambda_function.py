import json

import logging

import boto3
import botocore

logging.getLogger().setLevel(logging.INFO)

BUCKET_NAME = 'dev-days-test'
KEY = 'hello.txt'

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    
    logging.info(event)
    # TODO implement
  
    try:
        temp_file = "/tmp/hello_local.txt"
        s3.Bucket(BUCKET_NAME).download_file(KEY, temp_file)
        file= open(temp_file, "r")
        return {
          'statusCode': 200,
          'body': file.read()
        }
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            logging.error("The object does not exist,")
        else:
             raise
  