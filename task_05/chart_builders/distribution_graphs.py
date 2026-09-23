import numpy as np
import matplotlib.pyplot as plt

def save_graph(save_dir: str, name: str):
    import os
    os.makedirs(save_dir, exist_ok=True)
    plt.savefig(f'{save_dir}/{name}.png', dpi=300)

class DistributionGraph:
    def __init__(self, seed: int = 2023, n_samples: int = 1000, norm_loc = 0, norm_scale = 1, uniform_low = -3, uniform_high = 3, exp_scale = 1.5):
        self.seed = seed
        self.n_samples = n_samples
        self.norm_data = None
        self.uniform_data = None
        self.exp_data = None
        self.norm_loc = norm_loc
        self.norm_scale = norm_scale
        self.uniform_low = uniform_low
        self.uniform_high = uniform_high
        self.exp_scale = exp_scale

        self.setup_distribution()

    def setup_distribution(self):
        self.norm_data = np.random.normal(loc=self.norm_loc, scale=self.norm_scale, size=self.n_samples)
        self.uniform_data = np.random.uniform(low=self.uniform_low, high=self.uniform_high, size=self.n_samples)
        self.exp_data = np.random.exponential(scale=self.exp_scale, size=self.n_samples)

    def build_graph(self, show: bool = True, save_dir: str = None, save_name: str = 'histograms'):
        fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

        axes[0].hist(self.norm_data, bins=30, color='#2b5c8f', edgecolor='black', alpha=0.7)
        axes[0].set_title(f'Нормальное (μ={self.norm_loc}, σ={self.norm_scale})', fontweight='bold')
        axes[0].set_xlabel('Значение')
        axes[0].set_ylabel('Частота')
        axes[0].grid(True, linestyle=':', alpha=0.6)

        axes[1].hist(self.uniform_data, bins=30, color='#d95f02', edgecolor='black', alpha=0.7)
        axes[1].set_title(f'Равномерное ({self.uniform_low}, {self.uniform_high})', fontweight='bold')
        axes[1].set_xlabel('Значение')
        axes[1].set_ylabel('Частота')
        axes[1].grid(True, linestyle=':', alpha=0.6)

        axes[2].hist(self.exp_data, bins=30, color='#7570b3', edgecolor='black', alpha=0.7)
        axes[2].set_title(f'Экспоненциальное (scale={self.exp_scale})', fontweight='bold')
        axes[2].set_xlabel('Значение')
        axes[2].set_ylabel('Частота')
        axes[2].grid(True, linestyle=':', alpha=0.6)

        fig.suptitle('Сравнение распределений случайных выборок', fontsize=16, fontweight='bold')
        plt.tight_layout()

        if save_dir is not None:
            save_graph(save_dir=save_dir, name=save_name)

        if show:
            plt.show()

        plt.close()


