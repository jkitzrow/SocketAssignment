from socket import *
import pickle

# Client Name
name = "Josh Kitzrow"
print("Client of " + name)

# Error checking loop
# TODO: check if user entered an integer
canContinue = False
while not canContinue:
    # Prompt user for number
    number = (int)(input("Enter a number between 1 and 100: "))
    if (number >= 1 and number <= 100):
        canContinue = True
    else:
        print("Out of range, try again")

# Server and client socket setup
serverName, serverPort = 'localhost', 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server
clientSocket.connect((serverName, serverPort))

# Pack up data for easy use and send it
data = pickle.dumps([name, (str)(number)])
clientSocket.send(data)

print("Sent Data ... waiting for response")

# Store server response and unpack data
response = clientSocket.recv(1024)
response = pickle.loads(response)

# Print results
print("Server Name: " + response[0])
print("Server random number: " + response[1])
print("Sum of numbers: " + response[2])

# Close socket
clientSocket.close()

