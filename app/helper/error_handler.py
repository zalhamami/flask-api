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
  def badRequest(cls, message='bad request'):
    abort(
      cls.code['bad-request'],
      code=cls.code['bad-request'],
      message=message,
    )

  @classmethod
  def validationError(cls, errors):
    abort(
      cls.code['bad-request'],
      code=cls.code['bad-request'],
      message='validation failed',
      errors=errors,
    )

  @classmethod
  def itemNotFound(cls, id, data='item'):
    abort(
      cls.code['not-found'],
      code=cls.code['not-found'],
      data=data,
      message="{0} with id '{1}' does not exist.".format(data, id)
    )

  @classmethod
  def itemExists(cls, name, data='item'):
    abort(
      cls.code['conflict'],
      code=cls.code['conflict'],
      data=data,
      message="{0} with name '{1}' already exists.".format(data, name)
    )

  @classmethod
  def insertError(cls, data='item'):
    abort(
      cls.code['server-error'],
      code=cls.code['server-error'],
      message='An error occurred while inserting the {0}.'.format(data)
    )

  @classmethod
  def updateError(cls, data='item'):
    abort(
      cls.code['server-error'],
      code=cls.code['server-error'],
      message='An error occurred while updating the {0}.'.format(data)
    )

  @classmethod
  def deleteError(cls, data='item'):
    abort(
      cls.code['server-error'],
      code=cls.code['server-error'],
      message='An error occurred while deleting the {0}.'.format(data)
    )

  @classmethod
  def unauthorized(cls):
    abort(
      cls.code['unauthorized'],
      code=cls.code['unauthorized'],
      message='unauthorized client',
    )
