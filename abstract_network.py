class AbstractNetwork:
    """
    Abstract network definition. It cannot be instantiated (= you cannot create an AbstractNetwork-object).
    However, it can be inherited by other classes, which gives those other classes basic network functionality.
    """
    
    def __init__(self, n_nodes, n_edges):
        """
        Creates a network with the specified number of nodes and edges. There is nothing to do here.
        :param n_nodes: number of nodes
        :param n_edges: number of edges
        """
        # key = node ID, value = Node-object
        self.nodes = dict()
        # call the create network method of the respective sub-class
        self.__create_network__(n_nodes, n_edges)

    def __create_network__(self, n_nodes, n_edges):
        """
        Method overwritten by sub-classes. There is nothing to do here.
        :param n_nodes: number of nodes
        :param n_edges: number of edges
        """
        raise NotImplementedError

    def print(self):
        """
        Prints the network as a sorted adjacency list. For example:

        1: [2, 3]
        2: [1, 4]
        3: [1, 4]
        4: [2, 3]

    

        (Hint: you can make use of the __str__() function already implemented for each node.)
        """
        
        for k, node in self.nodes.items():
            print(str(node))

    def size(self):
        """
        :return: number of nodes in the network
        """
        return len(self.nodes)

    def add_node(self, node):
        """
        Adds a node to the network. If there is already a node with the same identifier in the network, simply
        overwrite it.
        :param node: Node-object
        """
        self.nodes[node.identifier]=node


    def get_node(self, identifier):
        """
        :param identifier: node ID
        :return: node with the given identifier
        :raise: KeyError if there is no node with that ID in the network
        """
        return self.nodes[identifier]

    def max_degree(self):
        """
        :return: highest node degree in the network
        """
       
        max_deg = 0
        for k, node in self.nodes.items():
         
            if node.degree()>max_deg:
                max_deg=node.degree()
        return max_deg

