from django.db import models


class Group(models.Model):
    course = models.CharField(max_length=64)
    created_group_at = models.DateTimeField(auto_now_add=True)

    @property
    def info(self) -> str:
        return f'{self.course} {self.created_group_at}'
