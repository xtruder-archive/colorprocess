from scipy import misc
from scipy import interpolate
import math
import sys
def process():
    im=misc.imread("graf2.jpg")
    impoints=[]
    colors=[]
    #Red 1
    #colors.append([115,64,69])
    #colors.append([120,78,89])
    #colors.append([93,42,52])
    #Blue green 1
    #colors.append([85,87,115])
    #colors.append([69,107,100])
    #colors.append([56,96,89])
    #colors.append([70,71,113])
    #colors.append([86,109,107])
    #colors.append([29,89,75])
    #Red 2
    #colors.append([105,70,69])
    #colors.append([95,76,87])
    #colors.append([112,90,98])
    colors.append([73,83,104])
    colors.append([77,89,114])
    colors.append([87,75,95])
    colors.append([63,65,98])
    for i,x in enumerate(im):
        print i
        min_r= 1000
        min_g= 1000
        min_b= 1000
        impoints.append([])
        for k,y in enumerate(x):
            impoints[i].append([0,0,0])
            r_sum=0
            g_sum=0
            b_sum=0
            if i<4 or k<4 or i>len(im)-4 or k>len(x)-4:
                continue
            for l in range(-2,3):
                for m in range(-2,3):
                    r_sum+= im[i+l][k+m][0]
                    g_sum+= im[i+l][k+m][1]
                    b_sum+= im[i+l][k+m][2]

            for color in colors:
                if abs(r_sum/25-color[0])<min_r and abs(g_sum/25-color[1])<min_g and abs(b_sum/25-color[2])<min_b:
                    min_r= abs(r_sum/25-color[0])
                    min_g= abs(g_sum/25-color[1])
                    min_b= abs(b_sum/25-color[2])

                if abs(r_sum/25-color[0])<10 and abs(g_sum/25-color[1])<10 and abs(b_sum/25-color[2])<10:
                    impoints[i][k]=y
                    print k,i, y

        print "Min:", min_r, min_g, min_b

    misc.imsave("procssed.png", impoints)
    return impoints

def extract_points(img):
    im=misc.imread(img)
    xpoints=[]
    ypoints=[]
    points= {}
    width=3326
    height=2336
    xoffset=2900
    yoffset=2200
    yoffset2=330
    for k,y in enumerate(im): #Y in graph
        print k
        for j,x in enumerate(y): #X in graph
            if x[0]>2 and x[1]>2 and x[2]>2:
                px= float(j)/float(xoffset)*2*math.pi-math.pi
                py= (height-k)-(height-yoffset)
                py= (py/float(yoffset-yoffset2))*40.0-40
                py= 10**(py/10)
                #if py<-30:
                #    continue
                if(px>math.pi or px<-math.pi):
                    continue

                if(points.has_key(px)):
                    if py>points[px]:
                        ypoints[ypoints.index(points[px])]= py
                        points[px]=py
                else:
                    points[px]=py
                    xpoints.append(px)
                    ypoints.append(py)

    return (xpoints, ypoints, points)

def integrate(points):
    keys= sorted(points.keys())
    keys= filter(lambda x: x>-0.02, keys)
    suma=0
    for x in range(len(keys)-1):
        if abs(points[keys[x+1]]-points[keys[x]])>20:
            print "Big span"
            continue
        Fp= (points[keys[x+1]]+points[keys[x]])/2
        sumk= (Fp**2)*math.sin(keys[x])*(keys[x+1]-keys[x])
        print sumk
        suma+=sumk

    return 2/suma
