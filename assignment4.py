"""
Name: Lim Zheng Haur
Student ID: 32023952
Assignment 4
FIT2004
"""
# =================================================================
# Question 01 // incomplete
# =================================================================

def allocate(preferences, sysadmins_per_night, max_unwanted_shifts, min_shifts):
    """
    This function returns a list of list of the allocation of sysadmins' night shifts

    Input: 
        preferences: a list of list representing employee's shift preferences
        sysadmins_per_night: an integer of the number employee needed per night
        max_unwanted_shifts: an integer of the maximum shift allocated to employee not in preference
        min_shifts: an integer of the minimum shift per employee
    Return:
        allocation: a list of list where allocation[i][j] is 1 if sysadmin[j] is allocated
                    to work on night[i] or 0 otherwise
        None: if there is no feasible solution
    Time complexity:
        Best: 
        Worst:
    Space complexity:
        Input: O(NM) where N = len(preferences) and M = len(list in preferences)
        Aux: 
    """
    #create a flow network
    flow_network = FlowNetwork(preferences, sysadmins_per_night, max_unwanted_shifts, min_shifts)
    #find the max flow
    # TODO

    #initialize allocation
    allocation = [None] * len(preferences)
    for i in range(len(allocation)):
        allocation[i] = [None] * len(preferences[0])

    #if flow_network is valid:
        #for flow in flow network
        #allocation[i][j] = 0/1
    return allocation
    # else:
    #     return None
    
class FlowNetwork:
    """
    class for a flow network
    """
    def __init__(self, preferences, sysadmins_per_night, max_unwanted_shifts, min_shifts):
        """
        flow network init function

        Input: 
            preferences: a list of list representing employee's shift preferences
            sysadmins_per_night: an integer of the number employee needed per night
            max_unwanted_shifts: an integer of the maximum shift allocated to employee not in preference
            min_shifts: an integer of the minimum shift per employee
        Return; 
            - 
        Time complexity:
            Best: O(NM) where N = len(preference) and M = len(list in preference)
            Worst: O(NM) where N = len(preference) and M = len(list in preference)
        Space complexity:
            Input: O(NM) where N = len(preference) and M = len(list in preference)
            Aux: O(N + M) where N = len(preference) and M = len(list in preference)
        """
        #source and target
        self.source = Vertex()
        self.target = Vertex()
        #set a
        self.sysadmins = []
        #set b
        self.unwanted_shifts = []
        self.preferred_shifts = []
        #set c
        self.nights = []
        
        # intialize vertex and edges
        for i in range(len(preferences)):
            self.nights.append(Vertex())
            self.nights[i].add_edge(Edge(i, 0, sysadmins_per_night, sysadmins_per_night))
        for i in range(len(preferences[0])):
            self.sysadmins.append(Vertex())
            self.unwanted_shifts.append(Vertex())
            self.preferred_shifts.append(Vertex())
            self.source.add_edge(Edge(0, i, min_shifts, len(preferences)))
            self.sysadmins[i].add_edge(Edge(i, i, 0, len(preferences)))
            self.sysadmins[i].add_edge(Edge(i, i, 0, max_unwanted_shifts))
        for i in range(len(preferences)):
            for j in range(len(preferences[i])):
                if preferences[i][j] == 1:
                    self.preferred_shifts[j].add_edge(Edge(j, i, 0, 1))
                else:
                    self.unwanted_shifts[j].add_edge(Edge(j, i, 0, 1)) 

    def ford_fulkerson(self):
        """
        ford fulkerson alogrithm to find max flow
        """
        # TODO
        pass
    

class Vertex:
    """
    class for a vertex
    """
    def __init__(self):
        """
        vertex class init function
        """
        self.edges = []

    def add_edge(self, edge):
        """
        function to add edge to vertex
        """
        self.edges.append(edge)

class Edge:
    """
    class for a edge
    """
    def __init__(self, u, v, lower_bound, capacity):
        """
        edge class init function
        """
        self.u = u
        self.v = v
        self.flow = 0
        self.lower_bound = lower_bound
        self.capacity = capacity


# =================================================================
# Question 02
# =================================================================

class EventsTrie:
    """
    class for a Events Trie
    """
    def __init__(self, timelines):
        """
        EventsTrie class init function
        
        Input: 
            timelines: a list of strings
        Return:
            - 
        Time complexity:
            Best: O(NM^2) where N = len(timelines) and M = len(string in timelines)
            Worst: O(NM^2) where N = len(timelines) and M = len(string in timelines)
        Space complexity:
            Input: O(NM) where N = len(timelines) and M = len(string in timelines)
            Aux: O(NM) where N = len(timelines) and M = len(string in timelines) 
        """
        self.root = Node()
        # for each word, insert into Trie
        for i in range(len(timelines)):
            self.insert(timelines[i])

    def getLongestChain(self, noccurence):
        """
        This function returns the longest chain in Trie with at least noccurence

        Input: 
            noccurence: an integer of minimum occurence
        Return:
            longest_chain: the longest chain with minimum occurence of noccurence 
            None: no valid chain found
        Time complexity:
            Best: O(1) where no longest chain with minimum occurence of noccurence is in Trie
            Worst: O(K) where K = len(longest chain with minimum occurence of noccurence)
        """
        def getLongestChain_aux(current, longestChain = "", string = ""):
            """
            This function is the recursion function of getLongestChain

            Input: 
                current: the current Node
                longestChain: the current longest chain found
                string: the current chain of events from root to current Node
            """
            # base case
            # if occurence >= noccurence
            # if length > longestchain length
            # update longest chain
            if current.occurence >= noccurence and current.length > len(longestChain):
                longestChain = string
            # perform recursion on each link if link exists
            for i in range(1, len(current.link)):
                if current.link[i] is not None and current.link[i].occurence >= noccurence:
                    # recursion
                    longestChain = getLongestChain_aux(current.link[i], longestChain, (string + chr(i + 97 - 1)))
            # return
            return longestChain
        # starts the recursion function from root
        longest_chain = getLongestChain_aux(self.root)
        # if not empty string, return
        if len(longest_chain) > 0:
            return longest_chain
        # else return None
        return None

    def insert(self, events):
        """
        This function inserts all suffix of input string into EventsTrie

        Input: 
            events: a string to input all suffix of into trie
        Return:
            -
        Time complexity: 
            Best: O(N^2) where N = len(events)
            Worst: O(N^2) where N = len(events)
        Space complexity:
            Input: O(N) where N = len(events)
            Aux: O(N) where N = len(events)
        """
        def insert_aux(events, pos, nodes):
            """
            Recursive function for insert()

            Input:
                events: a string to input all suffix
                pos: the current position of character to insert
                nodes: a list of nodes to add the current character to
            Return: 
                -
            """
            # base case
            # if pos == len(events), add terminal $
            if pos == len(events):
                for i in range(len(nodes)):
                    if nodes[i].link[0] is None:
                        nodes[i].link[0] = Node()
                    nodes[i].link[0].length = nodes[i].length + 1
            # recursion
            else:
                # find index
                index = ord(events[pos]) - 97 + 1
                # add character to all node in nodes
                for i in range(len(nodes)):
                    if nodes[i].link[index] is not None:
                        nodes[i] = nodes[i].link[index]
                        nodes[i].occurence += 1
                    else:
                        nodes[i].link[index] = Node()
                        nodes[i].link[index].length = nodes[i].length + 1
                        nodes[i] = nodes[i].link[index]
                # add character to root
                if self.root.link[index] is not None:
                    nodes.append(self.root.link[index])
                    self.root.link[index].occurence += 1
                else:
                    self.root.link[index] = Node()
                    nodes.append(self.root.link[index])
                # add next character
                insert_aux(events, pos + 1, nodes)
        # add the character recursively from pos = 0
        insert_aux(events, 0, [])
            
    
class Node:
    """
    class for a Node
    """
    def __init__(self):
        """
        Node class init function
        """
        self.link = [None] * 27
        self.occurence = 1
        self.length = 1


if __name__ == "__main__":
    # something here
    trie = EventsTrie(["abc", "dbcef", "gdbc"])
    longestChain2 = trie.getLongestChain(2)
    longestChain3 = trie.getLongestChain(3)
    longestChain4 = trie.getLongestChain(4)
    if longestChain2 == "dbc" and longestChain3 == "bc" and longestChain4 is None:
        print("working")

