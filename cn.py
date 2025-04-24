def compute_crc_simple(message, poly, width):
    result = 0  # Start with 0 as the magic number (CRC)

    for ch in message:
        result ^= ord(ch) << (width - 8)  # Mix in the character

        # Do 8 steps of bit magic
        for _ in range(8):
            if result & (1 << (width - 1)):  # If leftmost bit is 1
                result = (result << 1) ^ poly
            else:
                result <<= 1

            # Keep result within given width (like 12-bit or 16-bit)
            result &= (1 << width) - 1

    return result

if _name_ == "_main_":
    message = "HELLO"

    # Special magic numbers (polynomials) for different CRC types
    crc12_poly = 0x80F       # For CRC-12 (12-bit)
    crc16_poly = 0x8005      # For CRC-16-IBM (16-bit)
    crc_ccitt_poly = 0x1021  # For CRC-CCITT (16-bit)

    print("Message:", message)
    print(f"CRC-12: 0x{compute_crc_simple(message, crc12_poly, 12):03X}")
    print(f"CRC-16: 0x{compute_crc_simple(message, crc16_poly, 16):04X}")
    print(f"CRC-CCITT: 0x{compute_crc_simple(message, crc_ccitt_poly, 16):04X}")
    
    
    
    

    
# Total number of places (points on a map)
V = 5

# Function to find the nearest unvisited place
def find_min_distance(distances, visited):
    min_value = float('inf')
    min_index = -1
    for i in range(V):
        if not visited[i] and distances[i] < min_value:
            min_value = distances[i]
            min_index = i
    return min_index

# Dijkstra's algorithm to find shortest path
def dijkstra(graph, start):
    # Set all distances to a very big number
    distances = [float('inf')] * V
    # Starting point is 0 distance from itself
    distances[start] = 0
    # Keep track of visited places
    visited = [False] * V

    # Repeat for all places
    for _ in range(V):
        # Pick the nearest unvisited place
        u = find_min_distance(distances, visited)
        if u == -1:
            break
        visited[u] = True

        # Update distances to other places from u
        for v in range(V):
            if graph[u][v] > 0 and not visited[v]:
                new_distance = distances[u] + graph[u][v]
                if new_distance < distances[v]:
                    distances[v] = new_distance

    # Print the result
    print("Place\tDistance from Start")
    for i in range(V):
        print(f"{i}\t{distances[i]}")

# Map of places and distances between them
graph = [
    [0, 10, 0, 0, 5],
    [0, 0, 1, 0, 2],
    [0, 0, 0, 4, 0],
    [7, 0, 6, 0, 0],
    [0, 3, 9, 2, 0]
]

# Start from place 0
dijkstra(graph, 0)






NUM_NODES = 5
INFINITY = 99999  # A very big number means "no direct road"

# Find the nearest unvisited computer
def find_closest_node(cost, visited):
    min_cost = INFINITY
    closest = -1
    for i in range(NUM_NODES):
        if not visited[i] and cost[i] < min_cost:
            min_cost = cost[i]
            closest = i
    return closest

# Create and print the routing table from one computer
def build_routing_table(network, start):
    cost = [INFINITY] * NUM_NODES
    visited = [False] * NUM_NODES
    cost[start] = 0  # Cost to itself is zero

    for _ in range(NUM_NODES - 1):
        current = find_closest_node(cost, visited)
        visited[current] = True

        # Check if going through 'current' is shorter to reach any neighbor
        for neighbor in range(NUM_NODES):
            if network[current][neighbor] != 0 and not visited[neighbor]:
                new_cost = cost[current] + network[current][neighbor]
                if new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost

    # Print the routing table
    print(f"Routing Table for Computer {start}:")
    for i in range(NUM_NODES):
        print(f"To {i}: Cost = {cost[i]}")
    print()

# Our computer network (like a map with distances)
network = [
    [0, 10, INFINITY, 30, 100],
    [10, 0, 50, INFINITY, INFINITY],
    [INFINITY, 50, 0, 20, 10],
    [30, INFINITY, 20, 0, 60],
    [100, INFINITY, 10, 60, 0]
]

# Show routing table for every computer
for computer in range(NUM_NODES):
    build_routing_table(network, computer)
    
    
    
    
    
    
    
    
    
# Character Stuffing: Replace every 'F' with 'EF'
def character_stuffing(data):
    result = ""
    for ch in data:
        if ch == 'F':
            result += "EF"
        else:
            result += ch
    return result

# Bit Stuffing: After five 1's in a row, add a 0
def bit_stuffing(bits):
    result = ""
    count = 0
    for bit in bits:
        result += bit
        if bit == '1':
            count += 1
            if count == 5:
                result += '0'  # Stuff a 0
                count = 0
        else:
            count = 0
    return result

# Let's test it
if _name_ == "_main_":
    data = "ABCF"
    bits = "111110"

    print("Character Stuffing:", character_stuffing(data))
    print("Bit Stuffing:", bit_stuffing(bits))
    
  
  
  
  
    
    
def sliding_window():
    frames = [1, 2, 3, 4]
    window_size = 2
    ack = 0

    for i in range(len(frames)):
        print(f"Sent: {frames[i]}")
        if i - ack + 1 <= window_size:
            print(f"Ack: {frames[ack]}")
            ack += 1
        else:
            print("Waiting for ack...")

if _name_ == "_main_":
    sliding_window()
    
    





import socket

def resolve_hostname(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"Resolved IP: {ip_address}")
    except socket.gaierror:
        print(f"Failed to resolve hostname: {hostname}")

if _name_ == "_main_":
    hostname = input("Enter hostname to resolve: ").strip()
    resolve_hostname(hostname)