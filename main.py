from source.server.WebSocketServer import WebSocketServer
from source.proxy.ProxyAccess import ProxyAccess

if __name__ == "__main__":
    Access = ProxyAccess()
    WsServer = WebSocketServer()
    WsServer.__startServer__(Access.__msg_handler__)