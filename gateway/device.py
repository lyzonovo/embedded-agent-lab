import json
class Device:
    def __init__(self, device_id):
        self.device_id = device_id
        self.temperature = 0
        self.voltage = 0
        self.current = 0
        self.speed = 0
        self.status = "NORMAL"
    def update_status(self):
            if self.temperature>=70:
                  self.status="over_temp"
            else:
                  self.status="normal"
    def to_dict(self):
        return{
               "device_id": self.device_id,
                "temperature": self.temperature,
                "voltage": self.voltage,
                "current": self.current,
                "speed": self.speed,
                "status": self.status     
        }
    
device = Device(1)
device.temperature = 69.5
device.voltage = 12.1
device.current = 1.8
device.speed = 1200
device.update_status()
print(json.dumps(device.to_dict(), indent=4))


