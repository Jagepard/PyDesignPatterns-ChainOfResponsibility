"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""


class AbstractHandler:
    next = None
    name = None

    def __init__(self, name) -> None:
        self.name = name

    def set_next(self, handler: object) -> object:
        self.next = handler
        return handler
    
    def execute(self, request: str) -> object:
        if request == self.name:
            print(self.name + " has handle an error")
            return

        if self.next is None:
            raise Exception("Handler does not exist in the chain")

        self.next.execute(request)
