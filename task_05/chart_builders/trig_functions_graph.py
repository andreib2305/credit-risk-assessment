import numpy as np
import matplotlib.pyplot as plt


def save_graph(save_dir: str, name: str):
    import os
    os.makedirs(save_dir, exist_ok=True)
    plt.savefig(f'{save_dir}/{name}.png', dpi=300)

class TrigFunctionsGraph:
    def __init__(self, x_range: int):
        self.x = x_range
        self.y_sin = None
        self.y_cos = None
        self.y_tan = None
        self.function_evaluation()
        self.set_limits()

    def function_evaluation(self):
        self.y_sin = np.sin(self.x)
        self.y_cos = np.cos(self.x)
        self.y_tan = np.tan(self.x)

    def set_limits(self):
        self.y_tan[(self.y_tan < -10) | (self.y_tan > 10)] = np.nan

    def build_graph(self, show: bool = True, save_dir: str = None, save_name: str = "trig_functions"):
        plt.figure(figsize=(10, 6))
        plt.plot(self.x, self.y_sin, label='sin(x)', color='blue', linewidth=2)
        plt.plot(self.x, self.y_cos, label='cos(x)', color='green', linewidth=2, linestyle='--')
        plt.plot(self.x, self.y_tan, label='tan(x)', color='red', linewidth=1.5)

        plt.title('Тригонометрические функции', fontsize=14, fontweight='bold')
        plt.xlabel('x (радианы)', fontsize=12)
        plt.ylabel('y', fontsize=12)

        plt.ylim(-3, 3)
        plt.xlim(-2 * np.pi, 2 * np.pi)

        plt.xticks(
            [-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi],
            [r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$']
        )

        plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
        plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.legend(fontsize=11)

        if save_dir is not None:
            save_graph(name=save_name, save_dir=save_dir)

        if show:
            plt.show()

        plt.close()



