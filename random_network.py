import random
from node import Node
from abstract_network import AbstractNetwork


class RandomNetwork(AbstractNetwork):
    """
    This network class inherits basic network functionality from the AbstractNetwork-class. It overwrites the
    __create_network__ function to create a random network.
    """
    
    def __create_network__(self, n_nodes, n_edges):
        """
        Creates a random network with the specified number of nodes and edges.
        1. build a list of n nodes
        2. create m edges between randomly selected nodes that are not yet connected
        (Hint: when adding an edge A --> B, do not forget to also add the edge B --> A)
        :param n_nodes: number of nodes
        :param n_edges: number of edges
        """
        # TODO
        nodes = []
       
        for i in range(n_nodes):
            nodes.append(Node(i))
        connected_node = 0
        while connected_node < n_edges:
            n = random.randint(0, n_nodes-1)
            m = random.randint(0, n_nodes-1)
            
            if n == m:
                continue
            if nodes[n].has_edge_to(nodes[m]):
                continue
            nodes[n].add_edge(nodes[m])
            connected_node += 1
        

        for node in nodes:
            self.nodes[node.identifier] = node
