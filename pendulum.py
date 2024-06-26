import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g = 9.81  
length = 1.0  
theta0 = np.pi / 4.0  
omega0 = 0.0  
time_step = 0.05  
total_time = 10.0 
time_values = [0.0]
theta_values = [theta0]
omega_values = [omega0]
current_time = 0.0
current_theta = theta0
current_omega = omega0
