from twisted.internet.protocol import Factory, Protocol, ClientFactory
from twisted.internet import reactor

from txsockjs.factory import SockJSMultiFactory
from txsockjs.utils import broadcast
from txsockjs import multiplex

from main import TwistedChatConnection


class MyClient(Protocol):

    def __init__(self):
        self.username = ''

    def connectionMade(self):
        print 'Connection Made!'

        print self.transport

    def dataReceived(self, data):
        print 'Incoming Message: ' + data
        self.messaging()

    def user_login(self):

        print 'Welcome to chat!  Please enter your name: '
        self.username = raw_input()


    def messaging(self):
        print 'Message to send: '
        message = raw_input()

        broadcast(message, TwistedChatConnection)


class MyClientFactory(ClientFactory):
    protocol = MyClient

    def clientConnectionFailed(self, connector, reason):
        print 'Connection Failed!!!'
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print 'Connection Lost!!!'
        reactor.stop()


def main():
    f = MyClientFactory()
    reactor.connectTCP('localhost', 8080, f)
    reactor.run()

if __name__ == '__main__':
    main()