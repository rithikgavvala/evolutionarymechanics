import math
import os, inspect

#TODO implement cells sticking together in clusters as opposed to being individual units
#TODO adding a positional gradiet so cells at top grow faster than cells at bottom or vice versa
file = open("C:\Users\Quadr\Documents\Processing\Simulation\evolutionarymechanics\main\parameters.txt", "r")

#window_width = 1200
#window_height = 400
lines = file.readlines()
#lines = loadStrings("parameters.txt")
#print(lines)
window_width = int(lines[0])
window_height = int(lines[1])

#cell_radius = 0
cell_radius = int(lines[3]) #tweak for bigger or smaller bacteria
grid_width = cell_radius
grid_height = cell_radius
max_num_cells = int((window_height/cell_radius) * (window_width/cell_radius)) 
#growth_rate = .05
growth_rate = float(lines[4])
#amount_of_bacteria = max_num_cells - 500
#amount_of_bacteria = 500
#amount_of_bacteria = 700
amount_of_bacteria = int(lines[2])
num_cells = 0
gravity = PVector(0,38,0)
counter = 0
eta = .01
dt = .071
growing = 1
dividing = int(lines[6])
bottom_only = False
top_only = False
kill_thresh = 4
apop_thresh = .99
#killing = 1
killing = int(lines[5])
one_species = False
num_tracers = int(lines[7])
epsilon = 10
r_0 = cell_radius
class Cluster():
    def __init__(self, bacteria):
        self.bacteria_group = [bacteria]
        self.center = PVector(0,0,0)
        self.leftmost_bacteria = bacteria
        self.rightmost_bacteria = bacteria
        self.highest_bacteria = bacteria
        self.lowest_bacteria = bacteria
        self.width_radius = 0
        self.height_radius = 0
        self.neighborhood = []
        self.species_color = bacteria.species_color
        self.growth_rate = bacteria.growth_rate
        self.enemy_count = 0
        self.divided = False
        self.killed = False
    def update(self):
        left_bacteria = self.bacteria_group[0]
        right_bacteria = self.bacteria_group[0]
        top_bacteria = self.bacteria_group[0]
        bottom_bacteria = self.bacteria_group[0]
        for bacteria in self.bacteria_group[0:]:
            if bacteria.r.x < left_bacteria.r.x:
                left_bacteria = bacteria
            if bacteria.r.x > right_bacteria.r.x:
                right_bacteria = bacteria
            if bacteria.r.y < left_bacteria.r.y:
                top_bacteria = bacteria
            if bacteria.r.y > right_bacteria.r.y:
                bottom_bacteria = bacteria
                
        self.width_radius = (right_bacteria.x - left.bacteria.x +  2 * cell_radius) * .5
        self.height_radius = (bottom_bacteria.y - top_bacteria.y +  2 * cell_radius) * .5
        self.center = PVector(left_bacteria.r.x + width_radius, top_bacteria.r.y + height_radius, 0)
        self.leftmost_bacteria = left_bacteria
        self.rightmost_bacteria = right_bacteria
        self.highest_bacteria = top_bacteria
        self.lowest_bacteria = bottom_bacteria
    
    def show(self):
        for bacteria in self.bacteria_group:
            bacteria.show()
    def grow(self):
        for bacteria in self.bacteria_group:
            bacteria.grow()
    def divide(self):
        if self.width_radius >= self.height_radius + cell_radius:
            i = random(1)
            splitting_bacteria = self.highest_bacteria if i < .5 else self.lowest_bacteria
            if i < .5:
                #find a better way to balance this. The goal is to try and make the the dividing process as even as possible. Basically if the sides get too wide
                #new bacteria will grow on the top and bottoms and vice versa if the sides get too tall
                #want to spawn the new bacteria with a poistion relative to the bacteria that lie on the extrema. Ex if i want to add a bacteria to the top
                #we would want to subtract some value from the y value of the highest bacteria which would become the new y value for the new bacteria, effectivly making it the 
                #highest. what to do with the x value in this case isnt the clearest. needs some testing a figuring out.
                #bacteria_group.append(Bacteria(PVector.sub(splitting_bacteria.r, PVector(random(.5) + , 0, 0))))
                i+1
   
            
        
class Bacteria:
    def __init__(self, r, radius, species_color, divided, killed, growth_rate):
        self.r = r
        self.neighborhood = []
        self.next_position = PVector()
        self.radius = radius;
        self.species_color = species_color
        self.divided = divided 
        self.killed = killed
        self.clock = 0
        self.growth_rate = growth_rate
        self.r0 = PVector(r.x, r.y, r.z)
        self.rf = PVector(0,0,0)
        self.times = [] #list of floats
        self.trails = 0
        self.enemy_count = 0
        self.mother = None
        self.daughters = []
        
    def show(self):
        self.r.x = min(width, self.r.x)
        self.r.x = max(0, self.r.x)
        self.r.y = min(height, self.r.y)
        self.r.y = max(0, self.r.y)
        
        if self.species_color.x == 255:
            if self.trails == 0:
                fill(self.species_color.x/1.5, self.species_color.y, self.species_color.z+20, 50)
                stroke(60)
                pushMatrix()
                translate(self.r.x, self.r.y-10)
                ellipse(0,0,self.radius,self.radius)
                popMatrix()
        elif self.species_color.z == 255:
            if self.trails == 0:
                fill(self.species_color.x, self.species_color.y, self.species_color.z,60)
                stroke(60)
                pushMatrix()
                translate(self.r.x, self.r.y-10)
                ellipse(0,0,self.radius,self.radius)
                popMatrix()
        else:
            if self.trails == 0:
                fill(self.species_color.x, self.species_color.y, self.species_color.z)
                noStroke()
                pushMatrix()
                translate(self.r.x, self.r.y-10)
                ellipse(0,0,self.radius, self.radius)
                popMatrix()
            else:
                fill(self.species_color.x, self.species_color.y, self.species_color.z);
                noStroke();
                pushMatrix();
                translate(self.r.x, self.r.y-10);
                ellipse(0,0,self.radius/4,self.radius/4);
                popMatrix();  
    def grow(self):
        if self.species_color.y == 0:
            self.radius = self.radius + (2 * math.pi * dt * self.growth_rate)/self.radius
    def isDaughter(self, bacteria):
        return bacteria in self.daughters
    
    def isMother(self, bacteria):
        return self.mother == bacteria
    
            
class Biofilm:
    bacteria = []
    
    def __init__(self):
        bacteria = []
        clusters = []
    
    def addBacterium(self, bacterium):
        self.bacteria.append(bacterium)
    
    def removeBacterium(self, bacterium):
        self.bacteria.remove(bacterium)
    
    def update(self, to_divide, to_kill, cell_count):
        for i in range(len(to_divide)):
            cell_to_divide = to_divide[i]
            cell_to_divide.radius = cell_radius
            if (cell_count < max_num_cells):
                daughter = Bacteria(PVector.add(cell_to_divide.r, PVector.random2D().mult(cell_to_divide.radius)), cell_radius, cell_to_divide.species_color, False, False, cell_to_divide.growth_rate) #finish this constructor
                cell_to_divide.daughters.append(daughter)
                daughter.mother = cell_to_divide
                film.addBacterium(daughter)
                cell_count += 1
        for bug in to_kill:
            film.removeBacterium(bug)
            cell_count -= 1
    def update_clusters(self, to_divide, to_kill, cell_count):
        for i in range(len(to_divide)):
            cluster_to_divide = to_divde[i]
            
        
class Site:
    
    def __init__(self):
        self.contains = []

    
    def addBacterium(self, bacterium):
        self.contains.append(bacterium)
    
    def removeBacterium(self, bacterium):
        if bacterium in self.contains:
            self.contains.remove(bacterium)
    
    def clearBacterium(self):
        self.contains = []
    
    def updateNeighborhood(self):
        for bacteria in self.contains:
            temp = self.contains
            temp.remove(bacteria)
            bacteria.neighborhood = temp

class Grid:
    sites = [[]]
    
    def __init__(self, temp_grid_height, temp_grid_width):
        self.grid_h = temp_grid_height
        self.grid_w = temp_grid_width
        self.sites = [[None] * int(window_height / self.grid_h)] * int(window_width / self.grid_w)
        #sites = Site(int(window_width/grid_w),int(window_height/grid_h))
        
        for i in range(int(window_height/self.grid_h)):
            for j in range(int(window_width/self.grid_w)):
                self.sites[j][i] = Site()
        #print(len(self.sites))
        
    def reset(self, bacteria):
        for i in range(window_height / self.grid_h):
            for j in range(window_width / self.grid_w):
                self.sites[j][i].clearBacterium()
            
        for b in bacteria:
            i = pb(int(window_width / self.grid_w), int(b.r.x / self.grid_w))
            j = pb(int(window_height / self.grid_h), int(b.r.y / self.grid_h))
            self.sites[int(i)][int(j)].addBacterium(b)        
             
        #for i in range(window_height / self.grid_h):
            #for j in range(window_width / self.grid_w):
                #self.sites[j][i].updateNeighborhood()
        
        
film = Biofilm()
grid = Grid(grid_width, grid_height)

def setup():
    size(window_width, window_height)
    init(num_cells)
def draw():
    update()
    stroke(255)
    line(0,0, mouseX, mouseY)
    stroke(255)
    
def init(number_of_cells):
    for i in range(int(amount_of_bacteria)):
        x = width * random(1)
        film.bacteria.append(Bacteria(PVector(x, height - height * random(.2), 0), cell_radius, rand_color(int(x/int((window_width/2)))), False, False, growth_rate))
        number_of_cells += 1
    #consider makeing one cell of a diffrent coulour, green, and tracking that cell to see what happens to it and its species
    for i in range(num_tracers):
        film.bacteria.append(Bacteria(PVector(width*random(1), height - height * random(.25), 0), cell_radius, PVector(0,255,0), False, False, growth_rate))
    
        
def rand_color(x):
    return PVector(255, 0, 0) if random(1) > x else PVector(0, 0, 255)
  
def movement(bug, bacteria_list, cut_off, k):
    f = PVector(0,0,0)
    
    bug.enemy_count = 0
    for bacteria in bacteria_list:
        disp = PVector.sub(bacteria.r, bug.r)
        magnitude = disp.mag()
        if magnitude == 0:
            magnitude = .01
        f_attraction_mag = 12 * epsilon * ((r_0/magnitude) ** 12 * (1/magnitude) - (r_0/magnitude)**6 * (1/magnitude))
        f_attraction_mag =  f_attraction_mag / gravity.mag()
        #print(bug.isDaughter(bacteria))
        if bug.isDaughter(bacteria):
            angle = math.atan(disp.y/(disp.x+.0000001))
            f_attraction = PVector(f_attraction_mag * math.cos(angle), f_attraction_mag * math.sin(angle), 0)
            f.add(f_attraction)
            #bug.species_color = PVector(0, 255, 0)
            print(f_attraction)
        if abs(height - bug.r.y) < cell_radius:
            f.add(PVector(0,height - bug.r.y, 0))
        if disp.mag() < 1.1 * cell_radius:
            f.add(disp.normalize().mult(-1).mult(1))
        disp = PVector.sub(bacteria.r, bug.r)
        if disp.mag() < cell_radius :
            if disp.mag() != 0:
                f.add((disp.add(disp.mult((bug.radius+bacteria.radius)/disp.mag())).mult(-k)).mult(1))
        if disp.mag() < cut_off:
            if bacteria.species_color.x != bug.species_color.x and bacteria.species_color.y == 0:
                bug.enemy_count += 1
    f.add(gravity)
    return f

def update():
    #counter += 1
    #TODO work on grid.reset
    background(0)
    grid.reset(film.bacteria)
    #background(0)
    
    #print(len(film.bacteria))
    for bacteria in film.bacteria:
        bacteria.show()
        if num_cells < max_num_cells and growing == 1:
            bacteria.grow()
            
        neighbors = []
        i = int(floor(bacteria.r.x/grid_width))
        j = int(floor(bacteria.r.y/grid_height))
        #print(bacteria.r)
        for k in range(2):
            for l in range(2):
                t1 = pb(int(width/grid_width), i + k)
                t2 = pb(int(height/grid_height), j + l)
                neighbors = neighbors + grid.sites[t1][t2].contains
                #for b in grid.sites[t1][t2].contains:
                    #neighbors.append(b)
        #print(len(neighbors))
        #print(len(bacteria.daughters))
        temp = movement(bacteria,neighbors,1.2 * cell_radius, k)

        bacteria.r.add((temp).mult(eta*dt))
        
    to_divide = []
    ymin = height
    for bacteria2 in film.bacteria:
        if bacteria2.r.y < ymin:
            ymin = bacteria2.r.y
    pos = 0
    while pos != len(film.bacteria):
        current_bacteria = film.bacteria[pos]
        if current_bacteria.radius < 1.2 * cell_radius:
    
            if 1/random(100) > .9 and dividing == 1:
                if current_bacteria.species_color.y == 0:
                    if bottom_only:
                        h_div = height - ymin
                        x_div = height - current_bacteria.r.y
                        fact_div = 1 - float(math.pow(x_div/h_div, .25))
                        if random(1) < fact_div:
                            to_divide.append(current_bacteria)
                    if top_only:
                        for bacteria2 in film.bacteria:
                            if bacteria2.r.y < ymin:
                                ymin = bacteria2.r.y
                        if current_bacteria.r.y - ymin < 6 * cell_radius: #the number six seems a bit arbitray
                            to_divide.append(current_bacteria)
                    to_divide.append(current_bacteria)
        pos += 1
    to_kill = []
    pos = 0
    while pos != len(film.bacteria):
        current_bacteria = film.bacteria[pos]
        if current_bacteria.enemy_count * random(1) > kill_thresh:
            if current_bacteria.species_color.y == 0 and killing == 1:
                to_kill.append(curret_bacteria)
        if random(1) > apop_thresh and killing  ==  1 and one_species == False:
            to_kill.append(current_bacteria)
        pos += 1

    film.update(to_divide, to_kill, num_cells)
                
            
                                 
                        
    
        
def keyPressed():
    if(key == 'i'):
        init()
    if(key == 'a'):
        print("Active Zone: ON")
        delay(500)
        active_zone_rheology_running = True
        long_rheology_running = False
        rheology_running = False
        first_run = 1
    if(key == 'b'):
        initBlue()
    if(key == 't'):
        trails = 1-trails
        background(0)
    if(key == 'g'):
        growing = 1 - growing
    if(key == 'm'):
        rheology_running = true
        long_rheology_running = true
        first_run = 1
    if(key == 'k'):
        killing = 1-killing
    if(key == 'u'):
        init_gaussian()
  
 
def pb(size_, x):
    if type(x) == float:
        intpart = (floor(x) + size_)%size_
        floatpart = x - int(x)
        return floatpart + intpart
    elif type(x) == int:
        return int((x+size_) % size_)
    






    
