#second order odinary diff eq - pendulum - vector flow setup - determining stable initial conditions

import numpy as np

#Below are physical constraints and inital conditions
g = 9.8
L = 2 
u = 0.1

theta_0 = np.pi /2 #90 degrees
theta_velocity_0 = 0 #initial angular velocity DNE

#ODE eqn
def fn_theta_acceleration(theta, theta_velocity):
    return -u * theta_velocity - (g/L) * np.sin(theta)
    
#soln detrmining loop
# utilizing the many steps of delta_t
# each loop increases theta by theta_velocity * delta_t then increase theta_velocity by theta_acceleration * delta_t 
# such that theta_acceleration can be computed based on the diff eq
def theta(t):
    #begin changing values
    theta = theta_0
    theta_velocity = theta_velocity_0
    delta_t = 0.01 #arbitrary but particular time step
    for time in np.arange(0, t, delta_t):
        theta_acceleration = fn_theta_acceleration(
        theta, theta_velocity
        )
        theta += theta_velocity * delta_t
        theta_velocity += theta_acceleration * delta_t
     return theta
    
    
