from django.db import models


class Current(models.Model):
    name = models.CharField(max_length=30, blank=False)
    value = models.CharField(max_length=30, blank=False)

    @classmethod
    def get_value(cls, name):
        sql = 'SELECT * FROM current WHERE name = "{0}"'.format(name)
        try:
            current = Current.objects.raw(sql)
        except ObjectDoesNotExist:
            current = None
        return current[0].value if current else ''
