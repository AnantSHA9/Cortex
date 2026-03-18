# goal: to implement a 20*20 2d grid which is our world view
      ## -> the grid will have walls on it's boundary 
      ## -> and inside 20% of indices will be walls which comes randomly not hard coded
      ## -> after that objects needs to appear inside grid 
      ## -> but the object can't be stored in the grid so we will need a container to store them with it's object tyep and it's location
      ## -> then we will need a render function that's going to print the grid with walls free indices and objects as well
      ## -> render function is for our use because it will provide information on how things are working printing the grind won't provide any information

import numpy as np
import random as r

class World:
    def __init__(self):
        self.size = 20
        self.grid = np.zeros((self.size,self.size),dtype=int)
        self.coords = []
        self.k = 0
        self._put_walls()
        self.free_cells = self.coords[self.k:]
        self.obj_dict = {}
        
        

    def _put_walls(self):
        self.grid[0,:]=1
        self.grid[-1,:]=1 

        self.grid[:,0]=1
        self.grid[:,-1]=1
        
        self.coords = [(i,j) for i in range(1,self.size-1) for j in range(1,self.size-1)]
        self.k = int(((self.size-2)*(self.size-2))*0.2)
        r.shuffle(self.coords)

        for i in range(self.k):
            x,y = self.coords[i]
            self.grid[x][y] = 1 

    def put_objects(self,obj_type,obj_name):
            x,y = self.free_cells.pop()
            self.obj_dict[obj_name]={"type":obj_type,"pos":(x,y)}

    def render(self):
        for i in range(self.size):
            row_build=""
            for j in range(self.size):
                flag = 0
                if self.grid[i][j]==1:
                    row_build+="#"
                elif self.grid[i][j]==0:
                    for obj_name,obj_data in self.obj_dict.items():
                         if (i,j) == obj_data["pos"]:
                             row_build+=obj_data["type"][0].upper()
                             flag = 1 
                             break
                    if not flag:
                      row_build+="."
            print(row_build)
          

world = World()
world.put_objects("chair","chair_1")
world.put_objects("table","table_1")
world.put_objects("stairs","stairs_1")
world.render()


