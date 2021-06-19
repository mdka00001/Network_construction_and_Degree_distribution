import matplotlib.pyplot as plt
import math
from math import factorial
import numpy as np


def plot_distribution_comparison(histograms, legend, title):
    """
    Plots a list of histograms with matching list of descriptions as the legend.
    :param histograms: list of histograms
    :param legend: list of matching histogram names
    :param title: plot title
    """
    # TODO: determine length of the longest distribution
    # TODO: extend "shorter" distributions

    maximum_len = max(len(prob_1) for prob_1 in histograms)

    prob_2 = 0
    
    for p in histograms:
        if len(p) < maximum_len:
            prob_2 = maximum_len - len(p)
            for j in range(0, prob_2):
                p.append(0)






    # plots histograms, nothing to do here
    for histogram in histograms:
        plt.plot(range(len(histogram)), histogram, marker='x')
    
    # TODO: axis labels
    plt.xlabel ( "Degree")
    plt.ylabel("Degree_Distribution")
    
    # finish the plot, nothing to do here
    plt.legend(legend)
    plt.title(title)
    plt.tight_layout()
    plt.show()


def poisson(k, lamb):
    """
    :param k: observed events in an interval
    :param lamb: average number of events in an interval, (lambda is a Python keyword)
    :return: Poisson probability P(k) of observing k events in an interval
    """
    # TODO
    def poisson(k, lamb):
        poisson = (lamb ** k / factorial(k)) * np.exp(-lamb)
        return poisson


    


def poisson_histogram(n_nodes, n_edges, max_degree):
    """
    Generate a histogram of the Poisson distribution from degree 0 to max_degree.
    :param n_nodes: number of nodes
    :param n_edges: number of edges
    :param max_degree: maximum degree in the histogram
    :return: Poisson distribution histogram
    """
    # TODO
    lamda = 2.0*n_edges / float(n_nodes)
    PDH = [0]*(max_degree + 1)
    i = 0
    while i <= max_degree:
        PDH[i] = pow(lamda, i)*pow(math.e,-lamda ) / math.factorial(i)
        i = i + 1
    return PDH
    
