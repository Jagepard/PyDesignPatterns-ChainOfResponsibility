"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

class Handler:
    def getClassName(self):
        return __name__
    
    def execute(self):
        print(__name__)
