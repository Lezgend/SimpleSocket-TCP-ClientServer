# SimpleSocket-TCP-ClientServer
A simple TCP socket built with MicroPython for ESP32

# Usage
You have to upload tcpServer.py to your ESP32 and configure the file for a WiFi connection first.
```
# !!! Need to Config !!!
SSID="SSID"
PASSWORD="PASSWORD"
# Port number must be the same as tcpClient
Port=10000
```

After you run the tcpServer.py script, you will get IPv4 for communicating with the server, which you have to copy and use in tcpClient.py.
```
# !!! Need to Config !!!
Host = "192.168.X.X"
# Port number must be the same as tcpServer
Port = 10000
DATA = "BANANA POTETO"
```
# Example

## Server
In Thonny Shell
```
Connection successful

Network Config: ('192.168.X.X', '255.255.255.0', '192.168.X.X', '192.168.X.X')
IP Address: 192.168.X.X

Listening on ('0.0.0.0', 10000)

Client Connected From ('192.168.X.X', 57265)
BANANA POTETO

Client Connected From ('192.168.X.X', 57266)
BANANA POTETO

Client Connected From ('192.168.X.X', 57267)
BANANA POTETO

Socket Closed
----------Bye----------
```

## Client
In your Terminal
```
❯ python tcpClient.py
Start Sending
BANANA POTETO
❯ python tcpClient.py
Start Sending
BANANA POTETO
❯ python tcpClient.py
Start Sending
BANANA POTETO
```
---
<b>Ctrl + C</b> keyboard shortcut; will interrupt the program.
```
Connection successful

Network Config: ('192.168.X.X', '255.255.255.0', '192.168.X.X', '192.168.X.X')
IP Address: 192.168.X.X

Listening on ('0.0.0.0', 10000)

Socket Closed
----------Bye----------
```