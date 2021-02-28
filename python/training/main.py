from dataRetriever import DataRetriever
from envDataObserver import EnvDataObserver
from trainer import Trainer

class main():
    def __init__(self):
        __prev_data = None

        __DataReceiver = DataRetriever() # Will create another Thread
        __EnvDataObserver = EnvDataObserver() 
        __Trainer = Trainer() 

        while __DataReceiver.getToProceed():
            __data = __DataReceiver.getUDPdata()

            if __DataReceiver.getToProceed():
                __data = __DataReceiver.getUDPdata()
                try:
                    if (__data != __prev_data):
                        __EnvDataObserver.setData(__data)
                        __prev_data = __data
                except:
                    pass
            else:
                __DataReceiver.stopIterate()

     
        
if __name__ == "__main__":
    main()
