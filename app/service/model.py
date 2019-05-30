from math import floor

from app.model import db
from app.model.list import ListMeta

class ModelService:
  @classmethod
  def getAllData(cls, model, page_position, page_size, filter = None, query = None):
    if query is None:
      query = model.query
      
    query = cls.queryFilter(model, query, filter)

    total_data = query.count()
    total_page = cls.getTotalPage(total_data, page_size)

    data = cls.paginateData(query, page_position, page_size)
    meta = ListMeta(
      PageSize = page_size,
      PagePosition = page_position,
      TotalPage = total_page,
      TotalData = total_data
    )
    
    return {
      'Data': data,
      'Meta': meta.toJSON()
    }

  @classmethod
  def queryFilter(cls, model, query, filter = None):
    if filter is not None:
      for attr, value in filter.items():
        if attr == 'keyword':
          query = query.filter(model.name.like('%' + value + '%'))
        else:
          query = query.filter(getattr(model, attr) == value)
    
    try:
      query = query.filter(model.deleted_at == None)
    except:
      pass
      
    return query

  @classmethod
  def paginateData(cls, query, page_position, page_size):
    result = query.paginate(page = page_position, per_page = page_size).items
    return result

  @classmethod
  def getTotalPage(cls, total_data, page_size):
    result = floor(total_data / page_size)
    if total_data % page_size is not 0:
      result += 1
    return result
