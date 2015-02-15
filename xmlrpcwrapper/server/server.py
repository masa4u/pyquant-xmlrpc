from SimpleXMLRPCServer import SimpleXMLRPCServer
import logging

from xmlrpcwrapper.marketdata.spot import MarketDataSpot


def xmlrpc_market_data_spot(name, date):
    logging.debug('market_data_spot(%s, %s)' % (name, date))

    return MarketDataSpot()


def xmlrpc_market_data_spot2(name):
    logging.debug('market_data_spot2(%s, %s)' % (name, ''))

    return name


def xmlrpc_market_data_list(name):
    logging.debug('market_data_spot2(%s, %s)' % (name, ''))

    return [1, 2, 3, 4, 5]


def run_xmlrpc_server():
    # Set up logging
    logging.basicConfig(level=logging.DEBUG)
    server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)
    # Expose a function

    server.register_function(xmlrpc_market_data_spot)
    server.register_function(xmlrpc_market_data_spot2)
    server.register_function(xmlrpc_market_data_list)

    try:
        print 'Use Control-C to exit'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Exiting'

if __name__ == '__main__':
    run_xmlrpc_server()
