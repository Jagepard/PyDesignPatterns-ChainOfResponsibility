from Chain import Chain
from NoticeHandler import NoticeHandler
from WarningHandler import WarningHandler
from ErrorHandler import ErrorHandler

chain = Chain()

chain.addToChain(NoticeHandler())
chain.addToChain(WarningHandler())
chain.addToChain(ErrorHandler())

chain.execute("NoticeHandler")
chain.execute("WarningHandler")
chain.execute("ErrorHandler")
