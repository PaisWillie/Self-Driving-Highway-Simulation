# TODO List
# - Car speed & accerleration
# - Lane change only into accessible lanes
# - Abstract vehicle class
# - Changing number of self-driving vehicle only lanes
# - Highway abstract class (different speed limit)
# - Ratio of self-driven to human-driven vehicles
# - Multiple entry/exit points
# - Multiple lanes
# - Different desired speed target per driver
# - Intention to merge off of self-driving lane if current lane converted

# TODO: Self-driven vehicle class
from Simulation.simulation import Simulation
import load_config

if __name__ == '__main__':
    load_config.init()
    config = load_config.get()
    simulation = Simulation(config['highway']['length'],
                            config['highway']['self-driving-lane']['count'],
                            config['highway']['shared-lane']['count'],
                            config['highway']['self-driving-lane']['speed-limit'],
                            config['highway']['shared-lane']['speed-limit'],
                            config['simulation']['time-steps'],
                            config['highway']['entry-points'],
                            config['simulation']['chance-gen-self-driven-vehicle'],
                            config['simulation']['chance-gen-human-driven-vehicle'])
    simulation.run()