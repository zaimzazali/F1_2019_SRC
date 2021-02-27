import threading
import sys
from pynput import keyboard

class KeyboardListener():
    toTerminate = None

    def getToTerminate(self):
        return self.toTerminate

    def toTerminateProgram(self):
        # print('<ctrl>+q pressed')
        self.toTerminate = True
        sys.exit(0)

    def startListening(self):
        with keyboard.GlobalHotKeys({'<ctrl>+q': self.toTerminateProgram}) as listener:
            listener.join()    

    def __init__(self):
        print("KeyboardListener Instantiated!")

        try:
            th1 = threading.Thread(target=self.startListening)
            th1.start()
        except Exception as e:
            print('Exception:', e, '\nERROR: Unable to start keyboard thread!')

        
