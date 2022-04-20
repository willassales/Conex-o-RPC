from socket import *
from http import *
from operator import add
from xmlrpc.server import SimpleXMLRPCServer  #importar a biblioteca
from xmlrpc.server import SimpleXMLRPCRequestHandler



#HOST = gethostname() 
#PORT = 8000

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 6789),
                        requestHandler=RequestHandler) as servidor:
    servidor.register_introspection_functions()

    class MyFuncs:

        def som(self, x,y):
            return x+y
        def mult(self,x, y):
            return x * y
        def sub(self,x,y):
            return x-y
        def div(self,x,y):
            if y == 0:
                return "erro não pode dividir por zero!!"
            else:
                return x/y


    print("Servidor executando na porta 6789")

    servidor.register_instance(MyFuncs())
    servidor.serve_forever()



