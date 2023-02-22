#!/usr/bin/env python

from websockets import serve
from asyncio import get_event_loop

PORT = 3000

class WebSocketServer():
    def __init__(self):
        """Init the class variables
        Args
            self.__server: It will receive a ws server to recv client requests
        """
        self.__server = None

    def __get_server__(self):
        """Returns the self.__server attribute
        
        Returns:
            self.__server: the server to recv requests from clients
        """
        return self.__server

    def __connect_ws_system__(self, handle_function):
        """Handler ws function
        
        Returns:
            A ws server
        """
        server = serve(handle_function, "localhost", PORT)
        return (server)

    def __startServer__(self, handle_function):
        """Start a ws server"""
        self.__server = self.__connect_ws_system__(handle_function)
        get_event_loop().run_until_complete(self.__server)
        get_event_loop().run_forever()