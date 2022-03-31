import yaml

def init():
    with open('config.yaml') as f:
        global data
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data

def get():
    return data