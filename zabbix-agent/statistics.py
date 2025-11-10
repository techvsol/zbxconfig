#!/usr/bin/env python3
import sys
import json
import socket
import ipaddress

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print(f"Использование: {sys.argv[0]} <ip> <port>")
    sys.exit(1)

_, host, port = sys.argv

ipaddress.ip_address(host)

line, action = 'statistics\n'.encode(), {"action": "statistics"}
action = '{}\n'.format(json.dumps(action)).encode()

client.connect((host, int(port)))

data: bytearray = client.recv(1024)

client.sendall(line)
client.sendall(action)

data = client.recv(1024)

if data:
    print(data.decode().strip())

client.sendall('quit\n'.encode())
sys.exit(0)
