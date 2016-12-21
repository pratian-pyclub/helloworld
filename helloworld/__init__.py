from configurations import helper

class Helloworld():
    def __init__(self, name):
        self.name = name

    def show(self, lastname = "A"):
        print(self.name + lastname)

    def helper(self):
        helper()

    # @staticmethod
    # def show():
    #     print("THIS IS A STATIC FUNCTION")
