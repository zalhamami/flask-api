from flask import jsonify
from flask_restful import abort

class ErrorHandler:
  code = {
    'bad-request': 400,
    'unauthorized': 401,
    'not-found': 404,
    'conflict': 409,
    'server-error': 500
  }
  
  @classmethod
  def badRequest(cls):
    abort(
      cls.code['bad-request'],
      code = cls.code['bad-request'],
      message = 'bad request',
    )

  @classmethod
  def itemNotFound(cls, id, data = 'item'):
    abort(
      cls.code['not-found'],
      code = cls.code['not-found'],
      data = data,
      message = "{0} with id '{1}' is doesn't exists.".format(data, id)
    )

  @classmethod
  def itemExists(cls, name, data = 'item'):
    abort(
      cls.code['conflict'],
      code = cls.code['conflict'],
      data = data,
      message = "{0} with name '{1}' is already exists.".format(name, id)
    )

  @classmethod
  def insertError(cls, data = 'item'):
    abort(
      cls.code['server-error'],
      code = cls.code['server-error'],
      message = 'An error ocurred when inserting the {0}.'.format(data)
    )

  @classmethod
  def updateError(cls, data = 'item'):
    abort(
      cls.code['server-error'],
      code = cls.code['server-error'],
      message = 'An error ocurred when inserting the {0}.'.format(data)
    )

  @classmethod
  def deleteError(cls, data = 'item'):
    abort(
      cls.code['server-error'],
      code = cls.code['server-error'],
      message = 'An error ocurred when deleting the {0}.'.format(data)
    )

  @classmethod
  def unauthorized(cls):
    abort(
      cls.code['unauthorized'],
      code = cls.code['unauthorized'],
      message = 'unauthorized client',
    )

  @classmethod
  def notEligible(cls):
    abort(
      cls.code['unauthorized'],
      code = cls.code['unauthorized'],
      message = 'not eligible',
    )

  @classmethod
  def hasRelation(cls):
    abort(
      cls.code['bad-request'],
      code = cls.code['bad-request'],
      message = "entity has relation"
    )

  @classmethod
  def reviewConflict(cls, userId):
    abort(
      cls.code['conflict'],
      code = cls.code['conflict'],
      message = "user with id '{0}' cannot write a review in this job again.".format(userId)
    )

  @classmethod
  def applicantsJobConflict(cls, userId):
    abort(
      cls.code['conflict'],
      code = cls.code['conflict'],
      message = "user with id '{0}' cannot apply in this job again.".format(userId)
    )
