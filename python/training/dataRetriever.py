import socket
import threading
import time 
from f1_2019_telemetry.packets import unpack_udp_packet

class DataRetriever:
    __packet = None
    __toProceed = True
    __hadFlow = False

    def getUDPdata(self):
        return self.__packet

    def stopIterate(self):
        self.__toProceed = False

    def getToProceed(self):
        return self.__toProceed

    def startCountdown(self, myTiming):
        while myTiming >= 0 and not self.__hadFlow: 
            timerStr = 'Trying to get the data... {:02d} to timeout'.format(myTiming) 
            if (myTiming < 1):
                print(timerStr) 
            else:
                print(timerStr, end="\r") 
            time.sleep(1) 
            myTiming -= 1

    def startStreamData(self):
        initial_timeout = 10
        altered_timeout = 0.5
        try:
            # Open and Connect to Socket
            udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            udp_socket.bind(('', 20777))
            udp_socket.settimeout(initial_timeout + 1) # Try for few seconds

            # Start the timeout countdown
            print()
            __th2 = threading.Thread(target=self.startCountdown, args=(initial_timeout,))
            __th2.start()

            # Get the Data
            while self.__toProceed:
                udp_packet = udp_socket.recv(2048)
                self.__packet = unpack_udp_packet(udp_packet)
                self.__hadFlow = True
                udp_socket.settimeout(altered_timeout) # Instantly stop

        except socket.timeout as e:
            self.stopIterate()
            if (self.__hadFlow):
                print('\nERROR startStreamData(): Data stop flowing!')
            elif (self.__packet == None):
                print('ERROR startStreamData():', e)
            


    def __init__(self):
        print('DataRetriever Instantiated!')
        try:
            __th1 = threading.Thread(target=self.startStreamData)
            __th1.start()
        except Exception as e:
            print('Exception:', e, '\nERROR: Unable to start streaming thread!')
