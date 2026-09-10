import numpy as np
from chart_builders.trig_functions_graph import TrigFunctionsGraph
from chart_builders.distribution_graphs import DistributionGraph

def main():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

    trig_func_graph = TrigFunctionsGraph(x_range=x)
    trig_func_graph.build_graph(show=False, save_dir="charts", save_name='trig_functions')

    distribution_graphs = DistributionGraph(seed=2023, n_samples=1000)
    distribution_graphs.build_graph(show=False, save_dir="charts", save_name='histograms')


if __name__ == "__main__":
    main()



