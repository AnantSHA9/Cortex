# createing a 20*20 grid which will be the world map for the robot;
import numpy as np
class World:
    def __init__(self,size=20):
        self.size=size
        self.grid = np.zeros((size,size))
        self._set_border()

    def _set_border(self):
        self.grid[0,:] = 1
        self.grid[-1,:] = 1
        self.grid[:,0] = 1
        self.grid[:,-1] = 1

    def render(self):
        for rows in self.grid:
            print(''.join(["#" if cell==1 else "." for cell in rows]))



world = World()
world.render()
