from flask import request
from flask_restful import reqparse

class RequestParams:
  parser = reqparse.RequestParser(bundle_errors=True)
  parser.add_argument('page_size', type=int, location='args')
  parser.add_argument('page_position', type=int, location='args')
  parser.add_argument('keyword', type=str, location='args')

  @classmethod
  def pagination(cls):
    # Get args
    args = cls.parser.parse_args()
    
    # Initialize meta for pagination
    meta = {
      'PageSize': 25,
      'PagePosition': 1,
    }
    
    # Check if args is not None
    if args['page_size'] is not None:
      meta['PageSize'] = args['page_size']
    if args['page_position'] is not None:
      meta['PagePosition'] = args['page_position']

    return meta