from socket import *
import pickle
import random

# Create socket and start listening
port = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', port))
serverSocket.listen(1)

serverName = 'Server of Josh Kitzrow'
print(serverName + " is up")

waiting = True # When we send our response, exit loop
while waiting:
    # Connect to client
    connection, address = serverSocket.accept()
    print("Connected")
    data = connection.recv(1024).decode()

    # Unpack data up for easy access
    data = pickle.loads(data)

    # Print client name and their chosen number
    print("Client Name: " + data[0])
    print("Client Number: " + data[1])

    # Generate random number and calculate sum
    randomNum = random.randrange(1, 100, 1)
    newSum = (int)(data[1]) + randomNum
    response = [serverName, str(randomNum), str(newSum)]
    response = pickle.dumps(response)

    # Send server name, the random number, and the sum
    connection.send(response.encode())
    print("Sent response")

    # Close connection
    connection.close()
    waiting = False