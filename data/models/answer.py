from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Answer(models.Model):

    @classmethod
    def get(cls, question_id, group_id):
        sql = 'SELECT * FROM answers WHERE question = {0} AND `group` = {1}'.format(question_id, group_id)
        try:
            answer = Answer.objects.raw(sql)
        except ObjectDoesNotExist:
            answer = None
        return answer[0].answer if answer else ''
