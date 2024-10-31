import numpy as np
class GBMSimulator:
  def __init__(self, y0, mu, sigma):
    self.y0 = y0
    self.mu = mu
    self.sigma = sigma
  def simulate_path(self, T, N):
    dt = T / N
    t_values = np.linspace(0, T, N + 1)
    y_values = np.zeros(N + 1)
    y_values[0] = self.y0
    for i in range(1, N + 1):
      z = np.random.normal(0, np.sqrt(dt))
      y_values[i] = y_values[0] * np.exp((self.mu - self.sigma**2 / 2) * dt + self.sigma * z)
    return t_values, y_values
  
class EulerMaruyama(GBMSimulator):
  def simulate_empath(self, T, N):
    dt = T/N
    t_values = np.linspace(0, T, N+1)
    y_values = np.zeros(N + 1)
    y_values[0] = self.y0
    for i in range(1, N+1):
      z = np.random.normal(0, 1)
      y_values[i] = y_values[i - 1] * (1 + self.mu * dt + self.sigma * np.sqrt(dt) * z)
        
    return t_values, y_values

class MilsteinSimulator(GBMSimulator):
  def simulate_milpath(self, T, N):
    dt = T/N
    t_values = np.linspace(0, T, N+1)
    y_values = np.zeros(N + 1)
    y_values[0] = self.y0
    for i in range(1, N+1):
      z = np.random.normal(0, 1)
      y_values[i] = (y_values[i - 1] + self.mu * y_values[i - 1] * dt + self.sigma * y_values[i - 1] * np.sqrt(dt) * z + ((self.sigma**2)/2) * y_values[i - 1] * (z**2 - 1) * dt)

    return t_values, y_values