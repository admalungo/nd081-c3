import logging
import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python createAd function processed a request.')

    # request = req.get_json()
    request = False

    if request:

        logging.info(request)
        logging.info(req.get_body())

        try:
            # url = "mongodb://127.0.0.1:27017"  # TODO: Update with appropriate MongoDB connection information
            # url = "mongodb://neighborlycmwestdb:TCriehv6QJp4e5PNLwmyeEBYbfzMd39K3xyqIkPiwuoUSV6I4NCjEEITLJytFZFQ4B4RCgn8ANDHeyiCwpYB9A==@neighborlycmwestdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlycmwestdb@"
            url = os.environ["AzureMongoDBConnString"]
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['ads']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())
        
        except ValueError:

            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
