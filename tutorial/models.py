from django.contrib.gis.db import models


class Marker(models.Model):
    location = models.PointField()
    name = models.CharField(max_length=255, null=True)
    list_of_choices = (('mw', 'men work'),  # дорожные работы
                       ('cr', 'crash'),  # Авария
                       ('cm', 'comment'),  # Комментарий
                       ('tc', 'temporary camera'),  # Временная камера
                       ('pc', 'pernament camers'),  # Постоянная камера
                       )
    marker_type = models.CharField(max_length=255, choices=list_of_choices, null=True)

    # ty = models.CharField(max_length=125)
    def __str__(self):
        return self.name
