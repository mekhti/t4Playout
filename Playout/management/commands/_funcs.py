import os
import platform

def checkOs():
    return {
        'osType': os.name,
        'systemType': platform.system(),
        'systemRelease': platform.release()
    }

def definePathDelimiter():
    osInfoObject = checkOs()
    if(osInfoObject['systemType'] == 'Windows'):
        return '\\'
    else:
        return '/'