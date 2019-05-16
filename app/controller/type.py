import json

from flask_restful import Resource, reqparse

from app.helper.error_handler import ErrorHandler

from app.model.list import ListResponse

from app.repository.type import TypeRepository

from app.schema.type import TypeSchema

class Type(Resource):
  # Initialize request parser in this controller
  parser = reqparse.RequestParser(bundle_errors=True)
  parser.add_argument('Name', type=str, required=True)
  
  def get(self, id):
    # get data from repository
    item = TypeRepository.getById(id)

    # chek data
    if item is None:
      ErrorHandler.itemNotFound(id, 'type')

    # json response
    response = TypeSchema().dumps(item).data
    response = json.loads(response)
    
    return response, 200


class TypeList(Resource):
  def get(self):
    # get data from repository
    items = TypeRepository.getAll()

    # data serialization
    data = TypeSchema(many=True).dumps(items).data
    data = json.loads(data)
    
    # json response
    response = ListResponse(
      Data = data
    ).toJSON()

    return response, 200
    

    