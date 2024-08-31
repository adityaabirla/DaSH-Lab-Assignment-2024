import socket
import pickle
import google.generativeai as genai
import threading

s = socket.socket()
#print('Server created')

api_key = "AIzaSyCiuFhLEgiX2KP3GypwKIVdBIxcOs8Embc"
genai.configure(api_key = api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

s.bind(('localhost',44534))

s.listen(4)

#print("waiting for connections")

def handleclient(c, addr):
    #print("Connected with ",addr)
    prompti = c.recv(5000).decode()
    print(prompti)
    prompti = prompti.strip()
    response = model.generate_content(prompti)
    final_response = response.parts[0].text

    my_tuple = (final_response,prompti)
    encoded_tuple = pickle.dumps(my_tuple)

    #remember we have to send it as encoded cuz all these comms are only in byte streams
    c.sendall(encoded_tuple)

    c.close()

while True:
    c, addr = s.accept()
    client_thread = threading.Thread(target=handleclient, args=(c, addr))
    client_thread.start()
