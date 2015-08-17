# -*- coding: utf-8 -*- 
 
###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
 
import wx
import wx.xrc
import serial
import serial.tools.list_ports
import threading
import wx.lib.newevent
import time
import sys
 
 
lock = threading.Lock()
 
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
        
        self.m_staticText_SerialComport = wx.StaticText( self.m_panel_Serial, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_SerialComport.Wrap( -1 )
        bSizer7.Add( self.m_staticText_SerialComport, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_SerialComPortChoices = []
        self.m_comboBox_SerialComPort = wx.ComboBox( self.m_panel_Serial, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_SerialComPortChoices, 0 )
        bSizer7.Add( self.m_comboBox_SerialComPort, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_SerialBuad = wx.StaticText( self.m_panel_Serial, wx.ID_ANY, u"Baud", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_SerialBuad.Wrap( -1 )
        bSizer7.Add( self.m_staticText_SerialBuad, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_SerialBuadChoices = [ u"2400", u"9600", u"14400", u"19200", u"38400", u"57600", u"76800", u"115200", u"230400", u"460800" ]
        self.m_comboBox_SerialBuad = wx.ComboBox( self.m_panel_Serial, wx.ID_ANY, u"115200", wx.DefaultPosition, wx.DefaultSize, m_comboBox_SerialBuadChoices, 0 )
        bSizer7.Add( self.m_comboBox_SerialBuad, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_SerialDataSize = wx.StaticText( self.m_panel_Serial, wx.ID_ANY, u"Data size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_SerialDataSize.Wrap( -1 )
        bSizer7.Add( self.m_staticText_SerialDataSize, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_SerialDataSizeChoices = [ u"5", u"6", u"7", u"8" ]
        self.m_comboBox_SerialDataSize = wx.ComboBox( self.m_panel_Serial, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, m_comboBox_SerialDataSizeChoices, 0 )
        bSizer7.Add( self.m_comboBox_SerialDataSize, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer_SerialConfiguartion.Add( bSizer7, 0, wx.ALL|wx.EXPAND, 5 )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_Parity = wx.StaticText( self.m_panel_Serial, wx.ID_ANY, u"Parity", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Parity.Wrap( -1 )
        bSizer5.Add( self.m_staticText_Parity, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_ParityChoices = [ u"None", u"Even", u"Odd", u"Mark", u"Space" ]
        self.m_comboBox_Parity = wx.ComboBox( self.m_panel_Serial, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, m_comboBox_ParityChoices, 0 )
        bSizer5.Add( self.m_comboBox_Parity, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_Handshake = wx.StaticText( self.m_panel_Serial, wx.ID_ANY, u"Handshake", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Handshake.Wrap( -1 )
        bSizer5.Add( self.m_staticText_Handshake, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_HandshakeChoices = [ u"OFF", u"RTS/CTS", u"Xon/Xoff" ]
        self.m_comboBox_Handshake = wx.ComboBox( self.m_panel_Serial, wx.ID_ANY, u"OFF", wx.DefaultPosition, wx.DefaultSize, m_comboBox_HandshakeChoices, 0 )
        bSizer5.Add( self.m_comboBox_Handshake, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_SerialStopbits = wx.StaticText( self.m_panel_Serial, wx.ID_ANY, u"Stop Bits", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_SerialStopbits.Wrap( -1 )
        bSizer5.Add( self.m_staticText_SerialStopbits, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_SerialStopbitsChoices = [ u"1", u"1.5", u"2" ]
        self.m_comboBox_SerialStopbits = wx.ComboBox( self.m_panel_Serial, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, m_comboBox_SerialStopbitsChoices, 0 )
        bSizer5.Add( self.m_comboBox_SerialStopbits, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer_SerialConfiguartion.Add( bSizer5, 0, wx.ALL|wx.EXPAND, 5 )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button_SerialOpen = wx.Button( self.m_panel_Serial, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_button_SerialOpen, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_SerialClose = wx.Button( self.m_panel_Serial, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_SerialClose.Enable( False )
        
        bSizer10.Add( self.m_button_SerialClose, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer_SerialConfiguartion.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        
        bSizer2.Add( sbSizer_SerialConfiguartion, 0, wx.ALL|wx.EXPAND, 5 )
        
        sbSizer_SerialScreen = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_Serial, wx.ID_ANY, u"Received/Send data" ), wx.VERTICAL )
        
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_textCtrl_SerialScreen = wx.TextCtrl( self.m_panel_Serial, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_textCtrl_SerialScreen.SetMaxLength( 102400 ) 
        self.m_textCtrl_SerialScreen.Enable( False )
        
        bSizer8.Add( self.m_textCtrl_SerialScreen, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        sbSizer_SerialScreen.Add( bSizer8, 1, wx.EXPAND|wx.ALL, 5 )
        
        
        bSizer2.Add( sbSizer_SerialScreen, 1, wx.EXPAND|wx.ALL, 5 )
        
        sbSizerSerialLineSender = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_Serial, wx.ID_ANY, u"Line Sender" ), wx.VERTICAL )
        
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_textCtrl_SerialLineSender = wx.TextCtrl( self.m_panel_Serial, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_textCtrl_SerialLineSender.Enable( False )
        
        bSizer9.Add( self.m_textCtrl_SerialLineSender, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        sbSizerSerialLineSender.Add( bSizer9, 1, wx.EXPAND|wx.ALL, 5 )
        
        
        bSizer2.Add( sbSizerSerialLineSender, 1, wx.EXPAND|wx.ALL, 5 )
        
        sbSizerSerialTextSender = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_Serial, wx.ID_ANY, u"Input Data" ), wx.VERTICAL )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_textCtrl_SerialInputText = wx.TextCtrl( self.m_panel_Serial, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl_SerialInputText.Enable( False )
        
        bSizer10.Add( self.m_textCtrl_SerialInputText, 1, wx.ALL, 5 )
        
        self.m_buttonSerialTextSend = wx.Button( self.m_panel_Serial, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonSerialTextSend.Enable( False )
        
        bSizer10.Add( self.m_buttonSerialTextSend, 0, wx.ALL, 5 )
        
        
        sbSizerSerialTextSender.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        
        bSizer2.Add( sbSizerSerialTextSender, 0, wx.EXPAND|wx.ALL, 5 )
        
        
        self.m_panel_Serial.SetSizer( bSizer2 )
        self.m_panel_Serial.Layout()
        bSizer2.Fit( self.m_panel_Serial )
        self.m_notebook_S2E_TestTool.AddPage( self.m_panel_Serial, u"Serial", True )
        self.m_panel_TCP = wx.Panel( self.m_notebook_S2E_TestTool, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_notebook_S2E_TestTool.AddPage( self.m_panel_TCP, u"TCP", False )
        
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
    
        # User Code
        self.m_ser_IsOpen = False
        self.GetComPortList()
        
         
    def __del__( self ):
        if self.m_ser_IsOpen == True:
            self.m_ser_recv_run_event.clear()
            self.m_ser.close()
     
    def GetComPortList(self):
        comboBox_serial_portChoices = []
         
        self.available_ports = list(serial.tools.list_ports.comports())
        for self.port in self.available_ports:
            if(self.port[2] != 'n/a'):
                comboBox_serial_portChoices.append(self.port[0])
                  
        self.m_comboBox_SerialComPort.SetItems(comboBox_serial_portChoices)
         
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
                
if __name__ == "__main__":
    app = wx.App(0)
    s2e_test_tool = Serial2Ethernet_Test_Tool(None)
    app.SetTopWindow(s2e_test_tool)
    s2e_test_tool.Show()
    app.MainLoop()
