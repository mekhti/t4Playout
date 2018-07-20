from django.db import models

class Instances(models.Model):
    channelId = models.UUIDField
    channelName = models.TextField()

    def __str__(self):
        return "%s" % (self.channelId)