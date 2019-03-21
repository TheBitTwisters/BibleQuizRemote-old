from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=15, blank=False)

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
