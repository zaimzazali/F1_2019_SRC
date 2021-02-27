import socket
from f1_2019_telemetry.packets import unpack_udp_packet

class DataRetriever:
    def __init__(self):
        try:
            udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            udp_socket.bind(('', 20777))
            udp_socket.settimeout(10) # To wait for 10 seconds

            while True:
                udp_packet = udp_socket.recv(2048)
                packet = unpack_udp_packet(udp_packet)
                print("Received:", packet)
                print()
                
        except:
            print("No data received!")
            print()
        