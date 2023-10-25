"""
Name: Lim Zheng Haur
Student ID: 32023952
Assignment 2
FIT2004
"""

# =================================================================
# Question 01
# =================================================================

def ideal_place(relevant):
    """
    This function returns a single pair of coordinates that have minimal distance to
    all coordinates in relevant

    Precondition: relevant is not empty
    Postcondition:

    Input:
        relevant: a list of coordinates [x,y]
    Return:
        [x, y]: a pair of coordinate
    Time complexity: 
        Best: O(N) where N = len(lst)
        Worst: O(N) where N = len(lst)
    Space complexity: 
        Input: O(N) where N = len(lst)
        Aux: O(N) where N = len(lst)

    """
    # initialize x and y list
    x_lst = []
    y_lst = []

    # append x to x list and y to y list
    for i in range(len(relevant)):
        x_lst.append(relevant[i][0])
        y_lst.append(relevant[i][1])
    
    # return [x,y]: x = median of x list, y = median of y list
    return [quick_select_median(x_lst), quick_select_median(y_lst)]

def quick_select_median(lst):
    """
    This function selects the median of the input list

    Precondition: 
    Postcondition:

    Input:
        lst: a numeric list
    Return:
        the median of lst
    Time complexity: 
        Best: O(N) where N = len(lst)
        Worst: O(N) where N = len(lst)
    Space complexity: 
        Input: O(N) where N = len(lst)
        Aux: O(N) where N = len(lst)

    """
    # initialize all arguments
    med = len(lst)//2
    start = 0
    end = len(lst) - 1

    # return item from list at median
    return lst[quick_select(lst, start, end, med)]
    
def quick_select(lst, start, end, ind):
    """
    This is a recursive function that selects the item at input index from the input list

    Precondition: 
    Postcondition:

    Input:
        lst: a numeric list
        start: starting index to quick select
        end: ending index to quick select
        ind: index of element to be selected
    Return:
        pivot_start: index of the pivot (item to be quick selected)
    Time complexity: 
        Best: O(N) where N = len(lst)
        Worst: O(N) where N = len(lst)
    Space complexity: 
        Input: O(N) where N = len(lst)
        Aux: O(N) where N = len(lst)

    """
    # partitioning
    pivot_start, pivot_end = partition(lst, start, end)
    # if item is on the left
    if pivot_start > ind:
        return quick_select(lst, start, pivot_start - 1, ind)
    # if item is on the right
    elif pivot_end < ind:
        return quick_select(lst, pivot_end + 1, end, ind)
    # if item is within pivot_start and pivot_end
    else: 
        return pivot_start

def partition(lst, start, end):
    """
    This function partitions the list from index start to index end by a pivot chosen 
    using median of median of all values from index start to index end.
    This function uses Dutch National Flag algorithm.

    Precondition: 
    Postcondition:

    Input:
        lst: a numeric list
        start: index to start partition
        end: index to end partition
    Return:
        boundary1: starting index of pivot
        boundary2: ending index of pivot
        
    Time complexity: 
        Best: O(N) where N = end - start
        Worst: O(N) where N = end - start
    Space complexity: 
        Input: O(N) where N = len(lst)
        Aux: O(N) where N = end = start

    """
    # finding median of median of lst[start] to lst[end]
    find = []
    for i in range(start, end + 1):
        find.append(lst[i])
    pivot = median_of_median(find)

    # Dutch National Flag method
    # initialize boundary and pointer
    boundary1 = start
    boundary2 = end
    j = start

    # loop to partition
    while j <= boundary2:
        if lst[j] < pivot:
            lst[boundary1], lst[j] = lst[j], lst[boundary1]
            boundary1 += 1
            j += 1
        elif lst[j] > pivot:
            lst[boundary2], lst[j] = lst[j], lst[boundary2]
            boundary2 -= 1
        else:
            j += 1

    # return both boundary
    return boundary1, boundary2


def median_of_median(lst):
    """
    This function returns the median of median of lst

    Precondition: 
    Postcondition:

    Input:
        lst: a numeric list
    Return:
        median of median of lst
    Time complexity: 
        Best: O(N) where N = len(lst)
        Worst: O(N) where N = len(lst)
    Space complexity: 
        Input: O(N) where N = len(lst)
        Aux: O(N) where N = len(lst)

    """
    # base case
    if len(lst) == 1:
        return lst[0]

    else:
        # sorting by 5 element in list
        for i in range(4, len(lst), 5):
            insertion_sort(lst, i-3, i)
        if len(lst) % 5 != 0:
            insertion_sort(lst, (len(lst)//5) * 5 + 1, len(lst) - 1)

        # appending median of group of 5 into new list called middle
        middle = []
        for i in range(4, len(lst), 5):
            middle.append(lst[i-2])
        if len(lst) % 5 != 0:
            ind = ((len(lst)//5)*5 + len(lst) - 1)//2
            middle.append(lst[ind])

        # find median of median of middle list
        return median_of_median(middle)

def insertion_sort(lst, start, end):
    """
    This function sorts the input list from index start to index end

    Precondition: 
    Postcondition: lst is sorted from lst[start] to lst[end]

    Input:
        lst: a numeric list
        start: index to start sorting
        end: index to end sorting
    Return:
        n/a
    Time complexity: 
        Best: O(N) where N = len(lst) // when lst[start] to lst[end] is already sorted
        Worst: O(N^2) where N = end - start
    Space complexity: 
        Input: O(N) where N = end - start
        Aux: O(1)

    """
    # for each item from start to end
    for i in range(start, end + 1):
        key = lst[i]
        j = i-1
        # insertion sort
        while j>= (start -1) and key <lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key

# =================================================================
# Question 02
# =================================================================

class RoadGraph:
    """
    Graph class for Question02 of Assignment02
    """

    def __init__(self, roads):
        """
        This is the init function of RoadGraph class

        Precondition: 
        Postcondition:

        Input:
            roads: a list of tuples containing edges data
        Return:
            n/a
        Time complexity: 
            Best: O(N) where N = len(roads)
            Worst: O(N) where N = len(roads)
        Space complexity: 
            Input: O(N) where N = len(roads)
            Aux: O(N) where N = len(roads)

        """
        # obtaining number of vertices
        vertices_list = []
        for i in range(len(roads)):
            vertices_list.append(roads[i][0])
            vertices_list.append(roads[i][1])
        vertices_count = max(vertices_list) + 1

        # initializing vertices list
        self.vertices = [None] * vertices_count
        for i in range(vertices_count):
            self.vertices[i] = Vertex(i)
        
        # adding edges to graph
        self.add_edges(roads)
            
    def routing(self, start, end, chores_location):
        """
        This function computes the shortest route from start to end while
        passing by 1 location from chores_location

        Precondition: 
        Postcondition:

        Input:
            start: id of starting vertex
            end: id of ending vertex
            chores_location: a list of vertex id to pass through
        Return:
            path: a list of vertex id according to the path from start to end
            None: if no path is possible
        Time complexity: 
            Best: O(N) where N = len(vertices)
            Worst: O(N) where N = len(vertices)
        Space complexity: 
            Input: O(N) where N = len(vertices)
            Aux: O(N) where N = len(vertices)

        """
        # create a reversed graph
        rev_roads = []
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices[i].edges)):
                v = self.vertices[i].edges[j].u
                u = self.vertices[i].edges[j].v
                w = self.vertices[i].edges[j].w
                edge = (u,v,w)
                rev_roads.append(edge)
        rev_graph = RoadGraph(rev_roads)

        # perform dijkstra on both graphs
        dijkstra(self, start)
        dijkstra(rev_graph, end)
        
        # calculate distance passing through each chore
        dist = []
        for i in range(len(chores_location)):
            chore = chores_location[i]
            dist_start = self.vertices[chore].distance
            dist_dest = rev_graph.vertices[chore].distance
            if dist_start != -1 and dist_dest != -1:
                total_dist = dist_start + dist_dest
                dist.append((total_dist, chore))
        
        # finding minimum distance among all chores
        min_dist = None
        chore = None
        if len(dist) > 0:
            min_dist = dist[0][0]
            chore = dist[0][1]
        for i in range(len(dist)):
            if dist[i][0] < min_dist:
                min_dist = dist[i][0]
                chore = dist[i][1]

        # return None if no possible path
        if chore is None:
            return None
        
        # backtrack from chore to start
        path_start = []
        current = self.vertices[chore]
        while current is not self.vertices[start]:
            current = current.previous
            path_start.append(current)
        
        # backtrack from chore to end
        path_dest = []
        current = rev_graph.vertices[chore]
        while current is not rev_graph.vertices[end]:
            current = current.previous
            path_dest.append(current)
        
        # combine start to chore and chore to end
        path = []
        for i in range(len(path_start) - 1, -1, -1):
            path.append(path_start[i].id)
        path.append(chore)
        for i in range(len(path_dest)):
            path.append(path_dest[i].id)

        # return path
        return path

    def add_edges(self, edges):
        """
        This function add edges to the graph according to the input list

        Precondition: 
        Postcondition:

        Input:
            edges: a list of tuples
        Return:
            n/a
        Time complexity: 
            Best: O(N) where N = len(edges)
            Worst: O(N) where N = len(edges)
        Space complexity: 
            Input: O(N) where N = len(edges)
            Aux: O(1)

        """
        for edge in edges:
            u = edge[0] # from this vertex
            v = edge[1] # to this vertex
            w = edge[2] # weight of vertex

            # create edge
            edge = Edge(u,v,w)

            # add to vertex
            vertex = self.vertices[u]
            vertex.add_edge(edge)

def dijkstra(graph, source):
    """
        This function computes the distance of all vertices to the source vertex

        Precondition: 
        Postcondition:

        Input:
            graph: the graph to traverse
            source: the id of the source vertex
        Return:
            n/a
        Time complexity: 
            Best: O(N) where N = len(graph.vertices)
            Worst: O(N) where N = len(graph.vertices)
        Space complexity: 
            Input: O(N) where N = len(graph.vertices)
            Aux: O(N) where N = len(graph.vertices)

        """
    # reset vertices
    for i in range(len(graph.vertices)):
        graph.vertices[i].distance = -1
        graph.vertices[i].discovered = False
        graph.vertices[i].visited = False
        graph.vertices[i].previous = None
        
    # source vertex
    graph.vertices[source].distance = 0
    graph.vertices[source].discovered = True
    # create heap
    discovered = MinHeap()
    # add source to heap
    discovered.append(graph.vertices[source])

    # until no more vertex could be traversed
    while len(discovered) > 0:

        # serve from heap
        u = discovered.serve()
        u.visited = True

        # perform edge relaxation on all adjacent vertices
        for edge in u.edges:
            v = graph.vertices[edge.v]

            # if not discovered yet
            if v.discovered == False:
                v.discovered = True
                v.distance = u.distance + edge.w
                v.previous = u
                discovered.append(v)

            # it is in heap, but not yet finalize
            else:
                if v.distance > u.distance + edge.w:
                    # update distance and previous
                    v.distance = u.distance + edge.w
                    v.previous = u
                    # update heap
                    discovered.update(v)

class MinHeap:
    """
    MinHeap class for Dijkstra algorithm implementation.
    Referenced to FIT1008 MaxHeap implementation.
    Modified to suit storing Vertex objects.
    """
    def __init__(self):
        """
        This is the init function for MinHeap class.

        Precondition: 
        Postcondition:

        Input:
            n/a
        Return:
            n/a
        Time complexity: 
            Best: O(1)
            Worst: O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)

        """
        self.length = 0
        self.array = [] 
    
    def __len__(self):
        """
        This function returns the length of MinHeap

        Precondition: 
        Postcondition:

        Input:
            n/a
        Return:
            length of MinHeap
        Time complexity: 
            Best: O(1)
            Worst: O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)

        """
        return self.length
    
    def append(self, element):
        """
        This function appends new element into MinHeap

        Precondition: 
        Postcondition:

        Input:
            element: item to be added to MinHeap
        Return:
            n/a
        Time complexity: 
            Best: O(1) when item do not need to rise
            Worst: O(logN) where N = len(MinHeap) // when item rise to root
        Space complexity: 
            Input: O(1)
            Aux: O(1)

        """
        # adding element to MinHeap
        self.length += 1
        while self.length > len(self.array) - 1:
            self.array.append(None)
        self.array[self.length] = element

        # rise the element
        self.rise(self.length)
    
    def rise(self, k):
        """
        This function rises the item at index k

        Precondition: 
        Postcondition:

        Input:
            k: index of item to be risen
        Return:
            n/a
        Time complexity: 
            Best: O(1) when item could not rise
            Worst: O(logN) where N = len(MinHeap) // when item rises to root
        Space complexity: 
            Input: O(1)
            Aux: O(1)

        """
        item = self.array[k]
        # if parent > item, rise
        while k > 1 and item.distance < self.array[k // 2].distance:
            self.array[k] = self.array[k // 2]
            k = k // 2
        self.array[k] = item

    def sink(self, k):
        """
        This function sinks the item at index k

        Precondition: 
        Postcondition:

        Input:
            k: index of item to be sunken
        Return:
            n/a
        Time complexity: 
            Best: O(1) when item could not be sunken
            Worst: O(logN) where N = len(MinHeap) // when item sunk from root to lowest level
        Space complexity: 
            Input: O(1)
            Aux: O(1)

        """
        item = self.array[k]
        # if smallest child < item, sink
        while 2 * k <= self.length:
            min_child  = self.smallest_child(k)
            # if smallest child > item, stop
            if self.array[min_child].distance >= item.distance:
                break
            self.array[k] = self.array[min_child]
            k = min_child
        self.array[k] = item

    def smallest_child(self, k):
        """
        This function returns the smallest child of item at index k

        Precondition: 
        Postcondition:

        Input:
            k: index of item to be searched
        Return:
            n/a
        Time complexity: 
            Best: O(1)
            Worst: O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)

        """
        # if item only have 1 child or left child < right child
        if 2 * k == self.length or \
                self.array[2 * k].distance < self.array[2 * k + 1].distance:
            return 2 * k
        # else right child < left child
        else:
            return 2 * k + 1
        
    def serve(self):
        """
        This function serves the minimum item in MinHeap

        Precondition: 
        Postcondition:

        Input:
            n/a
        Return:
            minimum item in MinHeap
        Time complexity: 
            Best: O(1)
            Worst: O(logN) where N = len(MinHeap) // cost of sink()
        Space complexity: 
            Input: O(1)
            Aux: O(1)

        """
        # min item
        min_elt = self.array[1]

        # update length
        self.length -= 1

        # move last item to root and sink
        if self.length > 0:
            self.array[1] = self.array[self.length + 1]
            self.sink(1)

        # return min item
        return min_elt

    def update(self, vertex):
        """
        This function updates the input item to the correct position in MinHeap

        Precondition: 
        Postcondition:

        Input:
            vertex: item to be updated
        Return:
            n/a
        Time complexity: 
            Best: O(1)
            Worst: O(N) where N = len(MinHeap) 
        Space complexity: 
            Input: O(1)
            Aux: O(1)

        """
        # find vertex in heap
        for i in range(len(self.array)):
            if self.array[i] is vertex:
                k = i
                break
        # rise vertex
        self.rise(k)

    def __str__(self):
        """
        This function represents the MinHeap object as a string

        Precondition: 
        Postcondition:

        Input:
            n/a
        Return:
            the array of the MinHeap
        Time complexity: 
            Best: O(1)
            Worst: O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)

        """
        return self.array

class Vertex:
    """
    Vertex class for vertex object in RoadGraph
    Referenced from FIT2004
    """
    def __init__(self, id):
        """
        This function is the init function for Vertex class

        Precondition: 
        Postcondition:

        Input:
            id: id of the vertex
        Return:
            n/a
        Time complexity: 
            Best: O(1)
            Worst: O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)

        """
        self.id = id

        # adjacency list
        self.edges = []
        
        # for traversal
        self.discovered = False
        self.visited = False

        # distance
        self.distance = -1

        # backtracking
        self.previous = None
    
    def add_edge(self, edge):
        """
        This function adds a edge into edges list

        Precondition: 
        Postcondition:

        Input:
            edge: an edge object
        Return:
            n/a
        Time complexity: 
            Best: O(1)
            Worst: O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)

        """
        self.edges.append(edge)

    def __str__(self):
        """
        This function represents the Vertex objet as a string

        Precondition: 
        Postcondition:

        Input:
            n/a
        Return:
            return_string: a string containing vertex id and a list of edges
        Time complexity: 
            Best: O(N) where N = len(edges)
            Worst: O(N) where N = len(edges)
        Space complexity: 
            Input: O(1)
            Aux: O(N) where N = len(edges)

        """
        return_string = str(self.id)
        for edge in self.edges:
            return_string = return_string + "\n" +  "with edges " + str(edge)
        return return_string

class Edge:
    """
    Edge class for edge object in vertices
    Referenced from FIT2004
    """
    def __init__(self, u, v, w):
        """
        This function is the init function for Edge class

        Precondition: 
        Postcondition:

        Input:
            u: starting vertex id
            v: ending vertex id
            w: weight of edge
        Return:
            n/a
        Time complexity: 
            Best: O(1)
            Worst: O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)

        """
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        """
        This function represents the edge object as a string

        Precondition: 
        Postcondition:

        Input:
            n/a
        Return:
            return_string: a string containing the u, v, w of the edge
        Time complexity: 
            Best: O(1)
            Worst: O(1)
        Space complexity: 
            Input: O(1)
            Aux: O(1)

        """
        return_string = str(self.u) + "," + str(self.v) + "," + str(self.w)
        return return_string

if __name__ == "__main__":
    relevant = [[5,8], [7,5], [9, 1], [0,7], [1,9], [2,1]]
    ideal_place(relevant)
    roads = [(0,1,4), (0,3,2), (0,2,3), (2,3,2), (3,0,3)]
    mygraph = RoadGraph(roads)
    mygraph.routing(0, 1, [2,3])
