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
            url = "mongodb://neighborlycmwestdb:Czf0l4PRQRY1iRieHBar2ARKE1Gx4hbYTH2V4gZFlJfl6uJV3JSe4orR56YTEdhqT56SNeb7FOi70OoMfGczfQ==@neighborlycmwestdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlycmwestdb@"
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