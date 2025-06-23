
import json
import struct

def send_msg(sock, obj):
    """Serialize obj to JSON, prefix with length, send."""
    data = json.dumps(obj).encode()
    length = struct.pack("!I", len(data))
    sock.sendall(length + data)

def recv_msg(sock):
    """Read length prefix, then JSON message."""
    raw_len = sock.recv(4)
    if not raw_len:
        raise ConnectionError("Disconnected")
    length = struct.unpack("!I", raw_len)[0]
    data = sock.recv(length)
    if not data:
        raise ConnectionError("Disconnected")
    return json.loads(data.decode())
