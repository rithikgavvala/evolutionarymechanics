class Bacteria:
    r = ""
    neighborhood = ""
    next_position = ""
    radius = ""
    species_color = ""
    divided = ""
    killed = ""
    clock = ""
    growth_rate = ""
    enemy_count = ""
    r0 = ""
    rf = ""
    long_rheology_list;
    times;
    bin;
    def __init__(self, r, radius, species_color, divided, killed, growth_rate):
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
        self.long_rheology_list = []
        self.times = []
        self.bin = 99
        
    def show():
        r.x = min(width, r.x)
        r.x = max(0, r.x)
        r.y = min(height, r.y)
        r.y = max(0, r.y)
        
        if(species_color.x = 255):
            if(trails = 0):
                fill(species_color.x/1.5, species_color.y, species_color.z+20, 50)
                stroke(60)
                pushMatrix()
                translate(r.x, r.y-10)
                ellipse(0,0,radius,radies)
                popMatrix()
        elif(species_color.z = 255):
            if(trails = 0):
                fill(species_color.x, species_color.y, species_color.z,60)
                stroke(60)
                pushMatrix()
                translate(r.x, r.y-10)
                ellipse(0,0,radius,radies)
                popMatrix()
        else:
            if(trails = 0):
                fill(species_color.x, species_color.y, species_color.z)
                noStroke()
                pushMatrix()
                translate(r.x, r.y-10)
                ellipse(0,0,radius,radies)
                popMatrix()
            else:
                fill(species_color.x,species_color.y, species_color.z);
                noStroke();
                pushMatrix();
                translate(r.x, r.y-10);
                ellipse(0,0,radius/4,radius/4);
                popMatrix();  
    def grow():
        if(species_color.y = 0):
            radius = radius + (2 * pi * dt * growth_rate)/radius
                
        
