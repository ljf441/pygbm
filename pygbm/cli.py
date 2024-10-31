import numpy as np
import argparse
import matplotlib.pyplot as plt
from pygbm import GBMSimulator

def main():
    parser = argparse.ArgumentParser(description="Simulate a geometric Brownian motion path.")
   
    parser.add_argument('--y0', type=float, required=True, help='Initial value (y0)')
    parser.add_argument('--mu', type=float, required=True, help="Drift (mu)")
    parser.add_argument('--sigma', type=float, required=True, help="Diffusion coefficient (sigma)")
    parser.add_argument('--T', type=float, required=True, help="Time taken (T)")
    parser.add_argument('--N', type=int, required=True, help="Number of time steps (N)")
    parser.add_argument('--output', type=str, default='gbm_plot.png', help="Output filename for the plot")

    args = parser.parse_args()

    simulator = GBMSimulator(args.y0, args.mu, args.sigma)

    t_values, y_values = simulator.simulate_path(args.T, args.N)

    plt.plot(t_values, y_values, label="GBM path")
    plt.xlabel("Time")
    plt.ylabel("Y(t)")
    plt.title("Simulated geometric Brownian motion path")
    plt.legend()
    plt.grid()

    plt.savefig(args.output)
    plt.close()

    print(f'Plot saved to {args.output}')

if __name__=='__main__':
    main()