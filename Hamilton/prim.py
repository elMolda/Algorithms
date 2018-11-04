from Point import Point
import math
import time
def dist(p1,p2):
  return math.sqrt(math.pow(p2.x-p1.x,2)+math.pow(p2.y-p1.y,2))

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
   
    def printPreOrder(self, parent):
        cost = 0 
        print ("Edge \tWeight")
        for i in range(1,self.V): 
            print (parent[i],"-",i,"\t",self.graph[i][ parent[i] ])
            cost += self.graph[i][ parent[i] ]
        #print("Cost: "+str(cost))
        return cost 
           
    def minKey(self, key, mstSet):  
        min = 100**100

        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 
  
    def primMST(self): 

        key = [100**100] * self.V 
        parent = [None] * self.V #MST 
        key[0] = 0 
        mstSet = [False] * self.V 
        parent[0] = -1 
  
        for cout in range(self.V): 

            u = self.minKey(key, mstSet) 
            mstSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
  
        cost = self.printPreOrder(parent) 
        return cost

#fout = open("prim_costs.txt","w+")
fi_time = open("prim_times.txt","w+")  
for i in range(1,101):
  name = "graph"+str(i)+".txt"
  f = open(name,"r") 
  f1 = f.readlines()
  pts = list() 
  for line in f1:
    cpy = line.split(',')
    p = Point(cpy[0],cpy[1])
    pts.append(p)

  f.close()
  g = Graph(8)
  g.graph = [
    [0,dist(pts[0],pts[1]),dist(pts[0],pts[2]),dist(pts[0],pts[3]),dist(pts[0],pts[4]),dist(pts[0],pts[5]),dist(pts[0],pts[6]),dist(pts[0],pts[7])],

    [dist(pts[1],pts[0]),0,dist(pts[1],pts[2]),dist(pts[1],pts[3]),dist(pts[1],pts[4]),dist(pts[1],pts[5]),dist(pts[1],pts[6]),dist(pts[1],pts[7])],

    [dist(pts[2],pts[0]),dist(pts[2],pts[1]),0,dist(pts[2],pts[3]),dist(pts[2],pts[4]),dist(pts[2],pts[5]),dist(pts[2],pts[6]),dist(pts[2],pts[7])],

    [dist(pts[3],pts[0]),dist(pts[3],pts[1]),dist(pts[3],pts[2]),0,dist(pts[3],pts[4]),dist(pts[3],pts[5]),dist(pts[3],pts[6]),dist(pts[3],pts[7])],

    [dist(pts[4],pts[0]),dist(pts[4],pts[1]),dist(pts[4],pts[2]),dist(pts[4],pts[3]),0,dist(pts[4],pts[5]),dist(pts[4],pts[6]),dist(pts[4],pts[7])],

    [dist(pts[5],pts[0]),dist(pts[5],pts[1]),dist(pts[5],pts[2]),dist(pts[5],pts[3]),dist(pts[5],pts[4]),0,dist(pts[5],pts[6]),dist(pts[5],pts[7])],

    [dist(pts[6],pts[0]),dist(pts[6],pts[1]),dist(pts[6],pts[2]),dist(pts[6],pts[3]),dist(pts[6],pts[4]),dist(pts[6],pts[5]),0,dist(pts[6],pts[7])],

    [dist(pts[7],pts[0]),dist(pts[7],pts[1]),dist(pts[7],pts[2]),dist(pts[7],pts[3]),dist(pts[7],pts[4]),dist(pts[7],pts[5]),dist(pts[7],pts[6]),0]
  ]
  start = time.time()
  cost = g.primMST()
  end = time.time()
  fi_time.write(str((end-start)*1000)+"\n")
  #fout.write(str(cost)+"\n")
  print("Cost: "+str(cost))
#fout.close()
fi_time.close()


