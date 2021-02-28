from dataRetriever import DataRetriever
from envDataObserver import EnvDataObserver

class main():
    def __init__(self):
        __prev_data = None

        __DataReceiver = DataRetriever() # Will create another Thread
        __EnvDataObserver = EnvDataObserver() # Will create another Thread

        while __DataReceiver.getToProceed():
            data = __DataReceiver.getUDPdata()

            if __DataReceiver.getToProceed():
                data = __DataReceiver.getUDPdata()
                try:
                    if (data != __prev_data):
                        print(data) 

                        __prev_data = data
                except:
                    pass
            else:
                __DataReceiver.stopIterate()

     
        
if __name__ == "__main__":
    main()
