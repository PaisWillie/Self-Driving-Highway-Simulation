from Simulation.simulation import Simulation
import Config.load_config as load_config

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
                            config['simulation']['chance-gen-human-driven-vehicle'],
                            config['vehicle']['self-driven']['safe-follow'],
                            config['vehicle']['human-driven']['safe-follow'],
                            config['vehicle']['self-driven']['acceleration'],
                            config['vehicle']['human-driven']['acceleration'])
    simulation.run()