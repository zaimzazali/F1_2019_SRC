import socket
import threading
from f1_2019_telemetry.packets import unpack_udp_packet

class DataRetriever:
    packet = None
    toProceed = True

    def getUDPdata(self):
        return self.packet

    def stopIterate(self):
        self.toProceed = False

    def startStreamData(self):
        try:
            # Open and Connect to Socket
            udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            udp_socket.bind(('', 20777))
            udp_socket.settimeout(5)

            # Get the Data
            while self.toProceed:
                udp_packet = udp_socket.recv(2048)
                self.packet = unpack_udp_packet(udp_packet)
                # print("Data received!")

                if (not self.toProceed):
                    break

        except socket.timeout as e:
            print('ERROR:', e)
            self.stopIterate()

    def __init__(self):
        print("DataRetriever Instantiated!")

        try:
            th1 = threading.Thread(target=self.startStreamData)
            th1.start()
        except Exception as e:
            print('Exception:', e, '\nERROR: Unable to start streaming thread!')
