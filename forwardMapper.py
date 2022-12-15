from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import libmapper as mpr
import threading

IP = '192.168.0.192'
PORT = 8000
signalNames = []

def _create_osc_server():
    dispatcher = Dispatcher()
    dispatcher.map('/*', osc_handler)
    return BlockingOSCUDPServer((IP, PORT), dispatcher)

def osc_handler(address, *args):
        if address in signalNames:
            # Set sig value
            sig = find_sig(address)
            if not sig:
                return
            else:
                #print("value: " + list(args))
                sig.set_value(list(args))
            pass
        else:
            # Add signal to device
            print("adding sig: forward" + str(address))
            sigType = mpr.Type.FLOAT if isinstance(args[0], float) else mpr.Type.INT32
            dev.add_signal(mpr.Direction.OUTGOING, address, len(args), sigType, "", -1000, 1000, None, None)
            signalNames.append(address)

def find_sig(fullname):
    fullname = fullname[1:]
    if dev:
        sig = dev.signals().filter(mpr.Property.NAME, fullname)
        if not sig:
            return None
        return sig.next()
    else:
        return None
        
if __name__ == '__main__':
    server = _create_osc_server()
    threading.Thread(target=server.serve_forever, daemon=True).start()
    dev = mpr.Device("forward")
    while 1:
        dev.poll(100)