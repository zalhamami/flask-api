from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from app.service.type import TypeService

from app.helper.error_handler import ErrorHandler
from app.helper.request_params import RequestParams
from app.helper.response import Response
from app.schema.type import TypeSchema


class Type(Resource):
  @classmethod
  def getDataById(cls, id):
    data = TypeService.getDataById(id)
    if data is None:
      ErrorHandler.itemNotFound(id, 'type')
    return data

  def get(self, id):
    type = self.getDataById(id)
    return TypeService.serialization(type), 200

  def put(self, id):
    type = self.getDataById(id)
    payload = _load_payload(TypeSchema())
    TypeService.updateData(type, payload)
    return TypeService.serialization(type), 200


class TypeList(Resource):
  def get(self):
    meta = RequestParams.pagination()
    types = TypeService.getAllData(
      page_position=meta['PagePosition'],
      page_size=meta['PageSize']
    )
    data = TypeService.serialization(types['Data'], many=True)
    return Response.json(data, types['Meta']), 200

  def post(self):
    payload = _load_payload(TypeSchema())
    type = TypeService.insertData(payload)
    return TypeService.serialization(type), 201


def _load_payload(schema):
  try:
    return schema.load(request.get_json(silent=True) or {})
  except ValidationError as err:
    ErrorHandler.validationError(err.messages)
