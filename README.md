# ForwardMapper
 
An OSC to libmapper signal discovery and forwarding program.

ForwardMapper discovers OSC messages sent to your device and creates libmapper signals on the network with the same namespace structure.

## Usage

1. In forwardMapper.py change the `IP` and `PORT` to match where OSC will be coming in
2. Run `python forwardMapper.py` and watch as OSC signals are discovered and created on the libmapper network under the `forward.1` device
3. Launch any other libmapper-enabled devices you intend to use
4. Open [webmapper](https://github.com/libmapper/webmapper) to create mappings between signals or use [mappersession](https://github.com/libmapper/mappersession) to load a mapping session file