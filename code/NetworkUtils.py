import socket

# 3 MB buffer
MAX_BUFFER_LEN = 3 * (1 << 20)

def sendTCP(host_ip: str, host_port: int, msg: bytes) -> bytes:
    assert type(host_ip) == str
    assert type(host_port) == int
    assert type(msg) == bytes

    # TCP client socket
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((host_ip, host_port))
    cs.send(msg)
    ret = cs.recv(MAX_BUFFER_LEN)
    cs.close()
    return ret

# basic testing worker
def echoWorker(client_msg: bytes):
    return b"echo recieved: " + client_msg

# set ban IP list
BAN_IP_LIST = []
def startDemoServerTCP(host_ip: str, host_port: int, worker=echoWorker) -> bytes:
    assert type(host_ip) == str
    assert type(host_port) == int

    s = socket.socket()
    s.bind((host_ip, host_port))
    s.listen(10)

    print("startDemoServerTCP: %s:%d" % (host_ip, host_port))
    while True:
        c, (client_ip, client_port) = s.accept()

        if client_ip not in BAN_IP_LIST:
            msg = c.recv(MAX_BUFFER_LEN)
            ret = worker(msg)
            print("accept: %s:%d" % (client_ip, client_port), "recieve:", msg)
            c.send(ret)
        c.close()

if __name__ == "__main__":
    startDemoServerTCP("127.0.0.1", 33728)