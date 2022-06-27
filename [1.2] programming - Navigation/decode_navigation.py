import socket

# get constellations
list_constellation = []
with open("constellations.txt") as constellation:
	for line in constellation:
		line = line[1:-2]
		list_constellation.append(line)

# connect with the sevice
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5.0)
s.connect(("ec2-52-209-66-116.eu-west-1.compute.amazonaws.com", 10000))

# Here we save what the socket reviewed in the variable answer.
answer = s.recv(1024).decode()
print(answer)

# read command to exec
task = answer.splitlines()[3]
_input = task.split()[5]

# calculate pow
import subprocess
subprocess.call([
    'python3',
    'proof.py',
    'solve',
    _input,
])

# send solution
solution = input()
s.send(f"{solution}\r\n".encode())
print(s.recv(1024).decode()) # Correct!

# read sky map
fragments = [] # list of bytes
while True: 
    chunk = s.recv(4096)
    fragments.append(chunk)
    if b'Length of the shortest path' in chunk:
    	break
   
full_map = b''.join(fragments)
full_map = full_map.decode()
full_map = ''.join(full_map.split("\n")[:-3])

# parse sky map
sky_road = []
for i in range(len(full_map)//8):
	sky_road.append(full_map[i*8:(i+1)*8])

routes=''
for path in sky_road:
	routes += chr(list_constellation.index(path))

import ast
# Given string "[(0,1,333), (0,2, 531),..]"
routes = ast.literal_eval(routes)
print("final list", routes)

import math
from collections import defaultdict

# run dijsktra 
all_nodes = {i: math.inf for i in range(51)}
all_nodes.update({0: 0})

paths = defaultdict(list)
paths[0] = [[0]]
visited_nodes = set()

def find_cheapest_unvisited_node():
    cheapest_cost = math.inf
    cheapest_node = None
    for node, dist in all_nodes.items():
        if node in visited_nodes:
            continue
        if dist < cheapest_cost:
            cheapest_cost = dist
            cheapest_node = node
    return cheapest_node

def find_path_from_node(node):
    routes_starting_at_node = [route for route in routes if route[0] == node]
    routes_ending_at_node = [route for route in routes if route[1] == node]
    print(f'{routes_starting_at_node=}')
    for route in routes_starting_at_node:
        target = route[1]
        all_nodes[target] = min(all_nodes[target], all_nodes[node] + route[2])
    for route in routes_ending_at_node:
        target = route[0]
        all_nodes[target] = min(all_nodes[target], all_nodes[node] + route[2])

    visited_nodes.add(node)

next_node = 0
while next_node is not None:
    print(f'{next_node=}')
    find_path_from_node(next_node)
    next_node = find_cheapest_unvisited_node()

print(all_nodes)

# send solution
solution = input()
s.send(f"{solution}\r\n".encode())
print(s.recv(1024).decode())

# close the socket.
s.close




