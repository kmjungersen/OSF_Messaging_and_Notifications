from twisted.internet.protocol import Factory, Protocol, ServerFactory
from twisted.internet import reactor

from txsockjs.factory import SockJSMultiFactory, SockJSFactory
from txsockjs.utils import broadcast
from txsockjs import multiplex


class TwistedChatConnection(Protocol):

    def __init__(self):
        self.factory.transports = set()
        self.users = set()




    def connectionMade(self):
        print 'User attempting connection!'

        #self.admin.login(username)

        self.factory.transports.add(self.transport)


    def dataReceived(self, data):

        broadcast(data, self.factory.transports)


    def connectionLost(self, reason=''):

        self.factory.transports.remove(self.transport)

        print 'User disconnected'


class ServerAdmin():

    def __init__(self):
        pass

    def login(self, username):

        if (username):
            print 'Welcome {}!'.format(username)
        else:
            print 'ERROR: Username already taken!'



    def authenticate_username(self, username):
        print 'authenticating....'

        print TwistedChatConnection.users

        if username in TwistedChatConnection.users:
            return False
        else:
            return True

def attempt_login(username):
    pass


def main():

    f = SockJSFactory(Factory.forProtocol(TwistedChatConnection))

    reactor.listenTCP(8020, f)

    reactor.run()

if __name__ == '__main__':
    main()