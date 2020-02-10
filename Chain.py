"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

from Handler import Handler

class Chain:
    chain = {}

    def addToChain(self, handler):
        if handler.getClassName() in self.chain:
            raise Exception("Handler already exists")
        self.chain[handler.getClassName()] = handler

    def execute(self, handlerName):
        if handlerName in self.chain:
            for key, handler in self.chain.items():
                handler.execute()
                if key == handlerName:
                    return;

        raise Exception("Handler does not exist in the chain")

