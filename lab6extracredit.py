from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses <= 0:
            return True
        graph = GraphAL(initial_num_vertices = numCourses, is_directed = True)
        for value in prerequisites:
            graph.add_edge(value[1], value[0])
        return Solution.topological_sort(graph) != None
     
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses <= 0:
            return True
        graph = GraphAL(initial_num_vertices = numCourses, is_directed = True)
        for value in prerequisites:
            graph.add_edge(value[1], value[0])
        return Solution.topological_sort(graph)
    
    
    def topological_sort(graph):

        if graph.adj_list is None:
            return None
        all_in_degrees = Solution.compute_indegree_every_vertex(graph)
        sort_result = list()

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

        if len(sort_result) != len(graph.adj_list):
            return None

        return sort_result


    def compute_indegree_every_vertex(graph):
        if graph.adj_list is None:
            return None
        final = [0] * len(graph.adj_list)
        for i in range(len(graph.adj_list)):
            temp = graph.adj_list[i]
            while temp != None:
                final[temp.item] += 1
                temp = temp.next
        return final

     
class GraphALNode:
    def __init__(self, item, next, weight):
        self.item = item
        self.weight = weight 
        self.next = next


class GraphAL:

    def __init__(self, initial_num_vertices, is_directed):
        self.adj_list = [None] * initial_num_vertices
        self.is_directed = is_directed

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.adj_list)

    def add_vertex(self):
        self.adj_list.append(None)

        return len(self.adj_list) - 1  # Return new vertex id

    def add_edge(self, src, dest, weight = 1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        #  TODO: What if src already points to dest?
        self.adj_list[src] = GraphALNode(dest, self.adj_list[src], weight)

        if not self.is_directed:
            self.adj_list[dest] = GraphALNode(src, self.adj_list[dest], weight)

    def remove_edge(self, src, dest):
        self.__remove_directed_edge(src, dest)

        if not self.is_directed:
            self.__remove_directed_edge(dest, src)

    def __remove_directed_edge(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        if self.adj_list[src] is None:
            return

        if self.adj_list[src].item == dest:
            self.adj_list[src] = self.adj_list[src].next
        else:
            prev = self.adj_list[src]
            cur = self.adj_list[src].next

            while cur is not None:
                if cur.item == dest:
                    prev.next = cur.next
                    return

                prev = prev.next
                cur = cur.next

    def get_num_vertices(self):
        return len(self.adj_list)

    def get_vertices_reachable_from(self, src):
        reachable_vertices = set()

        temp = self.adj_list[src]

        while temp is not None:
            reachable_vertices.add(temp.item)
            temp = temp.next

        return reachable_vertices

    def get_vertices_that_point_to(self, dest):
        vertices = set()

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                if temp.item == dest:
                    vertices.add(i)
                    break

                temp = temp.next

        return vertices
    
    def get_highest_cost_edge(self):
        most = 0
        for node in self.adj_list:
            temp = node
            while temp != None:
                most = max(most, temp.weight)
                temp = temp.next
        return most

    def get_num_edges(self):
        counter = 0
        for node in self.adj_list:
            temp = node
            while temp != None:
                counter += 1
                temp = temp.next
        return counter

    def get_edge_weight(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return 0
        temp = self.adj_list[src]
        while temp.item != dest:
            temp =temp.next
        return temp.weight

    def reverse_edges(self):
        if not self.is_directed:
            return
        temp_list = [None] * len(self.adj_list)
        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]
            while temp != None:
                temp_list[temp.item] = \
                    GraphALNode(i, temp_list[temp.item], temp.weight)
                temp = temp.next
        self.adj_list = temp_list
    
    def num_self_edges(self):
        counter = 0
        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]
            while temp != None:
                if temp.item == i:
                    counter += 1
                temp = temp.next
        return counter
    
    def get_adj_vertices(self, vertex):
        if vertex >= len(self.adj_list):
            return None
        adj = list()
        temp = self.adj_list[vertex]
        while temp != None:
            adj.append(temp.item)
            temp = temp.next
        return adj



