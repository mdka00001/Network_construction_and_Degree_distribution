from node import Node
from random_network import RandomNetwork
from degree_distribution import DegreeDistribution
from tools import plot_distribution_comparison
from tools import poisson
from tools import poisson_histogram

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)

node_1.add_edge(node_2)
node_1.add_edge(node_3)

network = RandomNetwork(6, 6)  



node_1=network.get_node(1)

network.print()

n1=DegreeDistribution(network)
print(n1.normalisation())

n2 = poisson(n1, 2)

