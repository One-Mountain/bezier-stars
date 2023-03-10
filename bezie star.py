import matplotlib.pyplot as plt
import numpy as np
import array as arr

# create a n sided star based on user input using bezier curves. 

# -------------------------modifiable inputs: 
# central point. 
x0 = 300
y0 = 300

# lenght/radius for the star
r = 300
# step size for the lerp function. 
delta = 0.05



# ------------ initializing values and functions
p0 = np.array([x0,y0])
#define the lerp function: c = a+ (b-a)*t
def lerpy(a,b,t):
  #linear interpolation starting point a, end point b, step size t
  tt= np.arange(0,1+t, t)
  x = a+(b-a)*tt
  return x

#create the quadratic bezier curve using lerp(lerp())
def quadLerp(a,b,c,t):
    
    x1 = lerpy(a[0], b[0], t)
    x2 = lerpy(b[0], c[0], t)

    y1 = lerpy(a[1], b[1], t)
    y2 = lerpy(b[1], c[1], t)

    x = lerpy(x1, x2, t)
    y = lerpy(y1, y2, t)

    #optional to show all lines
    plt.plot([x1, x2],[y1, y2])

    p = np.array([x, y])
    return p

#asking user for number of sides for a star (n>=3 starts creating a star )
n = input("Please enter a positive integer for the number of sides: ")

#-------------------- star creation
n=int(n)
if(n==1):
    #special case, 1 sided star. Would be just a line
    x1 = x0+r
    y1 = y0
    p1 = np.array([x1,y1])
    xL = lerpy(p0[0],p1[0],delta)
    yL = lerpy(p0[1],p1[1],delta)
    pL = np.array([xL, yL])
    plt.scatter(pL[0], pL[1])
    plt.plot(pL[0], pL[1])
    plt. xlim(0, 600)
    plt. ylim(0, 600)
    plt.show()
elif(n==2):
    #second special case. 2 point star would be define as the quad bezier of perpendicular lines
    x1 = x0+r
    y1 = y0
    p1 = np.array([x1,y1])
    x2 = x0
    y2 = y0+r
    p2 = np.array([x2,y2])
    
    pL = quadLerp(p1,p0,p2,delta)

    plt.plot([p0[0],p2[0]],[p0[1],p2[1]])
    plt.plot([p0[0],p1[0]],[p0[1],p1[1]])
    plt.plot(pL[0], pL[1])
    plt. xlim(0, 600)
    plt. ylim(0, 600)
    plt.show()
    
else:
    #n>=3 start of actual star creation
    #equally space the points in the star using the roots of unity 
    k = np.arange(n)
    x = r*np.cos(2*k*np.pi/n)+x0
    y = r*np.sin(2*k*np.pi/n)+y0
   
    for i in range(n):
        #plot a line from each point in the star back to the start
        plt.plot([p0[0],x[i]], [p0[1],y[i]])
        
        #create the quad bezier curve from one point in the star, center as control point, to the next point in the star
        p1 = np.array([x[i],y[i]])
        if(i==n-1):
            #last point uses the first point to get back to start
            p2 = np.array([x[0],y[0]])
        else:
            p2 = np.array([x[i+1],y[i+1]])
        
        pL = quadLerp(p1,p0,p2, delta)
        plt.plot(pL[0], pL[1])
        

    plt. xlim(0, 600)
    plt. ylim(0, 600)
    plt.show()
    
