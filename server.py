import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 9000))
server_socket.listen(1)

print("Listening on http://127.0.0.1:9000")

client_socket, client_address = server_socket.accept()
print(f"Connection from : {client_address}")

request = client_socket.recv(1024)
print(f"request: {request.decode("utf-8")}")

response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type:text/plain; charset=utf-8\r\n"
    "Content-Length: 24\r\n"
    "\r\n"
    "Hello from the raw socket!!!"
)

client_socket.sendall(response.encode("utf-8"))
client_socket.close()
server_socket.close()