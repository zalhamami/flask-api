
from flask_restful import Resource, reqparse

from app.service.type import TypeService

from app.helper.error_handler import ErrorHandler
from app.helper.request_params import RequestParams
from app.helper.response import Response

class Type(Resource):
  # Initialize request parser
  parser = reqparse.RequestParser(bundle_errors=True)
  parser.add_argument('Name', type=str, required=True)
  
  @classmethod
  def getDataById(cls, id):
    # get data from repository
    data = TypeService.getDataById(id)

    # check data
    if data is None:
      ErrorHandler.itemNotFound(id, 'type')

    return data

  def get(self, id):
    # get data
    type = self.getDataById(id)

    # data serialization
    data = TypeService.serialization(type)
    return data, 200

  def put(self, id):
    # check data
    type = self.getDataById(id)

    # get payload
    payload = self.parser.parse_args()

    # update data
    TypeService.updateData(type, payload)

    # json response
    response = TypeService.serialization(type)
    return response, 200


class TypeList(Resource):
  def get(self):
    # get meta data
    meta = RequestParams.pagination()

    # get data from repository by service
    types = TypeService.getAllData(
      page_position = meta['PagePosition'],
      page_size = meta['PageSize']
    )
    
    # data serialization
    data = TypeService.serialization(types['Data'], many=True)

    # json response
    response = Response.json(data, types['Meta'])
    return response, 200

  def post(self):
    # get payload
    payload = Type.parser.parse_args()

    # insert data
    type = TypeService.insertData(payload)

    # data serialization
    data = TypeService.serialization(type)
    return data, 200
    