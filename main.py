from chain import Chain
from notice import Notice
from warning import Warning
from error import Error

chain = Chain()

chain.addToChain(Notice())
chain.addToChain(Warning())
chain.addToChain(Error())

chain.execute("notice")
chain.execute("warning")
chain.execute("error")
