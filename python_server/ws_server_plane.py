#!/usr/bin/env python

# WS server example

##import asyncio
##import websockets
##import keyboard
from pykeyboard import PyKeyboard
k = PyKeyboard()

def steer(val):
    val = eval(val)
    if val[0] < -2 :
        k.press_key("d")
        k.release_key("a")
##        keyboard.call_later(lambda a=0: keyboard.release("a"), args=("a"), delay=0.1)
    elif -2 < val[0] < 2 :
        k.release_key("a")
        k.release_key("d")
    elif val[0] > 2 :
        k.press_key("a")
        k.release_key("d")
##        keyboard.call_later(lambda a=0: keyboard.release("d"), args=("d"), delay=0.1)

    if val[1] < -2 :
        k.press_key("u")
        k.release_key("j")
##        keyboard.call_later(lambda a=0: keyboard.release("a"), args=("a"), delay=0.1)
    elif -2 < val[1] < 2 :
        k.release_key("u")
        k.release_key("j")
    elif val[1] > 2 :
        k.press_key("j")
        k.release_key("u")

##
##    if val[0] < -3 :
##        keyboard.press("w")
##        keyboard.call_later(lambda a=0: keyboard.release("w"), args=("w"), delay=0.5)
##
##    elif val[0] > 3 :
##        keyboard.press("s")
##        keyboard.call_later(lambda a=0: keyboard.release("s"), args=("s"), delay=0.5)
##sleep(5)
##for i in range(100):
##    keyboard.press("a")
####    keyboard.call_later(lambda a=0: keyboard.release("a"), args=("a"), delay=0.1)
####sleep(2)
##    sleep(0.01)
##    keyboard.release("a")
##
##port = 8765
##
##async def server(websocket, path):
##    data = await websocket.recv()
##    print("{}".format(data))
##
####    greeting = f"Hello {name}!"
##
####    await websocket.send("from python")
####    print(f"> {greeting}")
##
##start_server = websockets.serve(server, "0.0.0.0", port)
##print("server started on port {}".format(port))
##
##asyncio.get_event_loop().run_until_complete(start_server)
##asyncio.get_event_loop().run_forever()
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
##        self.sendMessage(self.data)
        print(self.data)
        steer(self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('0.0.0.0', 8000, SimpleEcho)
server.serveforever()
