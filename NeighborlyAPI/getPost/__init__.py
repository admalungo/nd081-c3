import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPost trigger function processed a request.')

    id = req.params.get('id')

    if id:
        try:
            # url = "mongodb://127.0.0.1:27017"  # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://neighborlycmwestdb:Ig5RtWMeUa9cCIc2h6uxJeg4BFySAT2CLAaFuf1kWihivWSNPLFqxabv9FxOVH1CcXv2eLu9MHl6LJHCs4p6Jw==@neighborlycmwestdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlycmwestdb@"
            # url = os.environ["AzureMongoDBConnString"]
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['posts']

            # query = {'_id': ObjectId(id)}
            # result = collection.find_one(query)
            result = collection.find_one(id)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)