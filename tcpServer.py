import SocketServer
import time
import datetime
import logging
import wx
from wx.lib.pubsub import setupkwargs
from wx.lib.pubsub import pub
import sys

logging.basicConfig(level=logging.INFO,
                    format='%(name)s: %(message)s')
  
class TCPServerHandler(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger("TCPServerHandler")
        self.logger.debug('__init__')
        
        pub.subscribe(self.close_request, 'TCPS_Close_Request')
        pub.subscribe(self.send_data,'TCPS_Send_Data')    
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
          
    def setup(self):
        self.logger.debug('setup')
        return SocketServer.BaseRequestHandler.setup(self)
      
    def handle(self):
        self.logger.debug('handle')
        self.request.settimeout(5)

        self.logger.info('%s connected',self.client_address)
        wx.CallAfter(pub.sendMessage, 'TCPStatus_Recv', data= "connected " + str(self.client_address[0]) +
                     "," + str(self.client_address[1]) + "\r\n")
        while True:
            try:
                recv_data = self.request.recv(1024)
                if not recv_data:
                    self.request.close()
                    self.logger.info('%s disconnected',self.client_address)
                    break
     
                self.logger.debug('recv()->"%s"',recv_data)
                #self.request.send(self.data)
                wx.CallAfter(pub.sendMessage,'TCPS_Recv_data',data=recv_data)
            except:
                pass
        
    def close_request(self):
        self.request.close()
        
        wx.CallAfter(pub.sendMessage, 'TCPStatus_Recv', data= "disconnected " + str(self.client_address[0]) +
                     "," + str(self.client_address[1]) + "\r\n")
        self.logger.info('%s disconnected',self.client_address)
    
    def send_data(self,data):
        self.request.send(data)
        
    def finish(self):
        self.logger.debug('finish')
        return SocketServer.BaseRequestHandler.finish(self)

        
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

      
if __name__ == '__main__':
    HOST, PORT = "", 5000
    server = SocketServer.TCPServer((HOST,PORT), TCPServerHandler)
    server.serve_forever()

