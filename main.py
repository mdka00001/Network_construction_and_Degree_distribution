import tools
from time import time
from random_network import RandomNetwork
from degree_distribution import DegreeDistribution


# NOTHING TO DO HERE
def plot(title, data):
    plot_data = []
    plot_legend = []

    print(title + ':')
    for n_nodes, n_edges in data:
        print('\tnodes: {0:,}, edges: {1:,}'.format(n_nodes, n_edges))
        # build random network
        start = time()
        network = RandomNetwork(n_nodes, n_edges)
        print('\t--> generated random network in {0:.2f}s'.format(time() - start))
        # compute the normalised degree distribution histogram
        start = time()
        plot_data.append(DegreeDistribution(network).normalisation())
        plot_legend.append('r: {0:,}/{1:,}'.format(n_nodes, n_edges))
        print('\t--> computed degree distribution in {0:.2f}s'.format(time() - start))

        # build the histogram of the Poisson distribution
        start = time()
        plot_data.append(tools.poisson_histogram(n_nodes, n_edges, network.max_degree()))
        plot_legend.append('p: {0:,}/{1:,}'.format(n_nodes, n_edges))
        print('\t--> computed Poisson distribution in {0:.2f}s'.format(time() - start))

    tools.plot_distribution_comparison(plot_data, plot_legend, title)

plot('Plot 1', [(50, 100), (500, 1000), (5000, 10000), (50000, 100000)])
plot('Plot 2', [(20000, 5000), (20000, 17000), (20000, 40000), (20000, 70000)])


