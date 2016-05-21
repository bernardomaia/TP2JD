import socket

def activeOpen(SRV,port):
    soquete = Soquete()
    host = socket.gethostname()
    
    soquete.s.connect((host,port))
    return soquete

def passiveOpen(port):
    soquete = Soquete()
    host = socket.gethostname()
    soquete.s.bind((host, port))
    
    print "host: ", host
    print "port: ", port
    soquete.s.listen(5)
    
    conn, addr = soquete.accept()
    
    return (conn, addr)

class Soquete:
    
    def __init__(self):
        self.s = socket.socket()
        
    def recv(self, size):
        return self.s.recv(size)
    
    def send(self, data):
        self.s.send(data)
    
    def close(self):
        self.s.close()
    
    def accept(self):
        conn = Soquete()
        conn.s, addr = self.s.accept()
        return conn, addr