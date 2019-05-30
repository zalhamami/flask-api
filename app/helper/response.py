from app.model.list import ListResponse

class Response:
  @classmethod
  def json(cls, data, meta = None):
    response = ListResponse(
      Data = data,
      Meta = meta
    ).toJSON()

    return response

