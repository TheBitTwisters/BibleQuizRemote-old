from django.db import connections, models, IntegrityError
from django.core.exceptions import ObjectDoesNotExist


class Answer(models.Model):

    @classmethod
    def get(cls, question_id, group_id):
        sql = 'SELECT * FROM `answers` WHERE `question` = {0} AND `group` = {1}'.format(question_id, group_id)
        try:
            answer = Answer.objects.raw(sql)
        except ObjectDoesNotExist:
            answer = None
        return answer[0].answer if answer else None

    @classmethod
    def set(cls, question_id, group_id, answer):
        saved_answer = Answer.get(question_id, group_id)
        sql = 'INSERT INTO `answers` (`question`, `group`, `answer`) VALUES ({0},{1},"{2}")'.format(question_id, group_id, answer)
        if saved_answer:
            sql = 'UPDATE `answers` SET `answer`="{2}" WHERE `question`={0} AND `group`={1}'.format(question_id, group_id, answer)
        with connections['default'].cursor() as cursor:
            cursor.execute(sql)
