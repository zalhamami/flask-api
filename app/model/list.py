import json

class ListMeta:
  def __init__(self, PageSize, PagePosition, TotalPage, TotalData):
    self.PageSize = PageSize
    self.PagePosition = PagePosition
    self.TotalPage = TotalPage
    self.TotalData = TotalData

  def toJSON(self):
    data = json.dumps(self.__dict__)
    return eval(data)


class ListResponse:
  def __init__(self, Data, Meta = None):
    self.Data = Data
    if (Meta is not None):
      self.Meta = Meta

  def toJSON(self):
    data = json.dumps(self.__dict__)
    return json.loads(data)
    