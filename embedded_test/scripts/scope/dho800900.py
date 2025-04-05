import pyvisa
print(pyvisa.__version__)

class Dho800900:



    def __init__(self, arg_model, arg_name, arg_ip_address):
        self.model = arg_model
        self.name = arg_name
        self.ip_address = arg_ip_address


    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."