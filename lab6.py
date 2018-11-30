"""
CS 2302
Mark Williams
Lab 6
Diego Aguirre/Manoj Saha
Last Modified: 11-30-18
Purpose: Implement topological sort and Kruskal's algorithm
"""

from lab6utils import topological_sort
from lab6utils import kruskals
from GraphAL import GraphAL


def main():
  print("For reults in Kruskal's algorithm, edges are formatted as:")
  print("[source, dest, weight].")
  print()
  # Kruskal Graph 1
  # 0--1
  # |\/|
  # |/\|
  # 2--3
  graph_kruskals = GraphAL(initial_num_vertices=4, is_directed=False)

  graph_kruskals.add_edge(0, 1, 6.0)
  graph_kruskals.add_edge(1, 3, 4.0)
  graph_kruskals.add_edge(0, 3, 3.0)
  graph_kruskals.add_edge(2, 3, 2.0)
  graph_kruskals.add_edge(0, 2, 1.0)
  graph_kruskals.add_edge(1, 2, 5.0)
  print("A minimum spanning tree for graph 1 can be created from the\
 following edges:")
  for value in kruskals(graph_kruskals):
    print(value)
  
  # Kruskal Graph 2
  # 0--1
  # | /|\4
  # |/ |/
  # 2--3
  graph_kruskals = None
  graph_kruskals = GraphAL(initial_num_vertices=5, is_directed=False)

  graph_kruskals.add_edge(0, 1, 6.0)
  graph_kruskals.add_edge(1, 3, 4.0)
  graph_kruskals.add_edge(2, 3, 6.0)
  graph_kruskals.add_edge(0, 2, 1.0)
  graph_kruskals.add_edge(1, 2, 3.0)
  graph_kruskals.add_edge(1, 4, 2.0)
  graph_kruskals.add_edge(3, 4, 8.0)

  print("A minimum spanning tree for graph 2 can be created from the\
 following edges:")
  for value in kruskals(graph_kruskals):
    print(value)
  
  # Kruskal Graph 3
  # 0--1
  # | /|\
  # |/ | \
  # 2--3--4
  graph_kruskals = None
  graph_kruskals = GraphAL(initial_num_vertices=5, is_directed=False)

  graph_kruskals.add_edge(0, 1, 7.0)
  graph_kruskals.add_edge(1, 3, 2.0)
  graph_kruskals.add_edge(2, 3, 1.0)
  graph_kruskals.add_edge(0, 2, 10.0)
  graph_kruskals.add_edge(1, 2, 8.0)
  graph_kruskals.add_edge(1, 4, 6.0)
  graph_kruskals.add_edge(3, 4, 3.0)
  
  print("A minimum spanning tree for graph 3 can be created from the\
 following edges:")
  for value in kruskals(graph_kruskals):
    print(value)

  print()
  # Topological Sort Graph 1
  #   /--> 1 -> 4 -> 7 -\
  #  /                   \
  # 0 -> 2 -> 5 -> 8------> 10
  #  \                  /
  #  \--> 3 -> 6 -> 9--/
  print("The topological order of vertices in  graph 1 is as follows:")
  graph_topological = GraphAL(initial_num_vertices=11, is_directed=True)

  graph_topological.add_edge(0, 1)
  graph_topological.add_edge(0, 2)
  graph_topological.add_edge(0, 3)

  graph_topological.add_edge(1, 4)
  graph_topological.add_edge(2, 5)
  graph_topological.add_edge(3, 6)

  graph_topological.add_edge(4, 7)
  graph_topological.add_edge(5, 8)
  graph_topological.add_edge(6, 9)

  graph_topological.add_edge(7, 10)
  graph_topological.add_edge(8, 10)
  graph_topological.add_edge(9, 10)
  print(topological_sort(graph_topological))
  
  # Topological Sort Graph 2
  #   /----->1 
  #  /      /
  # 0 <- 2<-
  
  print("The topological order of vertices in graph 2 is as follows:")
  graph_topological = None
  graph_topological = GraphAL(initial_num_vertices=3, is_directed=True)
  graph_topological.add_edge(0, 1)
  graph_topological.add_edge(1, 2)
  graph_topological.add_edge(2, 0)
  print(topological_sort(graph_topological))
  
  # Topological Sort Graph 3
  #   /------>1 --->2
  #  /            /
  # 0 --> 3------/
  
  print("The topological order of vertices in  graph 3 is as follows:")
  graph_topological = None
  graph_topological = GraphAL(initial_num_vertices=4, is_directed=True)
  graph_topological.add_edge(0, 1)
  graph_topological.add_edge(1, 2)
  graph_topological.add_edge(0, 3)
  graph_topological.add_edge(3, 2)
  print(topological_sort(graph_topological))

main()
