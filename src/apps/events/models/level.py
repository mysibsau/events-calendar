from django.db import models


class Level(models.Model):
    name = models.CharField('Уровень', max_length=32)
    is_inside = models.BooleanField('Внутреннее?', default=False)

    class Meta:
        verbose_name = 'Уровень мероприятия'
        verbose_name_plural = 'Уровни мероприятий'

    def __str__(self):
        return self.name
