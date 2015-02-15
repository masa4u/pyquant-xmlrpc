import cmd
from colorama import Fore
from xmlrpcwrapper.client.client import XMLRPCClient


class XMLRPCConsole(cmd.Cmd):
    """Simple command processor example."""
    intro = '\n'.join(['---------------------------------------------',
                       Fore.YELLOW + 'XMLRPCConsole' + Fore.RESET,
                       '---------------------------------------------'])
    prompt = Fore.RED + ' command : ' + Fore.RESET

    def do_xmlrpc_method(self, line):
        xmlrpc_func = XMLRPCClient().get_xmlrpc_func()
        for func_name in xmlrpc_func:
            print func_name
    def do_xmlrpc_call(self, line):
        print line

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    XMLRPCConsole().cmdloop()