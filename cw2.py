class TV:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 244
class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "8k"
class SmartPhone(Display, TV):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)
iphone = SmartPhone(model ="Best")
iphone.print_info()