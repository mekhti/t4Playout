from django.db import models
from uuid import uuid4

import Playout.Models.ccgEnums as CCGEnums


"""--------------------------------------------------------------------------

 ######                             
 #     #   ##   ##### #    #  ####  
 #     #  #  #    #   #    # #      
 ######  #    #   #   ######  ####  
 #       ######   #   #    #      # 
 #       #    #   #   #    # #    # 
 #       #    #   #   #    #  ####  


Paths configuration class for CasparCG engine.

--------------------------------------------------------------------------"""

class Paths(models.Model):
    objID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4(),
        editable=False
    )
    mediaPath = models.FilePathField(
        help_text='Path to media files folder located at the same machine with CasparCG engine.'
    )
    logPath = models.FilePathField(
        help_text='Path to log files folder located at the same machine with CasparCG engine.'
    )
    dataPath = models.FilePathField(
        help_text='Path to data files folder located at the same machine with CasparCG engine.'
    )
    templatePath = models.FilePathField(
        help_text='Path to template files folder located at the same machine with CasparCG engine.'
    )
    thumbnailsPath = models.FilePathField(
        help_text='Path to thumbnails files folder located at the same machine with CasparCH engine.'
    )
    fontPath = models.FilePathField(
        help_text='Path to fonts files folder located at the same machine with CasparCG engine.'
    )

    def __str__(self):
        return '%s' % (self.pathsID)

    class Meta:
        db_table = 'ccgengine_paths'



"""--------------------------------------------------------------------------

 #######                                                           
    #    #    # #    # #    # #####  #    #   ##   # #       ####  
    #    #    # #    # ##  ## #    # ##   #  #  #  # #      #      
    #    ###### #    # # ## # #####  # #  # #    # # #       ####  
    #    #    # #    # #    # #    # #  # # ###### # #           # 
    #    #    # #    # #    # #    # #   ## #    # # #      #    # 
    #    #    #  ####  #    # #####  #    # #    # # ######  ####  
                                                          
                                                          
Thumbnails generator configuration for CasparCG engine.

---------------------------------------------------------------------------"""

class ThumbnailsGenerator(models.Model):
    objID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4(),
        editable=False
    )

    def __str__(self):
        return '%s' % (self.objID)

    class Meta:
        db_table = 'ccgengine_thumbnails'



"""--------------------------------------------------------------------------

 ######                                              
 #     # ######  ####  #    # #      # #    # #    # 
 #     # #      #    # #   #  #      # ##   # #   #  
 #     # #####  #      ####   #      # # #  # ####   
 #     # #      #      #  #   #      # #  # # #  #   
 #     # #      #    # #   #  #      # #   ## #   #  
 ######  ######  ####  #    # ###### # #    # #    # 


Decklink consumer configuration for CasparCG engine channel.                                                      

--------------------------------------------------------------------------"""

class DecklinkConsumer(models.Model):
    objID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4(),
        editable=False
    )

    deviceId = models.PositiveSmallIntegerField(
        help_text='Decklink device id.'
    )

    keyDevice = models.PositiveSmallIntegerField(
        help_text='Decklink device id for key. Must not be the same main device id.'
    )

    embeddedAudio = models.BooleanField(
        help_text='Is needed to embedd audio to Decklink video output (SDI or HDMI output meaning).',
        default=False
    )

    audioChannelLayout = models.CharField(
        help_text='Audio layout for channel. Must be one of mono, stereo, '
                  'matrix, film, smpte, ebu_r123_8a, ebu_r123_8b, 8ch, 16ch.',
        max_length=20,
        choices=CCGEnums.AudioChannelsLayout.Choices,
        default=CCGEnums.AudioChannelsLayout.STRO
    )

    latency = models.CharField(
        help_text='Channel latency for Decklink output. Must be one of normal, low, default',
        max_length=20,
        choices=CCGEnums.DecklinkLatency.Choices,
        default=CCGEnums.DecklinkLatency.NORM
    )

    keyer = models.CharField(
        help_text='Keyer for Decklink output. Must be one of external, external_separate_device, internal, default.',
        max_length=20,
        choices=CCGEnums.DecklinkKeyer.Choices,
        default=CCGEnums.DecklinkKeyer.EXTR
    )

    keyOnly = models.BooleanField(
        help_text='Is output only key.',
        default=False
    )

    bufferDepth = models.PositiveSmallIntegerField(
        help_text='Depth of Decklink card.',
    )

    def __str__(self):
        return '%s' % (self.objID)

    class Meta:
        db_table = 'ccgengine_decklink_consumers'



"""--------------------------------------------------------------------------

 ######                                              
 #     # #      #    # ###### ###### #  ####  #    # 
 #     # #      #    # #      #      # #      #    # 
 ######  #      #    # #####  #####  #  ####  ###### 
 #     # #      #    # #      #      #      # #    # 
 #     # #      #    # #      #      # #    # #    # 
 ######  ######  ####  ###### #      #  ####  #    # 
                                                     

Decklink consumer configuration for CasparCG engine channel.                                                      

---------------------------------------------------------------------------"""

class BluefishConsumer(models.Model):
    objID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4(),
        editable=False
    )

    deviceId = models.PositiveSmallIntegerField(
        help_text='Bluefish device id.'
    )

    sdiStream = models.CharField(
        help_text='Select SDI stream for Bluefish device. Must be one of a, b, c, d.',
        max_length=5,
        choices=CCGEnums.BluefishSDIStream.Choices,
        default=CCGEnums.BluefishSDIStream.SDI_A
    )

    embeddedAudio = models.BooleanField(
        help_text='Is needed to embedd audio to Bluefish video output (SDI or HDMI output meaning).',
        default=False
    )

    audioChannelLayout = models.CharField(
        help_text='Audio layout for channel. Must be one of mono, stereo, '
                  'matrix, film, smpte, ebu_r123_8a, ebu_r123_8b, 8ch, 16ch.',
        max_length=20,
        choices=CCGEnums.AudioChannelsLayout.Choices,
        default=CCGEnums.AudioChannelsLayout.STRO
    )

    keyOnly = models.BooleanField(
        help_text='Is output only key.',
        default=False
    )

    keyer = models.CharField(
        help_text='Keyer for Bluefish output. Must be one of external, '
                  'internal or disabled. External only supported on '
                  'channels a and c, using c requires 4 out connectors. '
                  'Internal only available on devices with a hardware keyer.',
        max_length=20,
        choices=CCGEnums.BluefishKeyer.Choices,
        default=CCGEnums.BluefishKeyer.DSBL
    )

    internalKeyerAudioSource = models.CharField(
        help_text='Audio source for audio keyer. Must be one of videooutputchannel '
                  'or sdivideoinput. Only valid when using internal keyer option.',
        max_length=20,
        choices=CCGEnums.BluefishInternalKeyerAudioSource.Choices,
        default=CCGEnums.BluefishInternalKeyerAudioSource.VIDO
    )

    def __str__(self):
        return '%s' % (self.objID)

    class Meta:
        db_table = 'ccgengine_bluefish_consumers'


"""--------------------------------------------------------------------------

  #####                                                                    
 #     # #   #  ####  ##### ###### #    #      ##   #    # #####  #  ####  
 #        # #  #        #   #      ##  ##     #  #  #    # #    # # #    # 
  #####    #    ####    #   #####  # ## #    #    # #    # #    # # #    # 
       #   #        #   #   #      #    #    ###### #    # #    # # #    # 
 #     #   #   #    #   #   #      #    #    #    # #    # #    # # #    # 
  #####    #    ####    #   ###### #    #    #    #  ####  #####  #  ####  


System audio consumer configuration for CasparCG engine channel.                                                      

---------------------------------------------------------------------------"""


class SystemAudioConsumer(models.Model):
    objID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4(),
        editable=False
    )

    audioChannelLayout = models.CharField(
        help_text='Audio layout for channel. Must be one of mono, stereo, '
                  'matrix, film, smpte, ebu_r123_8a, ebu_r123_8b, 8ch, 16ch.',
        max_length=20,
        choices=CCGEnums.AudioChannelsLayout.Choices,
        default=CCGEnums.AudioChannelsLayout.STRO
    )

    latency = models.PositiveSmallIntegerField(
        help_text='Latensy for system audio output in msec.'
    )

    def __str__(self):
        return '%s' % (self.objID)

    class Meta:
        db_table = 'ccgengine_systemaudio_consumers'



"""--------------------------------------------------------------------------

  #####                                     
 #     #  ####  #####  ###### ###### #    # 
 #       #    # #    # #      #      ##   # 
  #####  #      #    # #####  #####  # #  # 
       # #      #####  #      #      #  # # 
 #     # #    # #   #  #      #      #   ## 
  #####   ####  #    # ###### ###### #    # 
                                                          
                                                          
Screen consumer configuration for CasparCG engine channel.

---------------------------------------------------------------------------"""

class ScreenConsumer(models.Model):
    objID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4(),
        editable=False
    )

    deviceId = models.PositiveSmallIntegerField(
        help_text='Screen device id. Must be positive integer.'
    )

    aspectRatio = models.CharField(
        help_text='Video output aspect ratio. Must be one of default, 4:3 or 16:9.',
        max_length=20,
        choices=CCGEnums.ScreenAspectRatio.Choices,
        default=CCGEnums.ScreenAspectRatio.DFLT
    )

    stretch = models.CharField(
        help_text='Video output stretch. Must be one of none, fill, uniform or uniform_to_fill.',
        max_length=20,
        choices=CCGEnums.ScreenStretch.Choices,
        default=CCGEnums.ScreenStretch.FILL
    )

    windowed = models.BooleanField(
        help_text='Is screen output windowed.',
        default=True
    )

    keyOnly = models.BooleanField(
        help_text='Is output only key.',
        default=False
    )

    autoDeinterlace = models.BooleanField(
        help_text='Is deinterlace enabled.',
        default=True
    )

    vsync = models.BooleanField(
        help_text='Is vsync enabled.',
        default=False
    )

    interactive = models.BooleanField(
        help_text='Is interaction enabled.',
        default=True
    )

    borderless = models.BooleanField(
        help_text='Is window borderless.',
        default=False
    )

    def __str__(self):
        return '%s' % (self.objID)

    class Meta:
        db_table = 'ccgengine_screen_consumer'



"""--------------------------------------------------------------------------

 #     #                                      ### #     #  #####     #    
 ##    # ###### #    # ##### ###### #    #     #  #     # #     #   # #   
 # #   # #      #    #   #   #      #   #      #  #     # #        #   #  
 #  #  # #####  #    #   #   #####  ####       #  #     # #  #### #     # 
 #   # # #      # ## #   #   #      #  #       #   #   #  #     # ####### 
 #    ## #      ##  ##   #   #      #   #      #    # #   #     # #     # 
 #     # ###### #    #   #   ###### #    #    ###    #     #####  #     # 
                                                          
                                                          
Newtek IVGA consumer configuration for CasparCG engine channel.

---------------------------------------------------------------------------"""

class NewtekIVGAConsumer(models.Model):
    objID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4(),
        editable=False
    )

    def __str__(self):
        return '%s' % (self.objID)

    class Meta:
        db_table = 'ccgengine_newtekivga_consumer'



"""--------------------------------------------------------------------------

 ####### ####### #     # ######  #######  #####      #####                                
 #       #       ##   ## #     # #       #     #    #     # # #    # #####  #      ###### 
 #       #       # # # # #     # #       #          #       # ##  ## #    # #      #      
 #####   #####   #  #  # ######  #####   #  ####     #####  # # ## # #    # #      #####  
 #       #       #     # #       #       #     #          # # #    # #####  #      #      
 #       #       #     # #       #       #     #    #     # # #    # #      #      #      
 #       #       #     # #       #######  #####      #####  # #    # #      ###### ###### 
                                                          
                                                          
FFMPEG simple consumer configuration for CasparCG engine channel.

---------------------------------------------------------------------------"""

class FFMPEGSimpleConsumer(models.Model):
    objID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4(),
        editable=False
    )

    outputType = models.CharField(
        help_text='Type of FFMPEG output. Must be one of NONE, FILE or STREAM.',
        choices=CCGEnums.FFMPEGOutputType.Choices,
        default=CCGEnums.FFMPEGOutputType.NONE
    )

    pathToFile = models.FilePathField(
        help_text = 'Path to file for FFMPEG simple output.'
    )

    pathToURL = models.URLField(
        help_text = 'URL field for FFMPEG simple output. Only UDP protocol supported as URL.'
    )

    arguments = models.TextField(
        help_text='Most ffmpeg arguments related to filtering and output codecs. Maximum '
                  'length of commands string is 2048 symbols include spaces.',
        max_length=2048
    )

    monostreams = models.BooleanField(
        help_text='Is monostreams enabled.',
        default=False
    )

    def __str__(self):
        return '%s' % (self.objID)

    class Meta:
        db_table = 'ccgengine_ffmpeg_simple_consumer'



"""--------------------------------------------------------------------------

 ####### ####### #     # ######  #######  #####        #                  
 #       #       ##   ## #     # #       #     #      # #   #####  #    # 
 #       #       # # # # #     # #       #           #   #  #    # #    # 
 #####   #####   #  #  # ######  #####   #  ####    #     # #    # #    # 
 #       #       #     # #       #       #     #    ####### #    # #    # 
 #       #       #     # #       #       #     #    #     # #    #  #  #  
 #       #       #     # #       #######  #####     #     # #####    ##   
                                                            
                                                          
FFMPEG advanced consumer configuration for CasparCG engine channel.

---------------------------------------------------------------------------"""

class FFMPEGAdvancedConsumer(models.Model):
    objID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4(),
        editable=False
    )

    def __str__(self):
        return '%s' % (self.objID)

    class Meta:
        db_table = 'ccgengine_ffmpeg_adv_consumer'



"""--------------------------------------------------------------------------

  #####                                    
 #     # ##### #####  ######   ##   #    # 
 #         #   #    # #       #  #  ##  ## 
  #####    #   #    # #####  #    # # ## # 
       #   #   #####  #      ###### #    # 
 #     #   #   #   #  #      #    # #    # 
  #####    #   #    # ###### #    # #    # 
                                                              
                                                          
FFMPEG advanced consumer configuration for CasparCG engine channel.

---------------------------------------------------------------------------"""

class StreamConsumer(models.Model):
    objID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4(),
        editable=False
    )

    def __str__(self):
        return '%s' % (self.objID)

    class Meta:
        db_table = 'ccgengine_stream_consumer'



"""--------------------------------------------------------------------------

  #####                                                   
 #     #  ####  #    #  ####  #    # #    # ###### #####  
 #       #    # ##   # #      #    # ##  ## #      #    # 
 #       #    # # #  #  ####  #    # # ## # #####  #    # 
 #       #    # #  # #      # #    # #    # #      #####  
 #     # #    # #   ## #    # #    # #    # #      #   #  
  #####   ####  #    #  ####   ####  #    # ###### #    # 
                                                          
                                                          
Consumer configuration class for CasparCG engine channel.

---------------------------------------------------------------------------"""

class Consumer(models.Model):
    objID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4(),
        editable=False
    )

    def __str__(self):
        return '%s' % (self.objID)

    class Meta:
        db_table = 'ccgengine_bluefish_consumer'



"""--------------------------------------------------------------------------

  #####                                                   
 #     # #    #   ##   #    # #    # ###### #       ####  
 #       #    #  #  #  ##   # ##   # #      #      #      
 #       ###### #    # # #  # # #  # #####  #       ####  
 #       #    # ###### #  # # #  # # #      #           # 
 #     # #    # #    # #   ## #   ## #      #      #    # 
  #####  #    # #    # #    # #    # ###### ######  ####  


Channel configuration class for CasparCG engine configuration.

--------------------------------------------------------------------------"""

class Channel(models.Model):
    objID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4(),
        editable=False
    )

    videoMode = models.CharField(
        help_text= 'Video mode for channel. Must be one of PAL, NTSC, '
                   '576p2500, 720p2398, 720p2400, 720p2500, 720p5000, '
                   '720p2997, 720p5994, 720p3000, 720p6000, 1080p2398, '
                   '1080p2400, 1080i5000, 1080i5994, 1080i6000, 1080p2500, '
                   '1080p2997, 1080p3000, 1080p5000, 1080p5994, 1080p6000, '
                   '1556p2398, 1556p2400, 1556p2500, dci1080p2398, dci1080p2400, '
                   'dci1080p2500, 2160p2398, 2160p2400, 2160p2500, 2160p2997, '
                   '2160p3000, 2160p5000, 2160p5994, 2160p6000, dci2160p2398, '
                   'dci2160p2400, dci2160p2500.',
        max_length=20,
        choices=CCGEnums.VIdeoMode.Choices,
        default=CCGEnums.VIdeoMode.VM_PAL
    )

    straightAlphaOutput = models.BooleanField(
        help_text='Is streight alpha output enabled.',
        default=False
    )

    audioChannelLayout = models.CharField(
        help_text='Audio layout for channel. Must be one of mono, stereo, '
                  'matrix, film, smpte, ebu_r123_8a, ebu_r123_8b, 8ch, 16ch',
        max_length=20,
        choices=CCGEnums.AudioChannelsLayout.Choices,
        default=CCGEnums.AudioChannelsLayout.STRO
    )

    def __str__(self):
        return '%s' % (self.objID)

    class Meta:
        db_table = 'ccgengine_channels'



"""--------------------------------------------------------------------------

  #####                                                                           
 #     #  ####  #    # ###### #  ####  #    # #####    ##   ##### #  ####  #    # 
 #       #    # ##   # #      # #    # #    # #    #  #  #    #   # #    # ##   # 
 #       #    # # #  # #####  # #      #    # #    # #    #   #   # #    # # #  # 
 #       #    # #  # # #      # #  ### #    # #####  ######   #   # #    # #  # # 
 #     # #    # #   ## #      # #    # #    # #   #  #    #   #   # #    # #   ## 
  #####   ####  #    # #      #  ####   ####  #    # #    #   #   #  ####  #    # 
                                       
                                       
Configuration class for CasparCG engine. All possible configurations implemented.

--------------------------------------------------------------------------"""

class Configuration(models.Model):
    objID = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4(),
        editable=False
    )

    pathSettings = models.ForeignKey(Paths, on_delete=models.CASCADE)

    lockClearPhrase = models.CharField(
        help_text='Field for passphrase for lock clear function on CasparCG engine. Maximum lenth of passphrase is 8(eight).',
        max_length=16
    )

    def __str__(self):
        return '%s' % (self.objID)

    class Meta:
        db_table = 'ccgengine_config'
