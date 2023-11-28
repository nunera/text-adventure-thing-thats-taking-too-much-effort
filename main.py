import random
from colorama import Fore

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

def mapSetup(m):
    spawns = []
    rp = config["replaceSpawnsAs"]
    m = m.split("\n")
    m.pop(0)
    m.pop(-1)
    for i,v in enumerate(m):
        for r in findall(v,"S"):
            spawns.append([i,r])
    spawn = random.choice(spawns)
    spawns.remove(spawn)
    sline = m[spawn[0]]
    sline = sline[:spawn[1]] + "C" + sline[spawn[1]+1:]
    print(sline)
    m[spawn[0]] = sline
    for i,v in enumerate(m):
        m[i] = v.replace("S",rp)
        for k,z in enumerate(definitions):
            if z in v:
                for g in findall(v,z):
                    gameInfo['worldEntities'][(i,g)] = definitions[z]
                
    print(gameInfo)
    return m

map = mapSetup(map)
