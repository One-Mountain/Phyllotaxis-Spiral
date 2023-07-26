import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button 
import numpy as np


n = 500 #number of samples 

k = np.linspace(0, n, num = n+1) # line spacing
def phyllotaxis(c, angle): # finding x and y coordinates of the phyllotaxis
    #phi = n* angle
    #r = c * sqrt(n)
    phi = k * angle 
    r = c * np.sqrt(k) 
    x =  r * np.cos(phi * np.pi / 180)  #change from radians to degrees
    y =  r * np.sin(phi * np.pi / 180)  
    return x, y

init_c = 2 # initial number for the radius of the phyllotaxis 
init_angle = 137.5 #initial angle for the phyllotaxis

fig, ax = plt.subplots()
x = phyllotaxis(init_c, init_angle)[0]
y = phyllotaxis(init_c, init_angle)[1]
line, = ax.plot(x, y,'.', markersize = 5, lw=2) #create the initial plot and conditions
ax.set_xlabel('x')
ax.set_ylabel('y')

fig.subplots_adjust(left = 0.25, bottom = 0.25) #adjust space for a couple of sliders

#add a slider to change the c value
axc = fig.add_axes([0.25, 0.1, 0.65, 0.03])
#create a slider
c_slider = Slider( 
    ax = axc, 
    label = 'c', 
    valmin = 1, 
    valmax = 30, 
    valinit = init_c,
)
# add a slider to change the angle value
axangle = fig.add_axes([0.1, 0.25, 0.03, 0.65]) 

angle_slider = Slider( 
    ax = axangle, 
    label = 'angle', 
    valmin = 0,
    valmax = 360,
    valinit = init_angle,
    orientation = 'vertical'
) 
#create a function to update the plot
def update(val):
    x = phyllotaxis(c_slider.val, angle_slider.val)[0]
    y = phyllotaxis(c_slider.val, angle_slider.val)[1]
    line.set_xdata(x)
    line.set_ydata(y)
    fig.canvas.draw_idle()

#register the update function with the sliders 
c_slider.on_changed(update)
angle_slider.on_changed(update)

#create a reset button to reset the plot to initial conditions
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04]) 
button = Button(resetax, 'Reset', hovercolor = '0.975') 

def reset(event): #define what happens with reset button
    c_slider.reset()
    angle_slider.reset()

button.on_clicked(reset) 

plt.show()