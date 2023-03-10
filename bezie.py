import matplotlib.pyplot as plt
import time
import numpy as np
import array as arr

#initial points
x1 = 0
y1 = 300

x2 = 100
y2 = 100

x3 = 400
y3 = 400

x4 = 600
y4 = 300

#ordered pair of points
p1 = np.array([x1,y1])
p2 = np.array([x2,y2])
p3 = np.array([x3,y3])
p4 = np.array([x4,y4])

# mouse movement of one control point. 

def on_move(event):
    if event.inaxes:
        plt.clf()
        plt. xlim(0, 600)
        plt. ylim(0, 600)
        (x2, y2) = (event.xdata, event.ydata)
        p2 = np.array([x2,y2])

        plt.scatter([x1,x2,x3,x4],[y1,y2,y3,y4])
        time.sleep(0.05)
        plt.plot([x1, x2],[y1, y2])
        plt.plot([x3, x4],[y3, y4])

        pL = cubicLerp(p1,p2,p3,p4,delta)
       

        plt.scatter(pL[0], pL[1])
        plt.plot(pL[0], pL[1])
        plt.show()
        
binding_id = plt.connect('motion_notify_event', on_move)


#quadratic Bezie

#define the lerp function 
delta = 0.05
def lerpy(a,b,t):
  tt= np.arange(0,1+t, t)
  x = a+(b-a)*tt
  return x


#xx1 = lerpy(x1, x2, delta)
#yy1 = lerpy(y1, y2, delta)

#xx2 = lerpy(x2, x3, delta)
#yy2 = lerpy(y2, y3, delta)

#xx = lerpy(xx1, xx2, delta)
#yy = lerpy(yy1, yy2, delta)

def quadLerp(a,b,c,t):
    #xx1 = lerpy(x1, x2, delta)
    #yy1 = lerpy(y1, y2, delta)

    #xx2 = lerpy(x2, x3, delta)
    #yy2 = lerpy(y2, y3, delta)

    #xx = lerpy(xx1, xx2, delta)
    #yy = lerpy(yy1, yy2, delta)
    
    x1 = lerpy(a[0], b[0], t)
    x2 = lerpy(b[0], c[0], t)

    y1 = lerpy(a[1], b[1], t)
    y2 = lerpy(b[1], c[1], t)

    x = lerpy(x1, x2, t)
    y = lerpy(y1, y2, t)

    plt.plot([x1, x2],[y1, y2])

    p = np.array([x, y])
    return p


def cubicLerp(a,b,c,d,t):
    #v1x= quadLerp(x1,x2,x3,delta)
    #v1y= quadLerp(y1,y2,y3,delta)

    #v2x= quadLerp(x2,x3,x4,delta)
    #v2y= quadLerp(y2,y3,y4,delta)

    #xL= lerpy(v1x,v2x,delta)
    #yL= lerpy(v1y,v2y,delta)
    x1 = quadLerp(a,b,c,t)
    x2 = quadLerp(b,c,d,t)
    x = lerpy(x1[0],x2[0],t)
    y = lerpy(x1[1],x2[1],t)

    plt.plot([x1[0],x2[0]],[x1[1],x2[1]])
    p = np.array([x,y])
    return p

pL = cubicLerp(p1,p2,p3,p4,delta)




plt.scatter([x1,x2,x3,x4],[y1,y2,y3,y4]) # all points
plt. xlim(0, 600)
plt. ylim(0, 600)
#plt.plot([x1, x2],[y1, y2])  #lines endpoint to control
#plt.plot([x3, x4],[y3, y4])  #lines endpoint to control
plt.plot(pL[0], pL[1])
plt.show()

