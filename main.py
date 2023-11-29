import random
from colorama import Fore
from time import sleep

config = {
    "replaceSpawnsAs" : "P"
}

map = '''
______w______________
______P______________
______P______________
______P______________
______SPPPPPPS_______
_____________________
_____________________
'''
gameInfo = {
    'char' : {
        'location' : [],
        'name' : '',
        'health' : 100,
        'hunger' : 100,
        'armor' : 0,
        'inv' : {
            'hands' : {
                'funcs': {
                    'punch' : {
                        'type' : 'dmg',
                        'damage' : 5,
                        'harvestDamage' : 5,
                    },
                },
            },
        },
    },
    'worldEntities' : {
    },
}

definitions = {
    'w' : {
        'name' : 'Wolf',
        'health' : 10,
        'armor' : 0,
        'inv' : {
            'claws' : {
                'funcs' : {
                    'scratch' : {
                        'type' : 'dmg',
                        'damage' : 2,
                    },
                },
            },
        },
    },
}

# this is so stupid that I have to do all this, it should be built in

def findall(str, q):
    return list(find_all_gen(str,q))

def find_all_gen(str, q):
    i = str.find(q)
    while i != -1:
        yield i
        i = str.find(q, i+1)
        
class gameHandler():
    
    def __init__(self, map, config, definitions, gameInfo):
        self.map = map
        self.config = config
        self.definitions = definitions
        self.gameInfo = gameInfo
        
    def mapSetup(self):
        spawns = []
        rp = self.config["replaceSpawnsAs"]
        m = self.map.split("\n")
        m.pop(0)
        m.pop(-1)
        for i,v in enumerate(m):
            for r in findall(v,"S"):
                spawns.append([i,r])
        spawn = random.choice(spawns)
        self.gameInfo['char']['location'] = spawn
        spawns.remove(spawn)
        sline = m[spawn[0]]
        sline = sline[:spawn[1]] + "C" + sline[spawn[1]+1:]
        m[spawn[0]] = sline
        for i,v in enumerate(m):
            m[i] = v.replace("S",rp)
            for k,z in enumerate(self.definitions):
                if z in v:
                    for g in findall(v,z):
                        self.gameInfo['worldEntities'][(i,g)] = self.definitions[z]
        return m
    
    def charSetup(self):
        input('''
______ _             _           _   _____            _   _ 
| ___ \\ |           | |         (_) /  __ \\          | | (_)
| |_/ / | __ _ _   _| |__   ___  _  | /  \\/ __ _ _ __| |_ _ 
|  __/| |/ _` | | | | '_ \\ / _ \\| | | |    / _` | '__| __| |
| |   | | (_| | |_| | |_) | (_) | | | \\__/\\ (_| | |  | |_| |
\\_|   |_|\\__,_|\\__, |_.__/ \\___/|_|  \\____/\\__,_|_|   \\__|_|
                __/ |                                       
                |___/                                 
            
                    TEXT ADVENTURE    
        
                PRESS [ENTER] TO START.   
                            ''')
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        self.gameInfo['char']['name'] = input("Please enter your name.\n\n> ")
            

game = gameHandler(map, config, definitions, gameInfo)
game.mapSetup()
game.charSetup()
