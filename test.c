#include <stdio.h>
#include <string.h>

// These are special numbers used in our magic math (called CRC)
#define POLYNOMIAL 0xD8
#define TOP_BIT 0x80

// This function creates a "magic number" (called CRC) from a message
unsigned char calculate_crc(unsigned char *message, size_t length) {
    unsigned char result = 0;

    // Go through every letter in the message
    for (size_t i = 0; i < length; ++i) {
        result ^= message[i];  // Mix the letter with the result

        // Do 8 steps of magic math for each letter
        for (unsigned char bit = 8; bit > 0; --bit) {
            if (result & TOP_BIT) {
                result = (result << 1) ^ POLYNOMIAL; // If top bit is 1, mix with polynomial
            } else {
                result = result << 1; // Just shift left
            }
        }
    }

    return result; // This is our final magic number (CRC)
}

int main() {
    unsigned char message[] = "Hello, CRC!"; // This is our message
    unsigned char crc_result = calculate_crc(message, strlen((char *)message)); // Calculate CRC

    printf("Message: %s\n", message); // Show the message
    printf("CRC (Magic Number): 0x%02X\n", crc_result); // Show the CRC in hex format

    return 0;
}




#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

#define V 5

int mindist(int dist[], bool visited[]) {
    int min = INT_MAX, minIndex = -1;
    for (int v = 0; v < V; v++) {
        if (!visited[v] && dist[v] < min) {
            min = dist[v];
            minIndex = v;
        }
    }
    return minIndex;
}

void dijkstra(int graph[V][V], int src) {
    int dist[V];
    bool visited[V];

    for (int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
        visited[i] = false;
    }

    dist[src] = 0;

    for (int count = 0; count < V - 1; count++) {
        int u = mindist(dist, visited);
        if (u == -1) break;
        visited[u] = true;

        for (int v = 0; v < V; v++) {
            if (!visited[v] && graph[u][v] && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    printf("Vertex\tDistance from Source\n");
    for (int i = 0; i < V; i++) {
        printf("%d\t%d\n", i, dist[i]);
    }
}

int main() {
    int graph[V][V] = {
        {0, 10, 0, 0, 5},
        {0, 0, 1, 0, 2},
        {0, 0, 0, 4, 0},
        {7, 0, 6, 0, 0},
        {0, 3, 9, 2, 0}
    };

    dijkstra(graph, 0);
    return 0;
}



#include <stdio.h>

#define NUM_NODES 5
#define INFINITY 99999

int findClosestNode(int cost[], int visited[]) {
    int min = INFINITY;
    int closest = -1;

    for (int i = 0; i < NUM_NODES; i++) {
        if (!visited[i] && cost[i] < min) {
            min = cost[i];
            closest = i;
        }
    }

    return closest;
}

void buildRoutingTable(int network[NUM_NODES][NUM_NODES], int startNode) {
    int cost[NUM_NODES];
    int visited[NUM_NODES] = {0}; 

    for (int i = 0; i < NUM_NODES; i++) {
        cost[i] = INFINITY;
    }

    cost[startNode] = 0;

    for (int step = 0; step < NUM_NODES - 1; step++) {
        int currentNode = findClosestNode(cost, visited);
        visited[currentNode] = 1;

        for (int neighbor = 0; neighbor < NUM_NODES; neighbor++) {
            if (!visited[neighbor] && network[currentNode][neighbor] &&
                cost[currentNode] + network[currentNode][neighbor] < cost[neighbor]) {
                cost[neighbor] = cost[currentNode] + network[currentNode][neighbor];
            }
        }
    }

    printf("Routing Table for Computer %d:\n", startNode);
    for (int i = 0; i < NUM_NODES; i++) {
        printf("To %d: Cost = %d\n", i, cost[i]);
    }
    printf("\n");
}

int main() {
    int network[NUM_NODES][NUM_NODES] = {
        {0, 10, INFINITY, 30, 100},
        {10, 0, 50, INFINITY, INFINITY},
        {INFINITY, 50, 0, 20, 10},
        {30, INFINITY, 20, 0, 60},
        {100, INFINITY, 10, 60, 0}
    };

    for (int computer = 0; computer < NUM_NODES; computer++) {
        buildRoutingTable(network, computer);
    }

    return 0;
}