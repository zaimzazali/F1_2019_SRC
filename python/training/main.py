import threading
from dataRetriever import DataRetriever
from keyboardListener import KeyboardListener

class main():
    def __init__(self):
        _DataReceiver = DataRetriever()
        _KeyboardListener = KeyboardListener()

        toProceed = not _KeyboardListener.getToTerminate()
        while toProceed:
            toProceed = not _KeyboardListener.getToTerminate()
            if toProceed:
                data = _DataReceiver.getUDPdata()
                try:
                    print(data) 
                except:
                    pass
            else:
                _DataReceiver.stopIterate()

        

if __name__ == "__main__":
    main()
