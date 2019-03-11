class Bacteria:
    r = ""
    neighborhood = [] # list of Bacterium
    next_position = PVector() # list of ints representing the position
    radius = ""
    species_color = ""
    divided = ""
    killed = ""
    clock = ""
    growth_rate = ""
    enemy_count = ""
    r0 = ""
    rf = ""
    times = []
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
            if trails == 0:
                fill(self.species_color.x, self.species_color.y, self.species_color.z)
                noStroke()
                pushMatrix()
                translate(self.r.x, self.r.y-10)
                ellipse(0,0,self.radius, self.radies)
                popMatrix()
            else:
                fill(self.species_color.x, self.species_color.y, self.species_color.z);
                noStroke();
                pushMatrix();
                translate(self.r.x, self.r.y-10);
                ellipse(0,0,self.radius/4,self.radius/4);
                popMatrix();  
    def grow():
        if self.species_color.y == 0:
            self.radius = self.radius + (2 * pi * dt * self.growth_rate)/self.radius
            
class Biofilm:
    bacteria = []
    
    def __init__(self):
        bacteria = []
    
    def addBacterium(bacterium):
        bacteria.append(bacterium)
    
    def removeBacterium(bacterium):
        bacteria.remove(bacterium)
    
    def update(to_divide, to_kill):
        for i in len(to_divide):
            to_divide[i].radius = cell_radius
            if (num_cells < max_num_cells):
                daughter = Bacterium #finish this constructor
                bugs.addBacterium(daughter)
                num_cells = num_cells + 1
        for i in len(to_kill):
            bugs.removeBacterium(b)
            num_cells = num_cells - 1
        
class Site:
    
    def __init__(self):
        self.contains = []

    
    def addBacterium(self, bacterium):
        contains.append(bacterium)
    
    def removeBacterium(self, bacterium):
        contains.remove(bacterium)
    
    def clearBacterium():
        contains = []

class Grid:
    sites = [[]]
    
    def __init__(self, temp_grid_height, temp_grid_width):
        self.sites = []
        self.grid_h = temp_grid_height
        self.grid_w = temp_grid_width
        #sites = Site(int(window_width/grid_w),int(window_height/grid_h))
        
        for i in range(int(window_height/self.grid_h)):
            self.sites.append([])
            for j in range(int(window_width/self.grid_w)):
                self.sites[i].append(Site())
        #print(self.sites[0])
        
        def reset(self, bacteria):
            for i in range(window_height / self.grid_h):
                for j in range(window_width / self.grid_w):
                    self.sites[i][j].clearBacterium()

            for b in bacteria:
                i = pb(int(window_width / self.grid_w), int(b.r.x / self.grid_w))
                j = pb(int(window_height / self.grid_h), int(b.r.y / self.grid_h))
                self.sites[i][j].addBacterium(b)            
        
        

window_width = 1200
window_height = 400
cell_radius = 20 #tweak for bigger or smaller bacteria
grid_width = cell_radius
grid_height = cell_radius
max_num_cells = int((window_height/cell_radius) * (window_width/cell_radius)) 
film = Biofilm()
growth_rate = .05
#amount_of_bacteria = max_num_cells - 500
amount_of_bacteria = 500
gravity = PVector(0,38,0)
counter = 0
grid = Grid(grid_width, grid_height)
eta = .01
dt = .071

def setup():
    size(window_width, window_height)
    init()
    print(max_num_cells)
def draw():
    line(0,0, mouseX, mouseY)
    update()
    stroke(255)
    
def init():
    for i in range(int(amount_of_bacteria)):
        x = width * random(1)
        film.bacteria.append(Bacteria(PVector(x, height - height * random(.2), 0), cell_radius, rand_color(x/int((window_width/2))), False, False, growth_rate))
        
def rand_color(x):
    return PVector(255, 0, 0) if random(1) > x else PVector(0, 0, 255)
  
def movement(bug, bacteria_list, cut_off, k):
    f = PVector(0,0,0)
    bug.enemy_count = 0
    for bacteria in bacteria_list:
        disp = PVector.sub(bacteria.r, bug.r)
        if abs(height - bug.r.y) < cell_radius:
            f.add(PVector(0,height - bug.r.y, 0))
        if disp.mag() < 1.1 * cell_radius:
            f.add(disp.normalize().mult(-1).mult(1))
        disp = PVector.sub(bacteria.r, bug.r)
        if disp.mag() < cell_radius :
            if disp.mag() != 0:
                f.add((disp.add(disp.mult((bug.radius+bacteria.radius)/disp.mag())).mult(-k)).mult(1))
        if dis.mag() < cut_off:
            if bacteria.species_color.x != bug.species_color.x and bacteria.species_color.y == 0:
                bug.enemy_count += 1
    f.add(gravity)
    return f

def update():
    #counter += 1
    for bacteria in film.bacteria:
        bacteria.show()
        neighbors = []
        i = int(floor(bacteria.r.x/grid_width))
        j = int(floor(bacteria.r.y/grid_height))
        print(str(i) + "   "+ str(j))
        print(len(grid.sites))
        for k in range(3):
            for l in range(3):
                print("k: "+ str(k) + "l: "+str(l))
                t1 = pb(int(width/grid_width), i + k)
                t2 = pb(int(height/grid_height), j + l)
                print (str(t1) + "     " + str(t2))
                for b in grid.sites[t1][t2].contains:
                    neighbors.append(b)
        bacteria.r.add(movement(bacteria,neighbors,1.2 * cell_radius, k)).mult(eta*dt)
        
def keyPressed():
    if(key == 'i'):
        init()
    if(key == 'a'):
        print("Active Zone: ON")
        delay(500)
        active_zone_rheology_running = true
        long_rheology_running = false
        rheology_running = false
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
    






    
