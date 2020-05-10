from django.db import models


# Create your models here.

# ORM
# Объектное представление в Джанго = модель
# Модель - отображение реляционной таблицы

class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()  # +,-.-127..+127 #Integer.Field

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def info(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.age}'

    def inc_age(self):
        self.age += 1
        self.save()

