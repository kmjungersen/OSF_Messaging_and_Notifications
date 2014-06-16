from twisted.internet.protocol import Factory, Protocol, ServerFactory
from twisted.internet import reactor

from txsockjs.factory import SockJSMultiFactory
from txsockjs.utils import broadcast
from txsockjs import multiplex

from twisted.words.protocols import irc


class TwistedChatConnection(Protocol):

    users = set()

    def __init__(self):
        pass
        #self.users = set()

    def connectionMade(self):
        print 'User connected!'

        self.factory.transports.add(self.transport)

    def dataReceived(self, data):

        broadcast(data, self.factory.transports)

    def connectionLost(self, reason=''):
        print 'User disconnected'


def authenticate_username(username):
    print 'authenticating....'

    print TwistedChatConnection.users

    if username in TwistedChatConnection.users:
        return False
    else:
        return True


def main():

    f = ServerFactory()
    f.protocol = TwistedChatConnection

    reactor.listenTCP(8080, f)
    reactor.run()

if __name__ == '__main__':
    main()