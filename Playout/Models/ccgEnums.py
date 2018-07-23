
class LoggingLevels():
    TRAC = 'trace'
    DEBG = 'debug'
    INFO = 'info'
    WARN = 'warning'
    ERRO = 'error'
    FATL = 'fatal'
    Choices = (
        (TRAC, 'trace'),
        (DEBG, 'debug'),
        (INFO, 'info'),
        (WARN, 'warning'),
        (ERRO, 'error'),
        (FATL, 'fatal'),
    )

class LogCategories():
    COMM = 'communication'
    CTRC = 'calltrace'
    BOTH = 'calltrace,communication'
    Choices = (
        (COMM, 'communication'),
        (CTRC, 'calltrace'),
        (BOTH, 'calltrace,communication'),
    )

class Accelerator():
    AUTO = 'auto'
    CPU = 'cpu'
    GPU = 'gpu'
    Choices = (
        (AUTO, 'auto'),
        (CPU, 'cpu'),
        (GPU, 'gpu'),
    )

class VIdeoMode():
    VM_PAL = 'PAL'
    VM_NTSC = 'NTSC'
    VM_576p2500 = '576p2500'
    VM_720p2398 = '720p2398'
    VM_720p2400 = '720p2400'
    VM_720p2500 = '720p2500'
    VM_720p5000 = '720p5000'
    VM_720p2997 = '720p2997'
    VM_720p5994 = '720p5994'
    VM_720p3000 = '720p3000'
    VM_720p6000 = '720p6000'
    VM_1080p2398 = '1080p2398'
    VM_1080p2400 = '1080p2400'
    VM_1080i5000 = '1080i5000'
    VM_1080i5994 = '1080i5994'
    VM_1080i6000 = '1080i6000'
    VM_1080p2500 = '1080p2500'
    VM_1080p2997 = '1080p2997'
    VM_1080p3000 = '1080p3000'
    VM_1080p5000 = '1080p5000'
    VM_1080p5994 = '1080p5994'
    VM_1080p6000 = '1080p6000'
    VM_1556p2398 = '1556p2398'
    VM_1556p2400 = '1556p2400'
    VM_1556p2500 = '1556p2500'
    VM_dci1080p2398 = 'dci1080p2398'
    VM_dci1080p2400 = 'dci1080p2400'
    VM_dci1080p2500 = 'dci1080p2500'
    VM_2160p2398 = '2160p2398'
    VM_2160p2400 = '2160p2400'
    VM_2160p2500 = '2160p2500'
    VM_2160p2997 = '2160p2997'
    VM_2160p3000 = '2160p3000'
    VM_2160p5000 = '2160p5000'
    VM_2160p5994 = '2160p5994'
    VM_2160p6000 = '2160p6000'
    VM_dci2160p2398 = 'dci2160p2398'
    VM_dci2160p2400 = 'dci2160p2400'
    VM_dci2160p2500 = 'dci2160p2500'
    Choices = (
        (VM_PAL, 'PAL'),
        (VM_NTSC, 'NTSC'),
        (VM_576p2500, '576p2500'),
        (VM_720p2398, '720p2398'),
        (VM_720p2400, '720p2400'),
        (VM_720p2500, '720p2500'),
        (VM_720p5000, '720p5000'),
        (VM_720p2997, '720p2997'),
        (VM_720p5994, '720p5994'),
        (VM_720p3000, '720p3000'),
        (VM_720p6000, '720p6000'),
        (VM_1080p2398, '1080p2398'),
        (VM_1080p2400, '1080p2400'),
        (VM_1080i5000, '1080i5000'),
        (VM_1080i5994, '1080i5994'),
        (VM_1080i6000, '1080i6000'),
        (VM_1080p2500, '1080p2500'),
        (VM_1080p2997, '1080p2997'),
        (VM_1080p3000, '1080p3000'),
        (VM_1080p5000, '1080p5000'),
        (VM_1080p5994, '1080p5994'),
        (VM_1080p6000, '1080p6000'),
        (VM_1556p2398, '1556p2398'),
        (VM_1556p2400, '1556p2400'),
        (VM_1556p2500, '1556p2500'),
        (VM_dci1080p2398, 'dci1080p2398'),
        (VM_dci1080p2400, 'dci1080p2400'),
        (VM_dci1080p2500, 'dci1080p2500'),
        (VM_2160p2398, '2160p2398'),
        (VM_2160p2400, '2160p2400'),
        (VM_2160p2500, '2160p2500'),
        (VM_2160p2997, '2160p2997'),
        (VM_2160p3000, '2160p3000'),
        (VM_2160p5000, '2160p5000'),
        (VM_2160p5994, '2160p5994'),
        (VM_2160p6000, '2160p6000'),
        (VM_dci2160p2398, 'dci2160p2398'),
        (VM_dci2160p2400, 'dci2160p2400'),
        (VM_dci2160p2500, 'dci2160p2500'),
    )

class AudioChannelsLayout():
    MONO = 'mono'
    STRO = 'stereo'
    MTRX = 'matrix'
    FILM = 'film'
    SMPT = 'smpte'
    ER8A = 'ebu_r123_8a'
    ER8B = 'ebu_r123_8b'
    A8CH = '8ch'
    A16C = '16ch'
    Choices = (
        (MONO, 'mono'),
        (STRO, 'stereo'),
        (MTRX, 'matrix'),
        (FILM, 'film'),
        (SMPT, 'smpte'),
        (ER8A, 'ebu_r123_8a'),
        (ER8B, 'ebu_r123_8b'),
        (A8CH, '8ch'),
        (A16C, '16ch'),
    )

class DecklinkLatency():
    NORM = 'normal'
    LOW = 'low'
    DFLT = 'default'
    Choices = (
        (NORM, 'normal'),
        (LOW, 'low'),
        (DFLT, 'default'),
    )

class DecklinkKeyer():
    EXTR = 'external'
    EXSD = 'external_separate_device'
    INTR = 'internal'
    DFLT = 'default'
    Choices = (
        (EXTR, 'external'),
        (EXSD, 'external_separate_device'),
        (INTR, 'internal'),
        (DFLT, 'default'),
    )

class BluefishSDIStream():
    SDI_A = 'a'
    SDI_B = 'b'
    SDI_C = 'c'
    SDI_D = 'd'
    Choices = (
        (SDI_A, 'a'),
        (SDI_B, 'b'),
        (SDI_C, 'c'),
        (SDI_D, 'd'),
    )

class BluefishKeyer():
    EXTR = 'external'
    INTR = 'internal'
    DSBL = 'disabled'
    Choices = (
        (EXTR, 'external'),
        (INTR, 'internal'),
        (DSBL, 'disabled'),
    )

class BluefishInternalKeyerAudioSource():
    VIDO = 'videooutputchannel'
    SDIO = 'sdivideoinput'
    Choices = (
        (VIDO, 'videooutputchannel'),
        (SDIO, 'sdivideoinput'),
    )

class ScreenAspectRatio():
    DFLT = 'default'
    AR_4_3 = '4:3'
    AR_16_9 = '16:9'
    Choices = (
        (DFLT, 'default'),
        (AR_4_3, '4:3'),
        (AR_16_9, '16:9'),
    )

class ScreenStretch():
    NONE = 'none'
    FILL = 'fill'
    UNFR = 'uniform'
    U2FL = 'uniform_to_fill'
    Choices = (
        (NONE, 'none'),
        (FILL, 'fill'),
        (UNFR, 'uniform'),
        (U2FL, 'uniform_to_fill'),
    )