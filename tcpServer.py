import network, socket, gc
gc.enable()
gc.collect()

# ============================================================================

# !!! Need to Config !!!
SSID="SSID"
PASSWORD="PASSWORD"
# Port number must be the same with tcpClient
Port=10000

# ============================================================================

# Connecting to WiFi
wlan = network.WLAN(network.STA_IF)
if wlan.isconnected() == True:
    print("Already connected")
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while wlan.isconnected() == False:
    pass
print("Connection successful\n")
print('Network Config:', wlan.ifconfig())
print('IP Address:', wlan.ifconfig()[0])
print()

# ============================================================================

addr = socket.getaddrinfo('0.0.0.0', Port)[0][-1]

print("Listening on", addr)
try:
    listenSocket = socket.socket()
    listenSocket.bind(addr)
    listenSocket.listen(1)
    listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    while True:
        conn, addr = listenSocket.accept()
        print()
        print('Client Connected From', addr)
        print()
    
        data = conn.recv(1024)     # Receive 1024 byte of data from the Socket
        if(len(data) == 0):
            print("Closed Socket")
            conn.close()           # If there is no data, Close Socket
            gc.collect()
            break
        print(data)
        ret = conn.send(data)      # Send Data
except:
    if(listenSocket):
        listenSocket.close()
        gc.collect()
        print()
        print("Bye\n")
# ============================================================================

