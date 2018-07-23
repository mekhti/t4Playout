from django.db import models
from enum import Enum
import uuid

import Playout.Models.ccgEnums as CCGEnums

from Playout.Models.instances import Instances

class Servers(models.Model):
    serverID = models.UUIDField
    serverName = models.TextField()
    serverChannelID = models.ForeignKey('Instances', on_delete=models.CASCADE)
    serverAddress = models.GenericIPAddressField()
    serverPort = models.PositiveIntegerField()
    serverSettings = models.ForeignKey('ServerSettings', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.serverID)

class MixerSettings(models.Model):
    mixerSettingsID = models.UUIDField
    serverID = models.ForeignKey('Servers', on_delete=models.CASCADE)
    blendModes = models.BooleanField(
        default="false"
    )
    mipmappingDefaultOn = models.BooleanField(
        default="false"
    )
    straightAlpha = models.BooleanField(
        default="false"
    )

    def __str__(self):
        return "%s" % (self.mixerSettingsID)

class TemplateHost(models.Model):
    templateHostID = models.UUIDField
    ttt = models.CharField(
        max_length=20,
        choices=CCGEnums.LoggingLevels.Choices,
        default=CCGEnums.LoggingLevels.INFO
    )

    def __str__(self):
        return "%s" % (self.templateHostID)

class ThumbnailsSettings(models.Model):
    settingsID = models.UUIDField
    generateThumbnails = models.BooleanField(
        default="false"
    )
    thumbWidt = models.PositiveSmallIntegerField
    thumbHeight = models.PositiveSmallIntegerField
    thumbVideoGrid = models.PositiveSmallIntegerField
    thumbScanInterval = models.PositiveIntegerField
    thumbGenerateDelayMillis = models.PositiveIntegerField
    thumbVideoMode = models.CharField(
        max_length=20,
        choices=[(tag, tag.value) for tag in CCGEnums.VIdeoMode.Choices],
        default=CCGEnums.VIdeoMode.VM_PAL
    )
    thumbMipMap = models.BooleanField(
        default="true"
    )

    def __str__(self):
        return "%s" %s (self.settingsID)

class Consumer(models.Model):
    consumerID = models.UUIDField
    serverID = models.ForeignKey("Servers", on_delete=models.CASCADE)
    consumerVideoMode = models.CharField(
        max_length=20,
        choices=[(tag, tag.value) for tag in CCGEnums.VIdeoMode],
        default=CCGEnums.VIdeoMode.VM_PAL
    )
    straightAlphaOutput = models.BooleanField(
        default="false"
    )
    audioChannelLayout = models.CharField(
        max_length=20,
        choices=[(tag, tag.value) for tag in CCGEnums.AudioChannelsLayout],
        default=CCGEnums.AudioChannelsLayout.STRO
    )

    def __str__(self):
        return "%s" % (self.consumerID)

class ServerSettings(models.Model):
    settingsID = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    serverID = models.ForeignKey('Servers', on_delete=models.CASCADE)
    logLevel = models.CharField(
        max_length=15,
        choices=[(tag, tag.value) for tag in CCGEnums.LoggingLevels],
        default= CCGEnums.LoggingLevels.INFO
    )
    logCategories = models.CharField(
        max_length=22,
        choices=[(tag, tag.value) for tag in CCGEnums.LogCategories],
        default= CCGEnums.LogCategories.COMM
    )
    forceDeinterlace = models.BooleanField(
        default="false"
    )
    channelGrid = models.BooleanField(
        default="false"
    )
    mixer = models.ForeignKey('MixerSettings', on_delete=models.CASCADE)
    accelerator = models.CharField(
        max_length=15,
        choices=[(tag, tag.value) for tag in CCGEnums.Accelerator],
        default= CCGEnums.Accelerator.AUTO
    )
    templateHost = models.ForeignKey('TemplateHost', on_delete=models.CASCADE)
    flashBufferDepth = models.CharField(
        max_length=10,
        default="auto"
    )
    htmlRemoteDebuggingPort = models.PositiveIntegerField()
    tumbnailsSettings = models.ForeignKey('ThumbnailsSettings', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.settingsID)
