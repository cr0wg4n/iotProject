#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial, time, threading

class Connect():

    connect = None
    def __init__(self, port):
        self.__connect = serial.Serial(port,9600)

    def getData(self):
        try:
            data = self.__connect.readline().decode("utf-8").strip()
            return data

        except serial.SerialException as e:
            print("error read data", e.strerror)

    def sendData(self, message):

        try:
            print message

            self.__connect.write(str(message))

        except serial.SerialException as e:
            print("error write data ",e.strerror)

    def setData(self, message):
        hilo = threading.Thread( target=self.sendData, args=(message, ) )
        hilo.start()
        print "termino"



    @staticmethod
    def getInstance(port):

        if Connect.connect == None:
            Connect.connect = Connect(port)

        return Connect.connect


class Information():

    information = None

    def __init__(self):

        self.__serial = Connect.getInstance("/dev/ttyACM0")
        self.data = None
        self.data1 = None
        self.data2 = None

        self.theadP = threading.Thread(target=self.theadingInf)
        self.theadP.setDaemon(True)
        self.theadP.start()

    def theadingInf(self):

        while True:
            datosAr = self.__serial.getData().split('_')

            self.data = datosAr[0]
            self.data1 = datosAr[1]
            self.data2 = datosAr[2]
            self.data3 = datosAr[3]

            time.sleep(0.06)

    @staticmethod

    def getInstance():

        if Information.information == None:
            Information.information = Information()

        return Information.information

