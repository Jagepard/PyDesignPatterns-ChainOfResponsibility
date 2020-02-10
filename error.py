from handler import Handler

class Error(Handler):
    def getClassName(self):
        return __name__

    def execute(self):
        print(__name__)
