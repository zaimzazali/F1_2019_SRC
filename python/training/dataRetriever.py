import socket
import threading
from f1_2019_telemetry.packets import unpack_udp_packet

class DataRetriever:
    packet = None
    toProceed = True
    hadFlow = False

    def getUDPdata(self):
        return self.packet

    def stopIterate(self):
        self.toProceed = False

    def getToProceed(self):
        return self.toProceed

    def startStreamData(self):
        initial_timeout = 10
        altered_timeout = 0.5
        try:
            # Open and Connect to Socket
            udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            udp_socket.bind(('', 20777))
            udp_socket.settimeout(initial_timeout) # Try for few seconds

            # Get the Data
            while self.toProceed:
                udp_packet = udp_socket.recv(2048)
                self.packet = unpack_udp_packet(udp_packet)
                self.hadFlow = True
                udp_socket.settimeout(altered_timeout) # Instantly stop

        except socket.timeout as e:
            self.stopIterate()
            if (self.hadFlow):
                print('\nERROR startStreamData(): Data stop flowing!')
            elif (self.packet == None):
                print('ERROR startStreamData():', e)
            


    def __init__(self):
        print("DataRetriever Instantiated!")
        try:
            th1 = threading.Thread(target=self.startStreamData)
            th1.start()
        except Exception as e:
            print('Exception:', e, '\nERROR: Unable to start streaming thread!')
