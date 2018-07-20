import os
import platform

def checkOs():
    osInfoObject = {
        'osType': os.name,
        'systemType': platform.system(),
        'systemRelease': platform.release()
    }
    return osInfoObject

def definePathDelimiter():
    osInfoObject = checkOs()
    if(osInfoObject['systemType'] == 'Windows'):
        return '\\'
    else:
        return '/'
    pass