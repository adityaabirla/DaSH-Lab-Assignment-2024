import socket
import pickle
import json
import time

def dump_to_json(data, filename):
    """Dump tuple data to JSON file in append mode"""
    with open(filename, 'a') as f:
        json.dump(data, f,indent=4)
        f.write('\n')  # append a newline for readability



c = socket.socket()
c.connect(('localhost',44534))
print("connected")
prompti = input()
start_time = int(time.time())
c.send(bytes(prompti,'utf-8'))
#received = c.recv(10000).decode()

#decoded_tuple = tuple(s.decode("utf-8") for s in c.recv(10000))
encoded_tuple = c.recv(10000)
end_time = int(time.time())
# Decode the tuple from bytes
my_tuple = pickle.loads(encoded_tuple)

filename = "all_responses_combined.json"
result = {
    "Prompt":my_tuple[1],
    "Message":my_tuple[0],
    "TimeSent":start_time,
    "TimeRecvd":end_time,
    "Source":"Google Generative AI",
    "ClientID":1
}
dump_to_json(result, filename)


