#!/usr/bin/env python

"""Imports"""
from websockets import serve
from asyncio import get_event_loop

PORT = 3000

class WebSocketServer():
    def __init__(self, maindirectory):
        """Private attributes"""
        self.__server = None
        """Public attributes"""
        self.maindirectory = maindirectory
        self.EventWriter   = None

    def __get_server__(self):
        return self.__server

    def __connect_ws_system__(self, handle_function):
        server = serve(handle_function, "localhost", PORT)
        return (server)

    def __startServer__(self, handle_function):
        """Start a ws server"""
        self.__server = self.__connect_ws_system__(handle_function)
        get_event_loop().run_until_complete(self.__server)
        get_event_loop().run_forever()