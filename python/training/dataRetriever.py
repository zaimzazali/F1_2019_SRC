import socket
import threading
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

    def startStreamData(self):
        initial_timeout = 10
        altered_timeout = 0.5
        try:
            # Open and Connect to Socket
            udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            udp_socket.bind(('', 20777))
            udp_socket.settimeout(initial_timeout) # Try for few seconds

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
