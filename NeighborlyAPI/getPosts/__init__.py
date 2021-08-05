import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        # url = "mongodb://127.0.0.1:27017"  # TODO: Update with appropriate MongoDB connection information
        # url = "mongodb://neighborlycmwestdb:TCriehv6QJp4e5PNLwmyeEBYbfzMd39K3xyqIkPiwuoUSV6I4NCjEEITLJytFZFQ4B4RCgn8ANDHeyiCwpYB9A==@neighborlycmwestdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlycmwestdb@"
        url = os.environ["AzureMongoDBConnString"]
        client = pymongo.MongoClient(url)
        database = client['azure']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)