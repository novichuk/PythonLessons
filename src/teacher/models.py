from django.db import models
from faker import Faker
import random

class Teacher(models.Model):
    DISTINGUISHED = 'Distinguished'
    PROFESSOR = 'professor'
    ASSOCIATE_PROFESSOR = 'Associate Professor'
    ASSISTANT_PROFESSOR = 'Assistant Professor'
    MASTER_INSTRUCTOR = 'Master Instructor'
    SENIOR_INSTRUCTOR = 'Senior Instructor'
    INSTRUCTOR = 'Instructor'
    RESEARCH_ASSOCIATE = 'Research Associate'
    LECTURER = 'Lecturer'

    TEACHERS_RANKS = [
        (DISTINGUISHED, 'Distinguished'),
        (PROFESSOR, 'Professor'),
        (ASSOCIATE_PROFESSOR, 'Associate Professor'),
        (ASSISTANT_PROFESSOR, 'Assistant Professor'),
        (MASTER_INSTRUCTOR, 'Master Instructor'),
        (SENIOR_INSTRUCTOR, 'Senior Instructor'),
        (INSTRUCTOR, 'Instructor'),
        (RESEARCH_ASSOCIATE, 'Research Associate'),
        (LECTURER, 'Lecturer'),
    ]

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    rank = models.CharField(max_length=32, choices=TEACHERS_RANKS, default='LECTURER')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def info(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.age} {self.rank}'

