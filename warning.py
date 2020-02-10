from handler import Handler

class Warning(Handler):
    def getClassName(self):
        return __name__

    def execute(self):
        print(__name__)
