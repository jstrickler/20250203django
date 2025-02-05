class Simple:  # default base class is object
    def __init__(self, message_text):  # constructor/initializer
        self._message_text = message_text  # message text stored in instance object

    def get_text(self):  # instance 'getter method'
        return self._message_text

    @property  # decorator
    def text(self):  # getter property
        return self._message_text

if __name__ == "__main__":
    msg1 = Simple('hello')  # instantiate an instance of Simple
    print(msg1.get_text())  # call instance method
    print(msg1.text) 

    msg2 = Simple('hi there')  # create 2nd instance of Simple
    print(msg2.get_text())
    print(msg2.text)
