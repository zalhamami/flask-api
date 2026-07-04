from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.repository.type import TypeRepository
from app.helper.error_handler import ErrorHandler
from app.schema.type import TypeSchema


class TypeService:
  @classmethod
  def getAllData(cls, page_position, page_size, filter=None):
    return TypeRepository.getAll(
      page_position=page_position,
      page_size=page_size,
      filter=filter
    )

  @classmethod
  def getDataById(cls, id):
    return TypeRepository.getById(id)

  @classmethod
  def insertData(cls, payload):
    data = TypeRepository(name=payload['name'])
    try:
      data.save()
    except SQLAlchemyError:
      db.session.rollback()
      ErrorHandler.insertError('type')
    return data

  @classmethod
  def updateData(cls, data, payload):
    try:
      data.name = payload['name']
      db.session.commit()
    except SQLAlchemyError:
      db.session.rollback()
      ErrorHandler.updateError('type')
    return data

  @classmethod
  def serialization(cls, data, many=False):
    return TypeSchema(many=many).dump(data)
