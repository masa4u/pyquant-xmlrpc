from xmlrpcwrapper.design_pattern.singleton import SingletonMetaclass, with_metaclass
import xmlrpclib
import xmlrpcwrapper.server.server as xmlrpcserver


class XMLRPCClient(with_metaclass(SingletonMetaclass)):
    def __init__(self):
        print 'init proxy'
        self.proxy = xmlrpclib.ServerProxy('http://localhost:9000')
        xmlrpc_funcs = self.get_xmlrpc_func()

        self.register_xmlrpc_client_functions(xmlrpc_funcs)

    def get_func_client(self, server_func):
        def sample_func(*args):
            func = getattr(self.proxy, server_func.__name__)
            print server_func.__name__
            return func(*args)
        sample_func.__doc__ = "client %s" % server_func.__doc__
        sample_func.__name__ = server_func.__name__

        return sample_func

    def get_xmlrpc_func(self):
        xmlrpc_funcs = filter(lambda x: x.startswith('xmlrpc'), dir(xmlrpcserver))
        return xmlrpc_funcs

    def register_xmlrpc_client_functions(self, xmlrpc_funcs):
        for xmlrpc_func in xmlrpc_funcs:
            server_func = getattr(xmlrpcserver, xmlrpc_func)
            setattr(self, xmlrpc_func, self.get_func_client(server_func))
            print 'added : ' + xmlrpc_func

if __name__ == '__main__':
    print XMLRPCClient().xmlrpc_market_data_spot('c:/TEMP', '222')
    print XMLRPCClient().xmlrpc_market_data_spot('c:/TEMP', '222')
    print XMLRPCClient().xmlrpc_market_data_spot2('c:/TEMP')
    print XMLRPCClient().xmlrpc_market_data_list('c:/TEMP')