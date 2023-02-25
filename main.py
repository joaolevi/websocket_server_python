"""Package Imports"""
from os import path, makedirs
from inspect import getfile, currentframe
from logging import basicConfig, getLogger, DEBUG

"""Source Imports"""
from source.server.WebSocketServer import WebSocketServer
from source.proxy.ProxyAccess import ProxyAccess

def get_main_directory():
    return path.dirname(path.abspath(getfile(currentframe())))

def start_log(maindirectory):
    
    directory = maindirectory + '/log'
    if (not path.exists(directory)):
        makedirs(directory)
        
    basicConfig(filename="./log/EventMain.log", format='%(asctime)s %(message)s', filemode='w')
    EventWriter = getLogger()
    EventWriter.setLevel(DEBUG)
    return EventWriter

if __name__ == "__main__":
    maindirectory = get_main_directory()
    EventWriter = start_log(maindirectory)
    EventWriter.warning(maindirectory)
    Access   = ProxyAccess(maindirectory, EventWriter)
    WsServer = WebSocketServer(maindirectory)
    WsServer.__startServer__(Access.__msg_handler__)