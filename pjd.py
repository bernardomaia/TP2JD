import socket

def checksum(message):

        size = len(message)
        cs = 0

        #Realiza a checksum 1 caracter por vez
        while size > 0:
            size -=1
            cs += ord(message[size])

        #Passando o carry
        if ( cs > 0xffff):
            cs = (cs & 0x1111) + (cs >>16)
        return hex(cs)


def activeOpen(SRV,port):
    soquete = Soquete()
    host = socket.gethostname()
    
    while 1:
        soquete.sendSYN(host,port)
        print "Cliente diz: enviei SYN para ",host,":",port
        soquete.state = "SYN_SENT"
    
    return soquete

def passiveOpen(port):
    soquete = Soquete()
    host = socket.gethostname()
    soquete.s.bind((host, port))
    soquete.state = "LISTEN"
    print "host: ", host
    print "port: ", port
    
    while 1:
        seqNo = -1
        package, addr = soquete.s.recvfrom(1024)
        header, data = splitPackage(package)
        if soquete.state == "LISTEN":
            if header.type == '3':
                print "Servidor diz: recebi SYN("+header.seqno+") do ", addr
                soquete.state = "LISTEN2"
                seqNo = header.seqno
        elif soquete.state == "LISTEN2":
            if header.type == '2' and int(header.seqno) == int(seqNo)+1:
                print "Servidor diz: recebi ACK("+header.seqno+")  do ", addr
                soquete.state = "EST"
                seqNo = header.seqno
                    
    
    return  addr

def splitPackage(p):
    a,b,c,data = p.split(',')
    header = Header(a,b,c)
    return (header, data)

class Soquete:
    
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.state = 'CLOSED'
        
    def recv(self, size):
        return self.s.recv(size)
    
    def sendSYN(self, host, port):
        header = Header("3","0", "")
        self.send(host,port,header,"")
    
    def send(self, host, port, header,data):
        package = header+data
        self.s.sendto(package,(host,port))
    
    def close(self):
        self.s.close()
    
    def accept(self):
        conn = Soquete()
        conn.s, addr = self.s.accept()
        return conn, addr


class Header:
    
    def __init__(self, t, s, w):
        self.type = t
        self.seqno = s
        self.window = w
    
    def __str__(self):
        return self.type+","+self.seqno+","+self.window+","
    
    def __add__(self, other):
        return str(self) + other

