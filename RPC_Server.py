from xmlrpc.server import SimpleXMLRPCServer

def is_runing():
    return True

def sendText(text):
    with open('log.txt', 'a') as the_file:
        the_file.write(text+'\n')

server = SimpleXMLRPCServer(("0.0.0.0", 8000), allow_none=True)
print("Listening on port 8000...")
server.register_function(is_runing, "is_runing")
server.register_function(sendText, "sendText")
server.serve_forever()