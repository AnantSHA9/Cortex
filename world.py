# createing a 20*20 grid which will be the world map for the robot;
import numpy as np
import random as r
class World:
    def __init__(self,size=20):
        self.size=size
        self.grid = np.zeros((size,size))
        self._set_border()
        self._set_walls()

    def _set_border(self):
        self.grid[0,:] = 1
        self.grid[-1,:] = 1
        self.grid[:,0] = 1
        self.grid[:,-1] = 1

    def render(self):
        for rows in self.grid:
            print(''.join(["#" if cell==1 else "." for cell in rows]))
 
    def _set_walls(self):
       coor = []
       for i in range(1,self.size-1):
           for j in range(1,self.size-1):
               coor.append((i,j))
        
       interior = self.size-2
       k = int((interior*interior)*0.2)

       r.shuffle(coor)

       for i in range(k):
            temp = coor[i]
            self.grid[temp[0],temp[1]]=1




world = World()
world.render()
