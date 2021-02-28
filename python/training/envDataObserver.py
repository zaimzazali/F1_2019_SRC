class EnvDataObserver:
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



    def __init__(self):
        print("EnvDataObserver Instantiated!")
        self.Motion = self.MotionPacket()
        self.Session = self.SessionPacket()
        self.LapData = self.LapDataPacket()
        self.CarTelemetry = self.CarTelemetryPacket()
        self.CarStatus = self.CarStatusPacket()
