from collections import deque
from GraphAL import GraphAL
from dsf import DisjointSetForest


def topological_sort(graph):
  """
  Implements topological sort algorithm on a graph object.
  
  Args:
    graph: A GraphAL object
  
  Returns:
    sort_result: A topological sortng of the vertices in the graph as a
                 list

  """
  if graph.adj_list is None:
    return None
  all_in_degrees = compute_indegree_every_vertex(graph)
  sort_result = list()
  
  # Python deque used here as queue
  queue = deque([])
  
  for i in range(len(all_in_degrees)):
    if all_in_degrees[i] == 0:
      queue.append(i)
  
  
  while len(queue) != 0:
    u = queue.popleft()
    sort_result.append(u)
    
    for adj_vertex in graph.get_adj_vertices(u):
      all_in_degrees[adj_vertex] -= 1
      
      if all_in_degrees[adj_vertex] == 0:
        queue.append(adj_vertex)
  # Returns None if a cycle is detected
  if len(sort_result) != len(graph.adj_list):
    return None
  
  return sort_result


def compute_indegree_every_vertex(graph):
  """
  Computes the indegree of every vertex in a graph object.
  
  Args:
    graph: A GraphAL object
  
  Returns:
    final: A list of the indegrees of every vertex

  """
  if graph.adj_list is None:
    return None
  final = [0] * len(graph.adj_list)
  for i in range(len(graph.adj_list)):
    temp = graph.adj_list[i]
    while temp != None:
      final[temp.item] += 1
      temp = temp.next
  return final


def kruskals(graph):
  """
  Implements Kruskal's algorithm on a graph object.
  
  Args:
    graph: A GraphAL object
  
  Returns:
    tree: The minimum spanning tree of the graph object as a list of
          edges. 
          Edges are in format [source_vertex, dest_vertex, weight]

  """
  if graph.adj_list is None:
    return None
  edges = list()
  for i in range(len(graph.adj_list)):
    temp = graph.adj_list[i]
    while temp != None:
      edges.append([i, temp.item, temp.weight])
      temp = temp.next

  def sort_key(elem):
    """
    Sort function for sorted. Sorts by weights
    Args:
      elem: An edge of a graph object in the format -
            [source_vertex, dest_vertex, weight]
      
    Returns:
      elem[2]: The weight of the edge
    """
    return elem[2]

  edges = sorted(edges, key=sort_key)
  tree = list()
  # A disjoint set forest is used here to detect cycles
  dsf = DisjointSetForest(len(graph.adj_list))
  for edge in edges:
    if dsf.find(edge[0]) != dsf.find(edge[1]):
      dsf.union(edge[0], edge[1])
      tree.append(edge)
    
  return tree
  
