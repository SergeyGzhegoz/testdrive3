from django.db import models


class Drive(models.Model):
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Телефон', max_length=50)
    email = models.CharField('Почта', max_length=50)
    auto = models.CharField('Машина', max_length=50)
    comment = models.TextField('Комментарий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Car(models.Model):
    marka = models.CharField('Марка', max_length=50)
    model = models.CharField('Модель', max_length=50)

    def __str__(self):
        return self.marka

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
