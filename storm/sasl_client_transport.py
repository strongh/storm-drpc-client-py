from thrift_sasl import TSaslClientTransport
from sasl import Client
import getpass

class SaslClientTransport(TSaslClientTransport):
    def __init__(self, host, transport, service=None, mechanism=None):
        self.host = host
        self.transport = transport
        self.service = service
        self.mechanism = mechanism
        TSaslClientTransport.__init__(self, self.SaslClientFactory, self.mechanism, transport)

    def SaslClientFactory(self):
        client = Client()
        client.setAttr("service", self.service)
        client.setAttr("host", self.host)
        client.setAttr("username", getpass.getuser())
        client.setAttr("password", "password")
        client.init()
        return client
