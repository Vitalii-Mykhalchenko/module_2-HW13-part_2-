from django import template
from bson.objectid import ObjectId

from .. utils import mongodb

register = template.Library()


def get_author(id_):
    db = mongodb()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    if author:
        return author["fullname"]
    return ""


register.filter('get_author', get_author)
