import numpy as np
from chart_builders.trig_functions_graph import TrigFunctionsGraph
from chart_builders.distribution_graphs import DistributionGraph

output_dir = "charts"

def main():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

    trig_func_graph = TrigFunctionsGraph(x_range=x)
    trig_func_graph.build_graph(show=False, save_dir=output_dir, save_name='trig_functions')

    distribution_graphs = DistributionGraph(seed=2023, n_samples=1000)
    distribution_graphs.build_graph(show=False, save_dir=output_dir, save_name='histograms')

    print(f'Все графики успешно построены и сохранены в папке "/{output_dir}"')


if __name__ == "__main__":
    main()



