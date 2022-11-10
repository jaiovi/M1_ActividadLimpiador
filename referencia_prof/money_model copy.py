import mesa
import numpy as np


class MoneyAgent(mesa.Agent):
    # An agent with fixed initial wealth.

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.counter = 0
        
    def step(self):
        self.move()
        self.clean()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        self.counter = self.counter + 1

    def clean(self):
        if self.model.isDirty(self.pos)
            self.model.setDirty(self.pos)
        '''
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1
        '''
    

class MoneyModel(mesa.Model):

    """A model with some number of agents."""

    def __init__(self, N, width, height, percent):
        self.num_agents = N
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)


        self.init_time = None
        self.final_time = None

        self.celdas_suc = (width*height) * percent
        self.celdas_lim 
        self.dirty_matriz = np.random.randint(2, size=(5,5)) #0 y 1 inicializr mtri

        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (1, 1)) #place agent en todos
    
    def step(self):
        # Advance the model by one step.
        self.schedule.step()

    def isDirty(self, new_position):
        x,y = new_position
        #return self.dirty_matriz[x][y]
        pass #retornar verdadero o falso

    def setDirty(self, new_position):
        #limpia extra
        self.celdas_suc -= 1
        self.celdas_lim += 1
        if self.celdas_suc==0:
            #si quedaron todas limpias
            self.final_time=5
        pass

    def totalMoviemientos(self):
        pass
    
    def porcentajeCeldasLimpias(self):
        return self.celdas_lim / (self.celdas_lim + self.celdas_suc)
        pass
    