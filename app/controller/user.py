
from werkzeug.security import safe_str_cmp
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required

from app.service.user import UserService

from app.helper.error_handler import ErrorHandler
from app.helper.request_params import RequestParams
from app.helper.response import Response

class User(Resource):
  # Initialize request parser
  parser = reqparse.RequestParser(bundle_errors=True)
  parser.add_argument('username', type=str, required=True)
  parser.add_argument('password', type=str, required=True)


class UserList(Resource):
  @jwt_required
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


class UserLogin(Resource):
  def post(self):
    # get payload
    payload = User.parser.parse_args()

    # check user
    user = UserService.getDataByUsername(payload['username'])
    if user and safe_str_cmp(user.password, payload['password']):
      access_token = create_access_token(identity=user.id, fresh=True)
      refresh_token = create_refresh_token(user.id)
      return {
        'access_token': access_token,
        'refresh_token': refresh_token
      }, 200

    return {'message': 'invalid credentials'}, 401
