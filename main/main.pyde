one_species=true
dt=.071
cell_radius=7
num_cells=0
eta=.01
max_num_cells=()((1200/cell_radius)*(400/cell_radius))
k=2.9
growth_rate=.05
kill_thresh=4
grid_width=cell_radius
grid_height=cell_radius
gravity= PVector(0,38,0)
counter=0
global_width=1200
global_height=400
Grid grid= Grid(grid_height,grid_width)
rheology_running
long_rheology_running
active_zone_rheology_running
first_run=0
Bacterium rheology_b=Bacterium(PVector(width*random(1),height-height*random(.05),0),cell_radius,PVector(0,255,0),false,false,growth_rate)
tracers= []
bottom_only=false
top_only=false
vector_plot=false
frac_to_top= []
time_to_top= []
tracer_positions= []
writenow=0
killing=0
apop_thresh=.99
save_snapshots=false

bugs = Biofilm()
growing = 1
tick = 1
initial_counter = 0
trails = 0
 
def setup(){
size(1200,400)
background(0)
init()
}
def init(){
    
           
}
