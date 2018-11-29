# coding: utf8
import os
from os.path import expanduser
from hermes_python.hermes import Hermes
import subprocess
import serial
import serial.tools.list_ports
import sys
import time
import warnings



class Robot:
    @classmethod
    def __init__(self):
        arduino_ports = [
                    p.device
                        for p in serial.tools.list_ports.comports()
                        for x in range (0, 10)
                        if 'ttyUSB%d' % x  in p.name or "ttyACM%d" % x in p.name]
        if not arduino_ports:
                raise IOError("No Arduino found")
        if len(arduino_ports) > 1:
                warnings.warn('Multiple Arduinos found - using the first')
        self.ser = serial.Serial(
                            port=arduino_ports[0],
                            baudrate = 9600
                        )

    @classmethod
    def left(self):
        #while 1:
        print "robot left"
        self.ser.write('B%dE\n'%(2))
       # time.sleep(5)

    def right(self):
       print "robot right"
       self.ser.write('B%dE\n'%(1))

    def up(self):
        print "robot face up"
        self.ser.write('B%dE\n'%(4))

    def down(self):
        print "robot face down"
        self.ser.write('B%dE\n'%(3))

   # def fine(self):
    #    print "robot I am fine"
       # result_sentence="I am fine thank you and how are you"
       # current_session_id=intentMessage.session_id
       # hermes.publish_end_session(result_sentence)

    

if (__name__ == "__main__"):
    c = Robot()
    c.left()
    c.right()
    c.up()
    c.down()
   # c.fine()

