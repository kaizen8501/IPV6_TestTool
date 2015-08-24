# -*- coding: utf-8 -*- 
 
###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
 
import wx
import os
import wx.xrc
from wx.lib.pubsub import pub
import serial
import serial.tools.list_ports
import threading
import wx.lib.newevent
import time
import sys
import filecmp
import socket
import tcpServer


lock = threading.Lock()
cv = threading.Condition()

class TCPLoopback_Infinite(threading.Thread):
    def __init__(self, parent):
        threading.Thread.__init__(self)
        self._parent = parent
        self._isStop = False
        self.start()
        
    def run(self):
        while True:
            if self._isStop == True: break

            cv.acquire()

            self._parent.m_tcpFileName = self._parent.m_textCtrl_TCP_FilePath.GetValue()
            if self._parent.m_tcpFileName == '': return
            
            self._parent.m_tcpFileSize = os.stat(self._parent.m_tcpFileName).st_size
            file_data = ""
            send_file = open(self._parent.m_tcpFileName,'rb')
            for i in xrange(0,self._parent.m_tcpFileSize,1024):
                data = send_file.read(1024)
                file_data += data
            send_file.close()

            self._parent.m_IstcpLoopback_First = True

            try:
                for i in xrange(0,self._parent.m_tcpFileSize,1024):
                    send_data = file_data[i:i+1024]
                    
                    if self._parent.m_checkBox_IsTCPServer.GetValue() == True:
                        wx.CallAfter(pub.sendMessage,'TCPS_Send_Data',data=send_data)
                    elif self._parent.m_checkBox_IsTCPClient.GetValue() == True:
                        self._parent.m_tcp_client_sock.sendall(send_data)

            except Exception as e:
                s = str(e)
                wx.MessageBox(s, 'Warning', wx.OK | wx.ICON_ERROR)

            cv.wait()
            cv.release()

            time.sleep(1)
        
        print 'Thread End'
                
    def stop(self):
        self._isStop = True

class TCPC_RecvThread(threading.Thread):
    def __init__(self, parent):
        threading.Thread.__init__(self)
        self._parent = parent
        self._isStop = False
        self.start()
        self.recv_data = ''
        
    def run(self):
        while True:
            if self._isStop == True:
                self._parent.m_tcp_client_sock.close()
                break
            try:
                self.recv_data = self._parent.m_tcp_client_sock.recv(1024)
            except socket.timeout:
                continue
            except Exception as e:
                wx.CallAfter(wx.MessageBox,e,'Warning', wx.OK|wx.ICON_ERROR)
            
            if not self.recv_data:
                self._parent.m_tcp_client_sock.close()
                break
        
            wx.CallAfter(pub.sendMessage,'TCPS_Recv_data',data=self.recv_data)
            
    def stop(self):
        self._isStop = True
        self._parent.m_tcp_client_sock.close()
            
 
###########################################################################
## Class Serial2Ethernet_Test_Tool
###########################################################################
 
class Serial2Ethernet_Test_Tool ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Serial to Ethernet Test Tool", pos = wx.DefaultPosition, size = wx.Size( 609,706 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_notebook_S2E_TestTool = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel_Serial = wx.Panel( self.m_notebook_S2E_TestTool, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer_SerialConfiguartion = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_Serial, wx.ID_ANY, u"Serial Configuration" ), wx.VERTICAL )
        
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_SerialComport = wx.StaticText( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_SerialComport.Wrap( -1 )
        bSizer7.Add( self.m_staticText_SerialComport, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_SerialComPortChoices = []
        self.m_comboBox_SerialComPort = wx.ComboBox( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_SerialComPortChoices, 0 )
        bSizer7.Add( self.m_comboBox_SerialComPort, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_SerialBuad = wx.StaticText( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, u"Baud", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_SerialBuad.Wrap( -1 )
        bSizer7.Add( self.m_staticText_SerialBuad, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_SerialBuadChoices = [ u"2400", u"9600", u"14400", u"19200", u"38400", u"57600", u"76800", u"115200", u"230400", u"460800" ]
        self.m_comboBox_SerialBuad = wx.ComboBox( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, u"115200", wx.DefaultPosition, wx.DefaultSize, m_comboBox_SerialBuadChoices, 0 )
        bSizer7.Add( self.m_comboBox_SerialBuad, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_SerialDataSize = wx.StaticText( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, u"Data size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_SerialDataSize.Wrap( -1 )
        bSizer7.Add( self.m_staticText_SerialDataSize, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_SerialDataSizeChoices = [ u"5", u"6", u"7", u"8" ]
        self.m_comboBox_SerialDataSize = wx.ComboBox( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, m_comboBox_SerialDataSizeChoices, 0 )
        bSizer7.Add( self.m_comboBox_SerialDataSize, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer_SerialConfiguartion.Add( bSizer7, 0, wx.ALL|wx.EXPAND, 5 )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_Parity = wx.StaticText( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, u"Parity", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Parity.Wrap( -1 )
        bSizer5.Add( self.m_staticText_Parity, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_ParityChoices = [ u"None", u"Even", u"Odd", u"Mark", u"Space" ]
        self.m_comboBox_Parity = wx.ComboBox( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, m_comboBox_ParityChoices, 0 )
        bSizer5.Add( self.m_comboBox_Parity, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_Handshake = wx.StaticText( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, u"Handshake", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Handshake.Wrap( -1 )
        bSizer5.Add( self.m_staticText_Handshake, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_HandshakeChoices = [ u"OFF", u"RTS/CTS", u"Xon/Xoff" ]
        self.m_comboBox_Handshake = wx.ComboBox( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, u"OFF", wx.DefaultPosition, wx.DefaultSize, m_comboBox_HandshakeChoices, 0 )
        bSizer5.Add( self.m_comboBox_Handshake, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_SerialStopbits = wx.StaticText( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, u"Stop Bits", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_SerialStopbits.Wrap( -1 )
        bSizer5.Add( self.m_staticText_SerialStopbits, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_SerialStopbitsChoices = [ u"1", u"1.5", u"2" ]
        self.m_comboBox_SerialStopbits = wx.ComboBox( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, m_comboBox_SerialStopbitsChoices, 0 )
        bSizer5.Add( self.m_comboBox_SerialStopbits, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer_SerialConfiguartion.Add( bSizer5, 0, wx.ALL|wx.EXPAND, 5 )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button_SerialOpen = wx.Button( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_button_SerialOpen, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_SerialClose = wx.Button( sbSizer_SerialConfiguartion.GetStaticBox(), wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_SerialClose.Enable( False )
        
        bSizer10.Add( self.m_button_SerialClose, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer_SerialConfiguartion.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        
        bSizer2.Add( sbSizer_SerialConfiguartion, 0, wx.ALL|wx.EXPAND, 5 )
        
        sbSizer_SerialScreen = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_Serial, wx.ID_ANY, u"Received/Send data" ), wx.VERTICAL )
        
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_textCtrl_SerialScreen = wx.TextCtrl( sbSizer_SerialScreen.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_textCtrl_SerialScreen.SetMaxLength( 102400 ) 
        bSizer8.Add( self.m_textCtrl_SerialScreen, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        sbSizer_SerialScreen.Add( bSizer8, 1, wx.EXPAND|wx.ALL, 5 )
        
        
        bSizer2.Add( sbSizer_SerialScreen, 1, wx.EXPAND|wx.ALL, 5 )
        
        sbSizerSerialLineSender = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_Serial, wx.ID_ANY, u"Line Sender" ), wx.VERTICAL )
        
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_textCtrl_SerialLineSender = wx.TextCtrl( sbSizerSerialLineSender.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizer9.Add( self.m_textCtrl_SerialLineSender, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        sbSizerSerialLineSender.Add( bSizer9, 1, wx.EXPAND|wx.ALL, 5 )
        
        
        bSizer2.Add( sbSizerSerialLineSender, 1, wx.EXPAND|wx.ALL, 5 )
        
        sbSizerSerialTextSender = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_Serial, wx.ID_ANY, u"Input Data" ), wx.VERTICAL )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_textCtrl_SerialInputText = wx.TextCtrl( sbSizerSerialTextSender.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_textCtrl_SerialInputText, 1, wx.ALL, 5 )
        
        self.m_buttonSerialTextSend = wx.Button( sbSizerSerialTextSender.GetStaticBox(), wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_buttonSerialTextSend, 0, wx.ALL, 5 )
        
        
        sbSizerSerialTextSender.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        
        bSizer2.Add( sbSizerSerialTextSender, 0, wx.EXPAND|wx.ALL, 5 )
        
        
        self.m_panel_Serial.SetSizer( bSizer2 )
        self.m_panel_Serial.Layout()
        bSizer2.Fit( self.m_panel_Serial )
        self.m_notebook_S2E_TestTool.AddPage( self.m_panel_Serial, u"Serial", False )
        self.m_panel_TCP = wx.Panel( self.m_notebook_S2E_TestTool, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer91 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer11 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer_TCPOption = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_TCP, wx.ID_ANY, u"Option" ), wx.VERTICAL )
        
        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_checkBox_IsTCPServer = wx.CheckBox( sbSizer_TCPOption.GetStaticBox(), wx.ID_ANY, u"TCP Server", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox_IsTCPServer.SetValue(True) 
        bSizer15.Add( self.m_checkBox_IsTCPServer, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_IsTCPClient = wx.CheckBox( sbSizer_TCPOption.GetStaticBox(), wx.ID_ANY, u"TCP Client", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.m_checkBox_IsTCPClient, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_IPver = wx.StaticText( sbSizer_TCPOption.GetStaticBox(), wx.ID_ANY, u"Version", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_IPver.Wrap( -1 )
        bSizer15.Add( self.m_staticText_IPver, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_TCPS_VerChoices = [ u"IPV4", u"IPV6" ]
        self.m_comboBox_TCPS_Ver = wx.ComboBox( sbSizer_TCPOption.GetStaticBox(), wx.ID_ANY, u"IPV4", wx.DefaultPosition, wx.DefaultSize, m_comboBox_TCPS_VerChoices, 0 )
        self.m_comboBox_TCPS_Ver.SetSelection( 0 )
        bSizer15.Add( self.m_comboBox_TCPS_Ver, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer_TCPOption.Add( bSizer15, 1, wx.EXPAND, 5 )
        
        
        bSizer11.Add( sbSizer_TCPOption, 0, wx.EXPAND, 5 )
        
        sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_TCP, wx.ID_ANY, u"Loopback Test Mode" ), wx.VERTICAL )
        
        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_checkBox_Loopback_Test = wx.CheckBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Loopback Test", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_checkBox_Loopback_Test, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_InfiniteLoop = wx.CheckBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Infinite Loops", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_checkBox_InfiniteLoop, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_TCP_Loopback_TestStart = wx.Button( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Start Test", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_TCP_Loopback_TestStart.Enable( False )
        
        bSizer17.Add( self.m_button_TCP_Loopback_TestStart, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_TCP_Loopback_TestStop = wx.Button( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Stop Test", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_TCP_Loopback_TestStop.Enable( False )
        
        bSizer17.Add( self.m_button_TCP_Loopback_TestStop, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer12.Add( bSizer17, 1, wx.EXPAND, 5 )
        
        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_Loopback_File = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"File", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Loopback_File.Wrap( -1 )
        bSizer16.Add( self.m_staticText_Loopback_File, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_TCP_FilePath = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl_TCP_FilePath.Enable( False )
        
        bSizer16.Add( self.m_textCtrl_TCP_FilePath, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_TCPFileBrowse = wx.Button( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_TCPFileBrowse.Enable( False )
        
        bSizer16.Add( self.m_button_TCPFileBrowse, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer12.Add( bSizer16, 1, wx.EXPAND, 5 )
        
        
        bSizer11.Add( sbSizer12, 0, wx.EXPAND, 5 )
        
        sbSizerTCPServer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_TCP, wx.ID_ANY, u"TCP Server" ), wx.VERTICAL )
        
        bSizer131 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_TCPS_Port = wx.StaticText( sbSizerTCPServer.GetStaticBox(), wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_TCPS_Port.Wrap( -1 )
        bSizer13.Add( self.m_staticText_TCPS_Port, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_TCPS_Port = wx.TextCtrl( sbSizerTCPServer.GetStaticBox(), wx.ID_ANY, u"5000", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.m_textCtrl_TCPS_Port, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_TCPS_Listen = wx.Button( sbSizerTCPServer.GetStaticBox(), wx.ID_ANY, u"Listen", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.m_button_TCPS_Listen, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_TCPS_Close = wx.Button( sbSizerTCPServer.GetStaticBox(), wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_TCPS_Close.Enable( False )
        
        bSizer13.Add( self.m_button_TCPS_Close, 1, wx.ALL, 5 )
        
        
        bSizer131.Add( bSizer13, 0, wx.EXPAND, 5 )
        
        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
        
        sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( sbSizerTCPServer.GetStaticBox(), wx.ID_ANY, u"Local IP Address List" ), wx.VERTICAL )
        
        self.m_textCtrl_TCPS_LocalIP = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        sbSizer11.Add( self.m_textCtrl_TCPS_LocalIP, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
        
        self.m_textCtrl_TCPS_LocalIPv6 = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        sbSizer11.Add( self.m_textCtrl_TCPS_LocalIPv6, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer14.Add( sbSizer11, 1, 0, 5 )
        
        sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( sbSizerTCPServer.GetStaticBox(), wx.ID_ANY, u"Client Connection Status" ), wx.VERTICAL )
        
        self.m_textCtrl_TCPS_ClientConnectionStatus = wx.TextCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        sbSizer10.Add( self.m_textCtrl_TCPS_ClientConnectionStatus, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer14.Add( sbSizer10, 1, wx.EXPAND, 5 )
        
        
        bSizer131.Add( bSizer14, 0, wx.EXPAND, 5 )
        
        
        sbSizerTCPServer.Add( bSizer131, 0, wx.EXPAND, 5 )
        
        
        bSizer11.Add( sbSizerTCPServer, 0, wx.EXPAND, 5 )
        
        sbSizerTCPClient = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_TCP, wx.ID_ANY, u"TCP Client" ), wx.HORIZONTAL )
        
        self.m_staticText_TargetIP = wx.StaticText( sbSizerTCPClient.GetStaticBox(), wx.ID_ANY, u"Target IP", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_TargetIP.Wrap( -1 )
        sbSizerTCPClient.Add( self.m_staticText_TargetIP, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_TCPC_TargetIP = wx.TextCtrl( sbSizerTCPClient.GetStaticBox(), wx.ID_ANY, u"192.168.0.100", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl_TCPC_TargetIP.Enable( False )
        
        sbSizerTCPClient.Add( self.m_textCtrl_TCPC_TargetIP, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_TCPC_Port = wx.StaticText( sbSizerTCPClient.GetStaticBox(), wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_TCPC_Port.Wrap( -1 )
        sbSizerTCPClient.Add( self.m_staticText_TCPC_Port, 0, wx.ALL, 5 )
        
        self.m_textCtrl_TCPC_Port = wx.TextCtrl( sbSizerTCPClient.GetStaticBox(), wx.ID_ANY, u"5000", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl_TCPC_Port.Enable( False )
        
        sbSizerTCPClient.Add( self.m_textCtrl_TCPC_Port, 1, wx.ALL, 5 )
        
        self.m_button_TCPC_Connect = wx.Button( sbSizerTCPClient.GetStaticBox(), wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_TCPC_Connect.Enable( False )
        
        sbSizerTCPClient.Add( self.m_button_TCPC_Connect, 0, wx.ALL, 5 )
        
        self.m_button_TCPC_Close = wx.Button( sbSizerTCPClient.GetStaticBox(), wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_TCPC_Close.Enable( False )
        
        sbSizerTCPClient.Add( self.m_button_TCPC_Close, 0, wx.ALL, 5 )
        
        
        bSizer11.Add( sbSizerTCPClient, 0, wx.EXPAND, 5 )
        
        sbSizer_TCPScreen = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_TCP, wx.ID_ANY, u"Received/Send data" ), wx.VERTICAL )
        
        self.m_textCtrl_TCPScreen = wx.TextCtrl( sbSizer_TCPScreen.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        sbSizer_TCPScreen.Add( self.m_textCtrl_TCPScreen, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer11.Add( sbSizer_TCPScreen, 1, wx.EXPAND, 5 )
        
        sbSizer_TCPSender = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_TCP, wx.ID_ANY, u"Input Data" ), wx.VERTICAL )
        
        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_textCtrl_TCPSendData = wx.TextCtrl( sbSizer_TCPSender.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_textCtrl_TCPSendData, 1, wx.ALL, 5 )
        
        self.m_button_TCP_Send = wx.Button( sbSizer_TCPSender.GetStaticBox(), wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button_TCP_Send, 0, wx.ALL, 5 )
        
        
        sbSizer_TCPSender.Add( bSizer12, 0, wx.EXPAND, 5 )
        
        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_checkBox_TCP_Hex = wx.CheckBox( sbSizer_TCPSender.GetStaticBox(), wx.ID_ANY, u"Hex", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.m_checkBox_TCP_Hex, 0, wx.ALL, 5 )
        
        self.m_checkBox_AddedCR_LF = wx.CheckBox( sbSizer_TCPSender.GetStaticBox(), wx.ID_ANY, u"CR_LF", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox_AddedCR_LF.SetValue(True) 
        bSizer18.Add( self.m_checkBox_AddedCR_LF, 0, wx.ALL, 5 )
        
        
        sbSizer_TCPSender.Add( bSizer18, 1, wx.EXPAND, 5 )
        
        
        bSizer11.Add( sbSizer_TCPSender, 0, wx.EXPAND, 5 )
        
        
        bSizer91.Add( bSizer11, 1, wx.EXPAND, 5 )
        
        
        self.m_panel_TCP.SetSizer( bSizer91 )
        self.m_panel_TCP.Layout()
        bSizer91.Fit( self.m_panel_TCP )
        self.m_notebook_S2E_TestTool.AddPage( self.m_panel_TCP, u"TCP", True )
        
        bSizer1.Add( self.m_notebook_S2E_TestTool, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_comboBox_SerialComPort.Bind( wx.EVT_LEFT_DOWN, self.onSerialComPort )
        self.m_button_SerialOpen.Bind( wx.EVT_BUTTON, self.onSerialOpen )
        self.m_button_SerialClose.Bind( wx.EVT_BUTTON, self.onSerialClose )
        self.m_textCtrl_SerialScreen.Bind( wx.EVT_CHAR, self.onSerialScreen )
        self.m_textCtrl_SerialLineSender.Bind( wx.EVT_CHAR, self.onSerialLineSender )
        self.m_buttonSerialTextSend.Bind( wx.EVT_BUTTON, self.onSerialTextSend )
        self.m_checkBox_IsTCPServer.Bind( wx.EVT_CHECKBOX, self.onTCPServer )
        self.m_checkBox_IsTCPClient.Bind( wx.EVT_CHECKBOX, self.onIsTCPClient )
        self.m_checkBox_Loopback_Test.Bind( wx.EVT_CHECKBOX, self.onLoopback_Test )
        self.m_button_TCP_Loopback_TestStart.Bind( wx.EVT_BUTTON, self.onTCP_Loopback_TestStart )
        self.m_button_TCP_Loopback_TestStop.Bind( wx.EVT_BUTTON, self.onTCP_Loopback_TestStop )
        self.m_button_TCPFileBrowse.Bind( wx.EVT_BUTTON, self.onTCPFileBrowse )
        self.m_button_TCPS_Listen.Bind( wx.EVT_BUTTON, self.onTCPS_Listen )
        self.m_button_TCPS_Close.Bind( wx.EVT_BUTTON, self.onTCPS_Close )
        self.m_button_TCPC_Connect.Bind( wx.EVT_BUTTON, self.onTCPC_Connect )
        self.m_button_TCPC_Close.Bind( wx.EVT_BUTTON, self.onTCPC_Close )
        self.m_textCtrl_TCPScreen.Bind( wx.EVT_CHAR, self.onTCPScreen )
        self.m_button_TCP_Send.Bind( wx.EVT_BUTTON, self.onTCPSend )

        # User Code
        self.m_ser_IsOpen = False
        self.m_IstcpLoopback_First = False
        self.m_IstcpLoopback_Stop = False
        self.m_tcpLoopback_recv_data = ''
        self.m_tcpTestCnt = 0
        self.m_tcp_client_sock = 0
        self.m_is_run_tcp_server = False
        self.m_is_run_tcp_client = False
        
        pub.subscribe(self.TCPScreen_Recv, 'TCPS_Recv_data')
        pub.subscribe(self.TCPStatus_Recv, 'TCPStatus_Recv')

        self.GetComPortList()
        host = socket.gethostname()
        ip_address_list = socket.getaddrinfo(host, None, socket.AF_INET)
        
        for ip_address in ip_address_list:
            self.m_textCtrl_TCPS_LocalIP.AppendText(ip_address[4][0])
            self.m_textCtrl_TCPS_LocalIP.AppendText('\r\n')
        
        ip_address_list = socket.getaddrinfo(host, None, socket.AF_INET6)
        
        for ip_address in ip_address_list:
            self.m_textCtrl_TCPS_LocalIPv6.AppendText(ip_address[4][0])
            self.m_textCtrl_TCPS_LocalIPv6.AppendText('\r\n')
        
    def __del__( self ):
        if self.m_ser_IsOpen == True:
            self.m_ser_recv_run_event.clear()
            self.m_ser.close()
        else:
            self.m_tcp_client_sock.close()
        
     
    def GetComPortList(self):
        comboBox_serial_portChoices = []
         
        self.available_ports = list(serial.tools.list_ports.comports())
        for self.port in self.available_ports:
            if(self.port[2] != 'n/a'):
                comboBox_serial_portChoices.append(self.port[0])
                  
        self.m_comboBox_SerialComPort.SetItems(comboBox_serial_portChoices)
         
    #***************For Thread***************
    # This is main function in Recv Thread
    def SerialRecv(self, run_event):
        self.m_textCtrl_SerialScreen.Clear()
        while run_event.is_set():
            recv_data = self.m_ser.read(1024)
            if len(recv_data) > 0:
                lock.acquire()
                output_msg = recv_data
                wx.CallAfter(self.m_textCtrl_SerialScreen.AppendText,output_msg)
                lock.release()
            else:
                time.sleep(0.01)
    

    def TCPScreen_Recv(self, data):
        if self.m_checkBox_Loopback_Test.GetValue() == False:
            cv.acquire()
            wx.CallAfter(self.m_textCtrl_TCPScreen.AppendText,data)
            cv.release()
        else:
            cv.acquire()
            if self.m_IstcpLoopback_First == True:
                self.m_TcpRecvStartTime = int(round(time.time()*1000))
                self.TcpRecvDialog = wx.ProgressDialog('TCP Loopback Test','Recv Data & Speed', self.m_tcpFileSize,
                                                       style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
                self.m_tcpLoopback_recv_data = data
                self.m_IstcpLoopback_First = False
            else:
                self.m_tcpLoopback_recv_data += data

            recved_size = len(self.m_tcpLoopback_recv_data)
            if recved_size >= self.m_tcpFileSize:
                self.m_tcpTestCnt +=1
                self.TcpRecvDialog.Destroy()
                
                # Calculate test time and speed
                self.m_TcpRecvEndTime = int(round(time.time()*1000)) - self.m_TcpRecvStartTime
                speed = float((recved_size * 8) / self.m_TcpRecvEndTime)
                
                # File Compare
                recv_file = open("recv_data.log","wb")
                recv_file.write(self.m_tcpLoopback_recv_data)
                recv_file.close()
                result = filecmp.cmp(self.m_textCtrl_TCP_FilePath.GetValue(), "recv_data.log")

                # Print test information
                output_string = "[Test %d] time : %dms, data len : %d speed %.2fK bps\r\n" %(self.m_tcpTestCnt, self.m_TcpRecvEndTime, recved_size, speed)
                wx.CallAfter(self.m_textCtrl_TCPScreen.AppendText,output_string)

                message = "Test Result(File Compare) : %s\r\n" % str(result)
                wx.CallAfter(self.m_textCtrl_TCPScreen.AppendText,message)  
                
                cv.notify()
            else:
                self.TcpRecvDialog.Update(recved_size)
            cv.release()
    
    def TCPStatus_Recv(self, data):
        lock.acquire()
        wx.CallAfter(self.m_textCtrl_TCPS_ClientConnectionStatus.AppendText,data)
        lock.release()
        
    #****************************************
            

    # Virtual event handlers, overide them in your derived class
    def onSerialComPort( self, event ):
        self.GetComPortList()
        event.Skip()
     
    def onSerialOpen( self, event ):
        self.m_port = self.m_comboBox_SerialComPort.GetValue()
        self.m_baudrate = int(self.m_comboBox_SerialBuad.GetValue())
        self.m_bytesize = int(self.m_comboBox_SerialDataSize.GetValue())
        self.m_parity = self.m_comboBox_Parity.GetValue()[0]
        self.m_stopbits = float(self.m_comboBox_SerialStopbits.GetValue())
        if   self.m_comboBox_Handshake.GetValue() == "OFF": 
            self.m_xonxoff = False
            self.m_rtscts = False
        elif self.m_comboBox_Handshake.getValue() == "RTS/CTS": 
            self.m_xonxoff = False
            self.m_rtscts = True
        elif self.m_comboBox_Handshake.GetValue() == "Xon/Xoff": 
            self.m_xonxoff = True
            self.m_rtscts = False
         
        if self.m_port == '':
            wx.MessageBox("Please Select Serial Port", 'Warning', wx.OK | wx.ICON_ERROR)
            return
         
        self.m_ser = serial.Serial(self.m_port, self.m_baudrate, timeout = 0.1, bytesize = self.m_bytesize, 
                                   parity = self.m_parity, stopbits = self.m_stopbits, xonxoff = self.m_xonxoff, rtscts = self.m_rtscts)
         
        if self.m_ser == -1:
            self.m_ser.close()
            wx.MessageBox("Serial Open Error.\r\n", 'Warning', wx.OK | wx.ICON_ERROR)
            return
         
        self.m_ser_recv_run_event = threading.Event()
        self.m_ser_recv_run_event.set()
        self.m_Ser_RecvThread = threading.Thread(target = self.SerialRecv, args = (self.m_ser_recv_run_event,))
        self.m_Ser_RecvThread.start()
         
        self.m_button_SerialOpen.Disable()
        self.m_button_SerialClose.Enable()
        self.m_textCtrl_SerialInputText.Enable()
        self.m_textCtrl_SerialLineSender.Enable()
        self.m_textCtrl_SerialScreen.Enable()
        self.m_buttonSerialTextSend.Enable()
        self.m_ser_IsOpen = True

     
    def onSerialClose( self, event ):
        if self.m_ser_IsOpen == True:
            self.m_ser_recv_run_event.clear()
            self.m_ser.close()

            self.m_button_SerialOpen.Enable()
            self.m_button_SerialClose.Disable()
            self.m_textCtrl_SerialInputText.Disable()
            self.m_textCtrl_SerialLineSender.Disable()
            self.m_textCtrl_SerialScreen.Disable()
            self.m_buttonSerialTextSend.Disable()

            self.m_ser_IsOpen = False
            
 
    def onSerialScreen( self, event ):
        lock.acquire()
        key = event.GetKeyCode()
        if key > 256:
            lock.release()
            return
 
        self.m_ser.write(chr(key))
        lock.release()

    def onSerialLineSender( self, event ):
        key = event.GetKeyCode()
        if event.HasModifiers():
            if key == wx.WXK_RETURN:
                curPos = self.m_textCtrl_SerialLineSender.GetInsertionPoint()
                lineNum = len(self.m_textCtrl_SerialLineSender.GetRange(0, self.m_textCtrl_SerialLineSender.GetInsertionPoint() ).split("\n") ) - 1
                lineText = self.m_textCtrl_SerialLineSender.GetLineText(lineNum) + "\r\n"
                self.m_textCtrl_SerialLineSender.SetInsertionPoint(curPos + len(lineText) - 1)
                self.m_ser.write(lineText)
                return

        event.Skip()
            
    def onSerialTextSend( self, event ):
        loop_cnt = 0 
        
        cmd = self.m_textCtrl_SerialInputText.GetValue()
        words = cmd.split('$')
        for word in words:
            if cmd.find('$') == 0 or loop_cnt > 0:
                word_len = len(word)
                if word_len == 0:
                    wx.MessageBox("", 'Warning', wx.OK | wx.ICON_ERROR)
                    return
                 
                hex_data = word[0:2]
                self.m_ser.write(hex_data.decode("hex"))
                if word_len > 2:
                    self.m_ser.write(word[2:])
            else:
                self.m_ser.write(word)
                 
            loop_cnt += 1

    def onTCPServer( self, event ):
        self.m_checkBox_IsTCPServer.SetValue(True)
        self.m_checkBox_IsTCPClient.SetValue(False)
        self.m_textCtrl_TCPS_Port.Enable()
        self.m_button_TCPS_Listen.Enable()
        self.m_button_TCPS_Close.Disable()
        self.m_textCtrl_TCPS_ClientConnectionStatus.Enable()
        self.m_textCtrl_TCPS_LocalIP.Enable()
        self.m_textCtrl_TCPS_LocalIPv6.Enable()
        
        self.m_textCtrl_TCPC_TargetIP.Disable()
        self.m_textCtrl_TCPC_Port.Disable()
        self.m_button_TCPC_Connect.Disable()
        self.m_button_TCPC_Close.Disable()
        
    def onIsTCPClient( self, event ):
        self.m_checkBox_IsTCPServer.SetValue(False)
        self.m_checkBox_IsTCPClient.SetValue(True)
        self.m_textCtrl_TCPS_Port.Disable()
        self.m_button_TCPS_Listen.Disable()
        self.m_button_TCPS_Close.Disable()
        self.m_textCtrl_TCPS_ClientConnectionStatus.Disable()
        self.m_textCtrl_TCPS_LocalIP.Disable()
        self.m_textCtrl_TCPS_LocalIPv6.Disable()
        
        self.m_textCtrl_TCPC_TargetIP.Enable()
        self.m_textCtrl_TCPC_Port.Enable()
        self.m_button_TCPC_Connect.Enable()
        self.m_button_TCPC_Close.Disable()
        
        
    def onLoopback_Test( self, event ):
        if self.m_checkBox_Loopback_Test.GetValue() == True:
            self.m_textCtrl_TCPSendData.Disable()
            self.m_button_TCP_Send.Disable()
            self.m_textCtrl_TCP_FilePath.Enable()
            self.m_button_TCPFileBrowse.Enable()
            self.m_button_TCP_Loopback_TestStart.Enable()
        else:
            self.m_textCtrl_TCPSendData.Enable()
            self.m_button_TCP_Send.Enable()
            self.m_textCtrl_TCP_FilePath.Disable()
            self.m_button_TCPFileBrowse.Disable()
            self.m_button_TCP_Loopback_TestStart.Disable()

    def onTCPFileBrowse( self, event ):
        filename = ''
        dlg = wx.FileDialog(self, message='Choose a file')
        
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
        dlg.Destroy()
        
        if filename:
            self.m_textCtrl_TCP_FilePath.SetValue(filename)

    def onTCP_Loopback_TestStart( self, event ):
        if self.m_checkBox_InfiniteLoop.GetValue() == True:
            self.m_tcpTestCnt = 0
            self.m_button_TCP_Loopback_TestStart.Disable()
            self.m_button_TCP_Loopback_TestStop.Enable()
            self.TCPLoopback_Infinite = TCPLoopback_Infinite(self)
        else:
            self.m_tcpFileName = self.m_textCtrl_TCP_FilePath.GetValue()
            if self.m_tcpFileName == '':
                return
            
            self.m_tcpFileSize = os.stat(self.m_tcpFileName).st_size
            file_data = ""
            send_file = open(self.m_tcpFileName,'rb')
            for i in xrange(0,self.m_tcpFileSize,1024):
                data = send_file.read(1024)
                file_data += data
            send_file.close()

            lock.acquire()
            self.m_IstcpLoopback_First = True
            try:
                for i in xrange(0,self.m_tcpFileSize,1024):
                    send_data = file_data[i:i+1024]
                    
                    if self.m_checkBox_IsTCPServer.GetValue() == True:
                        wx.CallAfter(pub.sendMessage,'TCPS_Send_Data',data=send_data)
                    elif self.m_checkBox_IsTCPClient.GetValue() == True:
                        self.m_tcp_client_sock.sendall(send_data)
                    
            except Exception as e:
                s = str(e)
                wx.MessageBox(s, 'Warning', wx.OK | wx.ICON_ERROR)
            lock.release()

    def onTCP_Loopback_TestStop( self, event ):
        self.m_IstcpLoopback_Stop = True
        self.TCPLoopback_Infinite.stop()
        self.m_button_TCP_Loopback_TestStart.Enable()
        self.m_button_TCP_Loopback_TestStop.Disable()

    
    def onTCPS_Listen( self, event ):
        tcpServerPort = int(self.m_textCtrl_TCPS_Port.GetValue())

        if self.m_comboBox_TCPS_Ver.GetValue() == 'IPV4':
            tcpServer.ThreadedTCPServer.allow_reuse_address = True
            tcpServer.ThreadedTCPServer.address_family = socket.AF_INET
        else:
            tcpServer.ThreadedTCPServer.allow_reuse_address = True
            tcpServer.ThreadedTCPServer.address_family = socket.AF_INET6

        self.tcp_server = tcpServer.ThreadedTCPServer(('',tcpServerPort), tcpServer.TCPServerHandler)
        self.server_thread = threading.Thread(target=self.tcp_server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
            
        self.m_is_run_tcp_server = True
        self.m_textCtrl_TCPScreen.Clear()
        self.m_button_TCPS_Listen.Enable(False)
        self.m_button_TCPS_Close.Enable(True)
        if self.m_checkBox_Loopback_Test.GetValue() == True: self.m_button_TCP_Loopback_TestStart.Enable(True)

        
    def onTCPS_Close( self, event ):
        if self.m_button_TCP_Loopback_TestStop.IsEnabled():
            self.onTCP_Loopback_TestStop(None)
        
        self.tcp_server.shutdown()
        self.tcp_server.server_close()

        wx.CallAfter(pub.sendMessage,'TCPS_Close_Request')
        
        self.m_button_TCPS_Listen.Enable(True)
        self.m_button_TCPS_Close.Enable(False)
        self.m_button_TCP_Loopback_TestStart.Enable(False)
        self.m_is_run_tcp_server = False
        
    
    def onTCPC_Connect( self, event ):
        if self.m_comboBox_TCPS_Ver.GetValue() == 'IPV4':
            self.m_tcp_client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.m_tcp_client_sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        
        self.m_tcp_client_sock.settimeout(0.5)
        server_address = (str(self.m_textCtrl_TCPC_TargetIP.GetValue()), int(self.m_textCtrl_TCPC_Port.GetValue()) )
        try:
            self.m_tcp_client_sock.connect(server_address)
        except socket.timeout:
            wx.MessageBox("Fail to connection. Please check IP address of server", 'Warning', wx.OK | wx.ICON_ERROR)
            return
        

        self.m_button_TCPC_Close.Enable()
        self.m_button_TCPC_Connect.Disable()
        self.m_is_run_tcp_client = True
        
        self.m_TCPC_RecvThread = TCPC_RecvThread(self)
    
    def onTCPC_Close( self, event ):
        if self.m_button_TCP_Loopback_TestStop.IsEnabled():
            self.onTCP_Loopback_TestStop(None)

        self.m_TCPC_RecvThread.stop()
        
        self.m_tcp_client_sock.close()
        self.m_button_TCPC_Close.Disable()
        self.m_button_TCPC_Connect.Enable()
    
    def onTCPScreen( self, event ):
        event.Skip()
    
    def onTCPSend( self, event ):
        message = self.m_textCtrl_TCPSendData.GetValue()
        if self.m_checkBox_AddedCR_LF.GetValue() == True:
            message = message + "\r\n"
        
        if self.m_checkBox_IsTCPServer.GetValue() == True:
            cv.acquire()
            wx.CallAfter(pub.sendMessage,'TCPS_Send_Data',data=message)
            cv.release()

        elif self.m_checkBox_IsTCPClient.GetValue() == True:
            cv.acquire()
            self.m_tcp_client_sock.sendall(message)
            cv.release()
                
if __name__ == "__main__":
    app = wx.App(0)
    s2e_test_tool = Serial2Ethernet_Test_Tool(None)
    app.SetTopWindow(s2e_test_tool)
    s2e_test_tool.Show()
    app.MainLoop()
