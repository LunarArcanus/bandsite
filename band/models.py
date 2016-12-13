from __future__ import unicode_literals

from django.db import models

class BandInfo(models.Model):
    name = models.CharField(max_length=200)
    est_date = models.DateTimeField("date established")
    pub_date = models.DateTimeField("date published")
    members = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name

class BandVote(models.Model):
    info = models.ForeignKey(BandInfo)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name
