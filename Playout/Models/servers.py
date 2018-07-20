from django.db import models
from enum import Enum

from Playout.Models.instances import Instances

class CCG_LoggingLevels(Enum):
    CCG_LL_TRACE = "trace"
    CCG_LL_DEBUG = "debug"
    CCG_LL_INFO = "info"
    CCG_LL_WARNING = "warning"
    CCG_LL_ERROR = "error"
    CCG_LL_FATAL = "fatal"

class CCG_LogCategories(Enum):
    CCG_LC_COMMUNICATION = "communication"
    CCG_LC_CALLTRACE = "calltrace"
    CCG_LC_TRACE_COMM = "calltrace,communication"

class CCG_Accelerator(Enum):
    CCG_ACC_CPU = "cpu"
    CCG_ACC_GPU = "gpu"
    CCG_ACC_AUTO = "auto"

class CCG_VideoMode(Enum):
    CCG_VM_PAL = "PAL"
    CCG_VM_NTSC = "NTSC"
    CCG_VM_576p2500 = "576p2500"
    CCG_VM_720p2398 = "720p2398"
    CCG_VM_720p2400 = "720p2400"
    CCG_VM_720p2500 = "720p2500"
    CCG_VM_720p5000 = "720p5000"
    CCG_VM_720p2997 = "720p2997"
    CCG_VM_720p5994 = "720p5994"
    CCG_VM_720p3000 = "720p3000"
    CCG_VM_720p6000 = "720p6000"
    CCG_VM_1080p2398 = "1080p2398"
    CCG_VM_1080p2400 = "1080p2400"
    CCG_VM_1080i5000 = "1080i5000"
    CCG_VM_1080i5994 = "1080i5994"
    CCG_VM_1080i6000 = "1080i6000"
    CCG_VM_1080p2500 = "1080p2500"
    CCG_VM_1080p2997 = "1080p2997"
    CCG_VM_1080p3000 = "1080p3000"
    CCG_VM_1080p5000 = "1080p5000"
    CCG_VM_1080p5994 = "1080p5994"
    CCG_VM_1080p6000 = "1080p6000"
    CCG_VM_1556p2398 = "1556p2398"
    CCG_VM_1556p2400 = "1556p2400"
    CCG_VM_1556p2500 = "1556p2500"
    CCG_VM_dci1080p2398 = "dci1080p2398"
    CCG_VM_dci1080p2400 = "dci1080p2400"
    CCG_VM_dci1080p2500 = "dci1080p2500"
    CCG_VM_2160p2398 = "2160p2398"
    CCG_VM_2160p2400 = "2160p2400"
    CCG_VM_2160p2500 = "2160p2500"
    CCG_VM_2160p2997 = "2160p2997"
    CCG_VM_2160p3000 = "2160p3000"
    CCG_VM_2160p5000 = "2160p5000"
    CCG_VM_2160p5994 = "2160p5994"
    CCG_VM_2160p6000 = "2160p6000"
    CCG_VM_dci2160p2398 = "dci2160p2398"
    CCG_VM_dci2160p2400 = "dci2160p2400"
    CCG_VM_dci2160p2500 = "dci2160p2500"

class CCG_AudioChannelLayout(Enum):
    CCG_ACL_MONO = "mono"
    CCG_ACL_STEREO = "stereo"
    CCG_ACL_MATRIX = "matrix"
    CCG_ACL_FILM = "film"
    CCG_ACL_SMPTE = "smpte"
    CCG_ACL_EBU_R123_8A = "ebu_r123_8a"
    CCG_ACL_EBU_R123_8B = "ebu_r123_8b"
    CCG_ACL_8CH = "8ch"
    CCG_ACL_16CH = "16ch"

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
        choices=[(tag, tag.value) for tag in CCG_VideoMode],
        default=CCG_VideoMode.CCG_VM_PAL
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
        choices=[(tag, tag.value) for tag in CCG_VideoMode],
        default=CCG_VideoMode.CCG_VM_PAL
    )
    straightAlphaOutput = models.BooleanField(
        default="false"
    )
    audioChannelLayout = models.CharField(
        max_length=20,
        choices=[(tag, tag.value) for tag in CCG_AudioChannelLayout],
        default=CCG_AudioChannelLayout.CCG_ACL_STEREO
    )

    def __str__(self):
        return "%s" % (self.consumerID)

class ServerSettings(models.Model):
    settingsID = models.UUIDField
    serverID = models.ForeignKey('Servers', on_delete=models.CASCADE)
    logLevel = models.CharField(
        max_length=15,
        choices=[(tag, tag.value) for tag in CCG_LoggingLevels],
        default= CCG_LoggingLevels.CCG_LL_INFO
    )
    logCategories = models.CharField(
        max_length=22,
        choices=[(tag, tag.value) for tag in CCG_LogCategories],
        default= CCG_LogCategories.CCG_LC_COMMUNICATION
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
        choices=[(tag, tag.value) for tag in CCG_Accelerator],
        default= CCG_Accelerator.CCG_ACC_AUTO
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
