import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")

with open('received_file.txt', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        # write data to a file
        f.write(data)
        break
f.close()

text = raw_input("pls append to me: ")
with open('received_file.txt','a') as file:
    file.write('\n' + text)
file.close()

f = open('received_file.txt','rb')
l = f.read(1024)
while (l):
    s.send(l)
    print('Sent ',repr(l))
    l = f.read(1024)
f.close()
print('Successfully got the file')
s.close()
print('connection closed')
