from django.db import models


class TimestampFields(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        """при добавлении флага abstract = True, класс объявляется как бстрактный. для него не
        будут создаваться таблицы в БД."""
        abstract = True


class Project(TimestampFields):
    """наследники от абстрактного класса будут реальными классами
     пока у них также не будет установлен флаг abstract = True"""
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Measurement(TimestampFields):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
