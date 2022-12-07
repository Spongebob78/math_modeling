import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
 
def circle_move(R):
    #alpha =(np.pi/180) * time
    time = np.arange(-100, 100, 0.1)

    x = R * (np.sin(time)**3) 
    y = R * (np.cos(time)**3)
    
    plt.axis('equal')
    plt.plot(x, y)
    plt.savefig('lab_7_osn_11.png')

circle_move(8)