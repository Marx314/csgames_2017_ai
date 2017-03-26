from twisted.internet import reactor
from twisted.internet.protocol import Factory

from network.communication import Communication
from network.online_gateway import OnlineGateway
from hockey.controller import ControllerGentle


class ChatFactory(Factory):
    def __init__(self):
        self.users = {}
        self.online_gateway = OnlineGateway(lambda: ControllerGentle(11, 11), timeout=2, debug=True)

    def buildProtocol(self, addr):
        return Communication(self.users, self.online_gateway)


cf = ChatFactory()
reactor.listenTCP(8023, cf)
reactor.run()
