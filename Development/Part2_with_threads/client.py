import socket
import pickle
import json
import time
import threading

def dump_to_json(data, filename):
    """Dump tuple data to JSON file in append mode"""
    with open(filename, 'a') as f:
        json.dump(data, f,indent=4)
        f.write('\n')  

def runclient(client_id):
    c = socket.socket()
    c.connect(('localhost',44534))
    print(f"Client {client_id} connected")
    prompti = input(f"Client {client_id} prompt: ")
    start_time = int(time.time())
    c.send(bytes(prompti,'utf-8'))
    encoded_tuple = c.recv(10000)
    end_time = int(time.time())
    my_tuple = pickle.loads(encoded_tuple)

    filename = "all_responses_combined.json"
    result = {
        "Prompt":my_tuple[1],
        "Message":my_tuple[0],
        "TimeSent":start_time,
        "TimeRecvd":end_time,
        "Source":"Google Generative AI",
        "ClientID":client_id
    }
    dump_to_json(result, filename)
    c.close()


num = 3
for i in range(num):
    client_thread = threading.Thread(target=runclient, args=(i+1,))  #remember we have to always pass a tuple for the arguments in a threading operation
    client_thread.start()
