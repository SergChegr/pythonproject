# class Grandparent:
#     def about(self):
#         print("I am GrandParent")
#         def about_myself(self):
#             print("I am Grandparent")
# class Parent(Grandparent):
#     def about_myself(self):
#         print("I am Parent")
# class Child(Parent):
#     def __init__(self):
#         super().about()
#         super().about_myself()
# nick = Child()
class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128
class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4k"
class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)
iphone = SmartPhone(model ="Last")
iphone.print_info()