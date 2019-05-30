import json

from app import db  
from app.repository.type import TypeRepository
from app.helper.error_handler import ErrorHandler
from app.schema.type import TypeSchema

class TypeService:
  @classmethod
  def getAllData(cls, page_position, page_size, filter = None):
    # get data from repository
    data = TypeRepository.getAll(
      page_position = page_position,
      page_size = page_size,
      filter = filter
    )
    return data

  @classmethod
  def getDataById(cls, id):
    # get data from repository
    data = TypeRepository.getById(id)
    return data

  @classmethod
  def insertData(cls, payload):
    data = TypeRepository(
      name = payload['Name']
    )
    try:
      data.save()
    except:
      ErrorHandler.insertError('type')
    return data
    
  @classmethod
  def updateData(cls, data, payload):
    try:
      data.name = payload['Name']
      db.session.commit()
    except:
      ErrorHandler.updateError('type')
    return 'ok'

  @classmethod
  def serialization(cls, data, many = False):
    result = TypeSchema(many=many).dumps(data).data
    result = json.loads(result)
    return result