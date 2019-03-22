from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Current(models.Model):

    @classmethod
    def get_value(cls, name, default_value):
        sql = 'SELECT * FROM current WHERE name = "{0}"'.format(name)
        try:
            current = Current.objects.raw(sql)
        except ObjectDoesNotExist:
            current = None
        return current[0].value if current else default_value
