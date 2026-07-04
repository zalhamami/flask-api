from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from marshmallow import ValidationError

from app.service.user import UserService

from app.helper.error_handler import ErrorHandler
from app.helper.request_params import RequestParams
from app.helper.response import Response
from app.schema.user import UserCredentialSchema


class UserList(Resource):
  @jwt_required()
  def get(self):
    meta = RequestParams.pagination()
    users = UserService.getAllData(
      page_position=meta['PagePosition'],
      page_size=meta['PageSize']
    )
    data = UserService.serialization(users['Data'], many=True)
    return Response.json(data, users['Meta']), 200

  def post(self):
    payload = _load_credentials()
    user = UserService.insertData(payload)
    return UserService.serialization(user), 201


class UserLogin(Resource):
  def post(self):
    payload = _load_credentials()

    user = UserService.getDataByUsername(payload['username'])
    if user and user.check_password(payload['password']):
      identity = str(user.id)
      return {
        'access_token': create_access_token(identity=identity, fresh=True),
        'refresh_token': create_refresh_token(identity=identity)
      }, 200

    return {'message': 'invalid credentials'}, 401


def _load_credentials():
  try:
    return UserCredentialSchema().load(request.get_json(silent=True) or {})
  except ValidationError as err:
    ErrorHandler.validationError(err.messages)
