import socket
import pickle
import google.generativeai as genai

s = socket.socket()
#print('Server created')
#I have kept my API_KEY as an environment variable so anyone downloading this code will have to do the same or paste their API KEY below for it to work
api_key = "API_KEY"
genai.configure(api_key = api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

s.bind(('localhost',44534))

s.listen(4)

#print("waiting for connections")

while True:
    c,addr = s.accept()
    #print("Connected with ",addr)
    prompti = c.recv(5000).decode()
    print(prompti)
    prompti = prompti.strip()
    response = model.generate_content(prompti)
    final_response = response.parts[0].text

    my_tuple = (final_response,prompti)
    encoded_tuple = pickle.dumps(my_tuple)

    # Send the encoded tuple to the client
    c.sendall(encoded_tuple)

    #encoded_tuple = tuple(f.encode("utf-8") for f in my_tuple)
    #tosend = encoded_tuple
    #c.sendall(tosend)

    c.close()










