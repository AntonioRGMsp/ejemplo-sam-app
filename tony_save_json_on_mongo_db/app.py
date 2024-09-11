import os
import json
import boto3
import pymongo
from pymongo import MongoClient

s3 = boto3.client('s3')

cluster = MongoClient(host=os.environ.get('ATLAS_URI'))
db_test = cluster[os.environ.get('DB_TEST')]
my_collection = db_test[os.environ.get('MY_COLLECTION')]

def get_json_data_from_s3(keyObject, bucketName):
    get_obj_response = s3.get_object(
        Bucket= bucketName,
        Key= keyObject
    )
    return json.loads(get_obj_response.get('Body').read())

def upload_json_data_to_db(jsonData):
    filter = {"id": jsonData["id"]}
    update = { "$set": jsonData}
    response_db = my_collection.update_one(
        filter,
        update,
        upsert=True
    )
    print(response_db)
    

def lambda_handler(event, context):
    try:
        print("Message received: ", json.dumps(event))
        records = event['Records']
        total_records = len(records)
        print('Records received: ', str(total_records))

        for record in records:
            body = json.loads(record['body'])
            if 'Records' in body:
                for event_info in body['Records']:
                    bucket_name = event_info['s3']['bucket']['name']
                    key_object = event_info['s3']['object']['key']

                    if(bucket_name and key_object):
                        json_data = get_json_data_from_s3(key_object, bucket_name)
                        upload_json_data_to_db(json_data)
                        print("Successfuly!!!")
            else:
                print("No Records key in the body of the message")
    except Exception as e:
        print(e)
        raise


    