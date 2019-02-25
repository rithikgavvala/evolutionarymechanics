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
    times;
    def __init__(self, r: list[int], radius:float, species_color: list[int], divided: boolean, killed: boolean, growth_rate: float):
        self.r = r
        self.neighborhood = neighborhood
        self.next_position = next_position
        self.radius = radius;
        self.species_color = species_color
        self.divided = divided 
        self.killed = killed
        self.clock = 0
        self.growth_rate = growth_rate
        self.r0 = PVector(r.x, r.y, r.z)
        self.rf = PVector(0,0,0)
        self.times = [] #list of floats
    
        
    def show():
        self.r.x = min(width, self.r.x)
        self.r.x = max(0, self.r.x)
        self.r.y = min(height, self.r.y)
        self.r.y = max(0, self.r.y)
        
        if(self.species_color.x = 255):
            if(self.trails = 0):
                fill(self.species_color.x/1.5, self.species_color.y, self.species_color.z+20, 50)
                stroke(60)
                pushMatrix()
                translate(r.x, r.y-10)
                ellipse(0,0,radius,radies)
                popMatrix()
        elif(self.species_color.z = 255):
            if(self.trails = 0):
                fill(self.species_color.x, self.species_color.y, self.species_color.z,60)
                stroke(60)
                pushMatrix()
                translate(r.x, r.y-10)
                ellipse(0,0,radius,radies)
                popMatrix()
        else:
            if(trails = 0):
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
        if(self.species_color.y = 0):
            self.radius = self.radius + (2 * pi * dt * self.growth_rate)/self.radius
                
        
