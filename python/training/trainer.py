from envDataObserver import EnvDataObserver

class Trainer:
    __envDataObject = None

    def __init__(self):
        print('Trainer Instantiated!')
        self.__envDataObject = EnvDataObserver.getDataObject(self.__envDataObject)
