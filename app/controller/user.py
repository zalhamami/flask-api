
from flask_restful import Resource, reqparse

from app.service.user import UserService

from app.helper.error_handler import ErrorHandler
from app.helper.request_params import RequestParams
from app.helper.response import Response

class User(Resource):
  # Initialize request parser
  parser = reqparse.RequestParser(bundle_errors=True)
  parser.add_argument('Username', type=str, required=True)


class UserList(Resource):
  def get(self):
    # get meta data
    meta = RequestParams.pagination()

    # get data from repository by service
    users = UserService.getAllData(
      page_position = meta['PagePosition'],
      page_size = meta['PageSize']
    )
    
    # data serialization
    data = UserService.serialization(users['Data'], many=True)

    # json response
    response = Response.json(data, users['Meta'])
    return response, 200