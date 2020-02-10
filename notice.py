from handler import Handler

class Notice(Handler):
    def getClassName(self):
        return __name__

    def execute(self):
        print(__name__)
