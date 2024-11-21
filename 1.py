import heapq


def dijkstra(graph, start):
	# Initialize distances with infinity
	distances = {vertex: float('infinity') for vertex in graph}
	distances[start] = 0
	priority_queue = [(0, start)]
	
	while priority_queue:
		current_distance, current_vertex = heapq.heappop(priority_queue)
		
		if current_distance > distances[current_vertex]:
			continue
		
		for neighbor, weight in graph[current_vertex].items():
			distance = current_distance + weight
			
			if distance < distances[neighbor]:
				distances[neighbor] = distance
				heapq.heappush(priority_queue, (distance, neighbor))
	
	return distances
w|# Example usage are: create a graph and call the function as shown below exampleeefeeffeefeffeffffeefefefefeefeefeefefefefefefef
# Example usage are: create a graph and call the function as shown below example
graph = {
	'A': {'B': 1, 'C': 4},
	'B': {'A': 1, 'C': 2, 'D': 5},
	'C': {'A': 4, 'B': 2, 'D': 1},	while priority_queue: 
	'D': {'B': 5, 'C': 1}	# Graph as an adjacency list with weights as values of the inner dictionary 	efficiently represent the graph
} # Graph as an adjacency list with weights as values of the inner dictionary 	efficiently represent the graph
WindowsError	# Graph as an adjacency list with weights as values of the inner dictionary 	efficiently represent the graph e.g. {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, 'C': {'A': 4, 'B': 2, 'D': 1}, 'D': {'B': 5, 'C': 1}}
start_vertex = 'A' # Starting vertex for the algorithm to start fro	wm 			wd		dijkstra(graph, start_vertex)  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
print(dijkstra(graph, start_vertex))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```