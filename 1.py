import heapq


def shortest_path(graph, start, end):
    # Initialize distances with infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to store (distance, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we reached the end node, return the distance
        if current_node == end:
            return current_distance
        # If we have already found a better path to current_node, skip it
        # If a shorter path to current_node has been found, skip processing
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]: 
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return float('inf')  # If there's no path from start to end

# Example usage
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3)]
}

start = 'A'
end = 'D'
print("Shortest path from {} to {} is {}".format(start, end, shortest_path(graph, start, end)))