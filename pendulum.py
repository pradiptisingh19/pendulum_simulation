import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def calculate_angular_acceleration(theta, omega):
    return -g / length * np.sin(theta)

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

while current_time < total_time:
    alpha = calculate_angular_acceleration(current_theta, current_omega)
    current_omega += alpha * time_step
    current_theta += current_omega * time_step
    current_time += time_step
    time_values.append(current_time)
    theta_values.append(current_theta)
    omega_values.append(current_omega)
