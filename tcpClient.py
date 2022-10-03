import socket, time

SOC = None

# ============================================================================

# !!! Need to Config !!!
Host = "192.168.x.x"
# Port number must be the same with tcpServer
Port = 10000
DATA = "BANANA POTETO"

# ============================================================================

print("Start Sending")

try:
    SOC = socket.socket()         # Create Socket
    SOC.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    SOC.connect((Host,Port))      # Send Require for Connecting
    SOC.send(DATA.encode())       # Send Data
    
    while True:
        data = SOC.recv(1024)          # Receive 1024 byte of data from the Socket
        count = 1
        if(len(data) == 0):                             
            print("Closed Socket")
            SOC.close()
            break
        print(data)
        SOC.send(DATA.encode())
        if count == 1: break
        
except:
    if (SOC):
        SOC.close()
        print()
        print("Bye\n")      
# ============================================================================

