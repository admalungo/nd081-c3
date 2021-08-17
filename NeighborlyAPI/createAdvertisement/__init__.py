import logging
import azure.functions as func
import pymongo
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python createAdvertisement trigger function processed a request.')

    # request = req.get_json()
    request = False

    if request:
        try:
            # url = "mongodb://127.0.0.1:27017"  # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://neighborlycmwestdb:Czf0l4PRQRY1iRieHBar2ARKE1Gx4hbYTH2V4gZFlJfl6uJV3JSe4orR56YTEdhqT56SNeb7FOi70OoMfGczfQ==@neighborlycmwestdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlycmwestdb@"
            # url = os.environ["AzureMongoDBConnString"]
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['ads']

            # rec_id1 = collection.insert_one(eval(request))
            rec_id1 = None

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )