from math import ceil

from app.model import db
from app.model.list import ListMeta


class BaseRepository:
  """Shared persistence helpers for model-backed repositories.

  Lives in the repository layer so the data-access concerns no longer depend
  on the service layer (previously ``app/service/model.py``).
  """

  @classmethod
  def getAll(cls, page_position, page_size, filter=None, query=None):
    if query is None:
      query = cls.query

    query = cls.queryFilter(query, filter)

    total_data = query.count()
    total_page = cls.getTotalPage(total_data, page_size)
    data = cls.paginateData(query, page_position, page_size)

    meta = ListMeta(
      PageSize=page_size,
      PagePosition=page_position,
      TotalPage=total_page,
      TotalData=total_data
    )

    return {
      'Data': data,
      'Meta': meta.toJSON()
    }

  @classmethod
  def queryFilter(cls, query, filter=None):
    if filter:
      for attr, value in filter.items():
        if attr == 'keyword' and hasattr(cls, 'name'):
          query = query.filter(cls.name.like('%{0}%'.format(value)))
        else:
          query = query.filter(getattr(cls, attr) == value)

    if hasattr(cls, 'deleted_at'):
      query = query.filter(cls.deleted_at.is_(None))

    return query

  @classmethod
  def paginateData(cls, query, page_position, page_size):
    pagination = query.paginate(
      page=page_position,
      per_page=page_size,
      error_out=False
    )
    return pagination.items

  @staticmethod
  def getTotalPage(total_data, page_size):
    if not page_size:
      return 0
    return ceil(total_data / page_size)

  @classmethod
  def getById(cls, id):
    return cls.query.filter(cls.id == id).first()

  def save(self):
    db.session.add(self)
    db.session.commit()
