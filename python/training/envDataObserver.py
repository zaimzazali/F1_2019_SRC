class EnvDataObserver:
    '''
    All packet data can be referred to: https://forums.codemasters.com/topic/44592-f1-2019-udp-specification/
    Only few selected data will be used, as of now.
    '''

    class MotionPacket:
        def __init__(self): 
            pass

    class SessionPacket:
        def __init__(self): 
            pass

    class LapDataPacket:
        def __init__(self): 
            pass

    class CarTelemetryPacket:
        def __init__(self): 
            pass

    class CarStatusPacket:
        def __init__(self): 
            pass



    def setData(self, myData):
        pass

    def getDataObject(self):
        return self



    def __init__(self):
        print('EnvDataObserver Instantiated!')
        self.Motion = self.MotionPacket()
        self.Session = self.SessionPacket()
        self.LapData = self.LapDataPacket()
        self.CarTelemetry = self.CarTelemetryPacket()
        self.CarStatus = self.CarStatusPacket()
