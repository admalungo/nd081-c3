import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getAdvertisements trigger function processed a request.')

    try:
        # url = "mongodb://127.0.0.1:27017"  # TODO: Update with appropriate MongoDB connection information
        url = "mongodb://neighborlycmwestdb:Czf0l4PRQRY1iRieHBar2ARKE1Gx4hbYTH2V4gZFlJfl6uJV3JSe4orR56YTEdhqT56SNeb7FOi70OoMfGczfQ==@neighborlycmwestdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlycmwestdb@"
        # url = os.environ["AzureMongoDBConnString"]
        client = pymongo.MongoClient(url)
        database = client['azure']
        collection = database['ads']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

