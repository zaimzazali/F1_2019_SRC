from dataRetriever import DataRetriever

class main():
    def __init__(self):
        prev_data = None

        _DataReceiver = DataRetriever() # Will create another Thread

        while _DataReceiver.getToProceed():
            data = _DataReceiver.getUDPdata()

            if _DataReceiver.getToProceed():
                data = _DataReceiver.getUDPdata()
                try:
                    if (data != prev_data):
                        print(data) 

                        prev_data = data
                except:
                    pass
            else:
                _DataReceiver.stopIterate()

     
        
if __name__ == "__main__":
    main()
