# World goal: to implement a 20*20 2d grid which is our world view
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
        if self.free_cells:
            x,y = self.free_cells.pop()
            self.obj_dict[obj_name]={"type":obj_type,"pos":(x,y)}

    def render(self,robot):
        for i in range(self.size):
            row_build=""
            for j in range(self.size):
                flag = 0
                if self.grid[i][j]==1:
                    row_build+="#"
                elif self.grid[i][j]==0:
                    if (i,j) == (robot.i,robot.j):
                        row_build+="R"
                        flag = 1
                        continue
                    if not flag:
                        for obj_name,obj_data in self.obj_dict.items():
                             if (i,j) == obj_data["pos"]:
                                 row_build+=obj_data["type"][0].upper()
                                 flag = 1 
                                 break
                    if not flag:
                      row_build+="."
            print(row_build)
         
# Robot goals: 
        ## existing in the world, which gets shown using render of world
        ## moving in the world 
        ## observing in the world
        ## creating own local world view
        ## creating mapping between the two worlds 
        ## remembering objects which were encountered and where 
class Robot:
    def __init__(self,world):
        self.world = world
        self.i,self.j = self.world.free_cells.pop()
        self.robo_occupied = []
        self.obs_dict = {}

    def movement(self,dirxn):
        if self.world.grid[self.i-1][self.j]!=1 and dirxn=="up":
            self.i-=1
            self.robo_occupied.append((self.i,self.j))

        if self.world.grid[self.i+1][self.j]!=1 and dirxn=="down":
            self.i+=1
            self.robo_occupied.append((self.i,self.j))


        if self.world.grid[self.i][self.j-1]!=1 and dirxn=="left":
            self.j-=1
            self.robo_occupied.append((self.i,self.j))


        if self.world.grid[self.i][self.j+1]!=1 and dirxn=="right":
            self.j+=1 
            self.robo_occupied.append((self.i,self.j))


    def observation(self):
        posi = []
        for i in range(self.i-2,self.i+3):
            for j in range(self.j-2,self.j+3):
                 if 0<=i<self.world.size and 0 <= j < self.world.size:
                      posi.append((i,j))

        pos_dict = {}
        for obj_name,obj_data in self.world.obj_dict.items():
            pos_dict[obj_data["pos"]] = {"obj_name":obj_name,"obj_type":obj_data["type"]}
            
         
        for i in posi:
           if i in pos_dict:
              self.obs_dict[i]={pos_dict[i]}



world = World()
robot = Robot(world)
world.put_objects("chair","chair_1")
world.put_objects("table","table_1")
world.put_objects("stairs","stairs_1")
robot.movement("up")
robot.movement("right")
robot.movement("down")
robot.observation()
print("robot:", robot.i, robot.j)
print("objects:", world.obj_dict)
print(robot.obs_dict)
world.render(robot)


