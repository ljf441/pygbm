.. notebook_test documentation master file, created by
   sphinx-quickstart on Sat Jul 25 11:56:56 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. .. figure:: logo.jpg
..    :alt: Course Logo
..    :align: left
..    :width: 200px

pygbm Package
===============================================================================

| *Author*: Laura Just Fung

.. _pygbm_package:

The **pygbm** package is a Python package designed to simulate geometric Brownian motion.

Features
--------

- **GBMSimulator**: core attributes and implements the analytic method
- **EulerMaruyama**: implements the Euler-Maruyama method
- **MilsteinSimulator**: implements the Milstein method

Installation
------------

Ensure you have Python 3.6 or higher. Install the package and its dependencies with:

.. code-block:: bash

    pip install -e .

Usage
-----

Here's a quick example of how to use the package:

.. code-block:: python

    from pygbm import GBMSimulator
    import matplotlib.pyplot as plt

    # Parameters for GBM
    y0 = 1.0
    mu = 0.05
    sigma = 0.2
    T = 1.0
    N = 100

    # Initialize simulator
    simulator = GBMSimulator(y0, mu, sigma)

    # Simulate path
    t_values, y_values = simulator.simulate_path(T, N)

    # Plot the simulated path
    plt.plot(t_values, y_values, label="GBM Path")
    plt.xlabel("Time")
    plt.ylabel("Y(t)")
    plt.title("Simulated Geometric Brownian Motion Path")
    plt.legend()
    plt.show()


Documentation
-------------

Visit our `documentation page <https://your-readthedocs-url-here>`_.

Contributing
------------

Contributions are welcome! Fork our repository and submit a pull request.

License
-------

This project is licensed under the MIT License - see the `LICENSE` file for details.


