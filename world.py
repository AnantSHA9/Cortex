# complete reimplementation of the step 1-4;
# goal :- 
        ## to implement a world class which will create a entire 2d world map
        ## to implent a 2d 20*20 grid 
        ## all boundary will be considered as walls represented by 1 and free cell by 0
        ## now to see grid we can either do print(world.grid) but that won't give us a good look 
        ## so we need to implement a render function that will act a monitior which shows grid after every change
        ## now as we have an inter map of the grid with wall on the boundary we need walls on 20% of the free walls inside boundary 
        ## so we need to implement a place walls function for that
        ## now we have walls and everything in place we need objects inside the world map
        ## so objects can't be directly placed in side the grid because it won't work for 100 or 1000 objects 
        ## so we will make a dictionary which will hold and object_name->type , coordinates, and we also need to mark those coordinates as filled as well

import numpy as np
import random as r

class World: 
    def __init__(self,size=20):
        self.size = size
        self.grid = np.zeros((size,size),dtype=int)
        self.k = 0
        self.coor=[]
        self.free_cells=[]
        self.obj_dict={}

        self._set_walls()
        self._place_walls()

        self.free_cells = self.coor[self.k:]


    def _set_walls(self):
        self.grid[0,:]=1
        self.grid[-1,:]=1
        self.grid[:,0]=1
        self.grid[:,-1]=1

    def render(self):
        for i in range(self.size):
            row_build = ""
            for j in range(self.size):
                flag = 0
                if self.grid[i][j]==1:
                    row_build+="#"
                elif self.grid[i][j]==0:
                    for obj_name,obj_data in self.obj_dict.items():
                        if obj_data["location"]==(i,j):
                            flag=1
                            row_build+=obj_data["type"][0].upper()
                            break
                    if not flag:
                        row_build+="."
            print(row_build)

    def _place_walls(self):
        for i in range(1,self.size-1):
            for j in range(1,self.size-1):
                self.coor.append((i,j))

        int_size = (self.size-2)**2
        self.k  = int((int_size*0.2))

        r.shuffle(self.coor)
        
        for i in range(self.k):
            x,y = self.coor[i]
            self.grid[x][y]=1


    def place_objects(self,obj_name,obj_type): 
        if len(self.free_cells)>0:
          indx = self.free_cells.pop()
        self.obj_dict[obj_name]={"type":obj_type,"location":indx}




                 
world=World()
world.place_objects("chair_1","chair")
world.place_objects("chair_2","chair")
world.place_objects("person_1","person")
world.place_objects("table_1","table")
world.render()
