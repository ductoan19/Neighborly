import azure.functions as func
import pymongo
import json
import os


def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = os.environ["MONGO_DB"]
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['advertisements']
            collection.insert_one(json.loads(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )
