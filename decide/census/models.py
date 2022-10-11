from sys import maxsize
from django.db import models


class Census(models.Model):
    voting_id = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()
    adscription = models.CharField(max_length= 30)
    class Meta:
        unique_together = (('voting_id', 'voter_id','adscription'),)
