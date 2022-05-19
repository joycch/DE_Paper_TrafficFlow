from src.trafficSimulator import *
# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([
    ((0, 100), (148, 100)), #lane 1 (left)
    ((148, 100), (300, 100)), #lane 2 (right)
    
    ((150, 0), (150, 98)), #lane 3 (top)
    ((150, 98), (150, 200)), #lane 4 (bottom)
])
sim.create_gen({
    'vehicle_rate': 50, #vehicles per minute, how many vehicles added in the simulation / min
    'vehicles': [
        [1, {"path": [0, 1]}], #list of tuples that contains the configuration (V) and
                               #probability (p) of the vehicules,L=[(p1, v1), (p2,v2)...] on lane 1
        [1, {"path": [0, 3]}], # idem but lane 2
        [1, {"path": [2, 3]}], # idem but lane 3
        [1, {"path": [2, 3]}] #idem but lane 4
    ]
})
sim.create_signal([[0], [2]])  #traffic light start and stop distance

# Start simulation
win = Window(sim)
win.offset = (-150, -110) #configuration of pygame
win.run(steps_per_update=5)




