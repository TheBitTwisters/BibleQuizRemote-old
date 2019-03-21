from django.db import models


class Question(models.Model):
    sequence = models.IntegerField()
    question_statement = models.CharField(max_length=30, blank=False)
    choices_layout = models.CharField(max_length=3, blank=False)

    @classmethod
    def get(cls, id):
        sql = 'SELECT * FROM questions WHERE id = {0}'.format(id)
        try:
            question = Question.objects.raw(sql)
        except ObjectDoesNotExist:
            question = None
        if question:
            return {
                'id': question[0].id,
                'sequence': question[0].sequence,
                'question_statement': question[0].question_statement,
                'choices_layout': question[0].choices_layout
            }
        return False
