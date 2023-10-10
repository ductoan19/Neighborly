import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import os


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            url = os.environ["MONGO_DB"]
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['posts']

            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass post detail in the body', status_code=400)
