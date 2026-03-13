# createing a 20*20 grid which will be the world map for the robot;
import numpy as np
import random as r
class World:
    def __init__(self,size=20):
        self.size=size
        self.grid = np.zeros((size,size))
        self.coor = []
        self.k = 0 
        self.object_dict = {}
        self._set_border()
        self._set_walls()
        self.free_cells = self.coor[self.k:]

# creating a set border function which runs the moment an object is created and initilize the borders with '1';
    def _set_border(self):
        self.grid[0,:] = 1
        self.grid[-1,:] = 1
        self.grid[:,0] = 1
        self.grid[:,-1] = 1

# created a render function which shows how the grid map looks 
    def render(self): 
     for i in range(self.size):
         row_string = ""
         for j in range(self.size):
              flag = 0
              if self.grid[i][j] == 1:
                   row_string+="#"
              elif self.grid[i][j] == 0:
                 for obj_name,obj_data in self.object_dict.items():
                        if obj_data["position"]==(i,j):
                            flag = 1
                            row_string+=obj_data["type"][0].upper()
                            break
                 if not flag:
                        row_string+="."

         print(row_string)
                                
# creating a set walls function it's a private function which places walls inside the grid;
# from position (1,1)->(18,18) and each time walls are placed at random positions because of r.suffle();
    def _set_walls(self):
       for i in range(1,self.size-1):
           for j in range(1,self.size-1):
               self.coor.append((i,j))
        
       interior = self.size-2
       self.k = int((interior*interior)*0.2)

       r.shuffle(self.coor)

       for i in range(self.k):
            x,y= self.coor[i]
            self.grid[x,y]=1

# creating a place objects functions which creates a dictionary to maintain which location has what object place;
# and we can see that by render function using the first initials of the object's name;
    def place_objects(self,obj_type,obj_name):
        if len(self.free_cells)>=1:
          indxs = self.free_cells.pop(0)
        else:
          print("No free position")

        self.object_dict[obj_name]={"type":obj_type,"position":indxs}





world = World()
world.place_objects("chair","chair_1")
world.place_objects("person","person_1")
print(world.object_dict)
world.render()
