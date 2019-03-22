from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Group(models.Model):

    @classmethod
    def get(cls, name):
        sql = 'SELECT * FROM `groups` WHERE name = "{0}"'.format(name)
        try:
            group = Group.objects.raw(sql)
        except ObjectDoesNotExist:
            group = None
        if group:
            return {
                'id': group[0].id,
                'name': group[0].name
            }
        return False
