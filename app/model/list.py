class ListMeta:
  def __init__(self, PageSize, PagePosition, TotalPage, TotalData):
    self.PageSize = PageSize
    self.PagePosition = PagePosition
    self.TotalPage = TotalPage
    self.TotalData = TotalData

  def toJSON(self):
    return dict(self.__dict__)


class ListResponse:
  def __init__(self, Data, Meta=None):
    self.Data = Data
    if Meta is not None:
      self.Meta = Meta

  def toJSON(self):
    return dict(self.__dict__)
