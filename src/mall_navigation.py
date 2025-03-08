from typing import Dict, List, Tuple
import heapq

def find_minimum_path(mall_graph: Dict[str, Dict[str, int]], start_store: str, end_store: str) -> Tuple[List[str], int]:
    """
    Find the minimum path between two stores in a mall represented as a weighted graph.
    
    Args:
        mall_graph (Dict[str, Dict[str, int]]): A weighted graph representing mall stores and connections
        start_store (str): The starting store 
        end_store (str): The destination store
    
    Returns:
        Tuple[List[str], int]: A tuple containing the path and total distance
    
    Raises:
        ValueError: If start or end store is not in the graph
        ValueError: If no path exists between start and end stores
    """
    # Validate input stores exist in graph
    if start_store not in mall_graph:
        raise ValueError(f"Start store '{start_store}' not found in mall graph")
    if end_store not in mall_graph:
        raise ValueError(f"End store '{end_store}' not found in mall graph")
    
    # Dijkstra's algorithm for shortest path
    distances = {store: float('inf') for store in mall_graph}
    distances[start_store] = 0
    previous_stores = {store: None for store in mall_graph}
    
    # Priority queue to track minimum distances
    pq = [(0, start_store)]
    
    while pq:
        current_distance, current_store = heapq.heappop(pq)
        
        # Found destination
        if current_store == end_store:
            break
        
        # Skip if we've found a shorter path already
        if current_distance > distances[current_store]:
            continue
        
        # Check neighbors
        for neighbor, weight in mall_graph[current_store].items():
            distance = current_distance + weight
            
            # Update if shorter path found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_stores[neighbor] = current_store
                heapq.heappush(pq, (distance, neighbor))
    
    # Check if path was found
    if distances[end_store] == float('inf'):
        raise ValueError(f"No path exists between '{start_store}' and '{end_store}'")
    
    # Reconstruct path
    path = []
    current = end_store
    while current is not None:
        path.append(current)
        current = previous_stores[current]
    path.reverse()
    
    return path, distances[end_store]