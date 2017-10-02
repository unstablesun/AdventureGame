

import random


Danger0 = {'description': 'You see a swarm of red and yellow wasps!',
           'power': 2,
           'attack': 'you are in a clearing',
           'defend': 'you duck and run close to the ground',
           'damage': 'you get stung several times in the face'}


Location0 = {'id': 0, 'north': 'area1', 'west': 'blocked', 'south': 'blocked', 'east': 'blocked',
             'description': 'you are in a clearing'}
Location1 = {'id': 1, 'north': 'area2', 'west': 'area3', 'south': 'blocked', 'east': 'blocked',
             'description': 'you are in a wooded area with spoungy turf'}
Location2 = {'id': 2, 'north': 'area3', 'west': 'blocked', 'south': 'blocked', 'east': 'blocked',
             'description': 'you are at the edge of a cliff over looking a river'}
Location3 = {'id': 3, 'north': 'blocked', 'west': 'blocked', 'south': 'blocked', 'east': 'area1',
             'description': 'you are at mouth of a cave blocked by dead bodies'}

WorldLocations = {'area0': Location0, 'area1': Location1, 'area2': Location2, 'area3': Location3}


CurrentLocation = 'area0'
ActionResponseText = 'none'
PlayerHealth = 'good'


def move_from_location(direction):
    global ActionResponseText
    global CurrentLocation
    location = WorldLocations[CurrentLocation]
    direction_value = location[direction]
    # chance = random.randint(0, 100)
    if direction_value == 'blocked':
        ActionResponseText = "The way is blocked"
        print(direction_value + ActionResponseText)
    else:
        print("Moving to " + direction_value + " yes the way is clear")
        CurrentLocation = direction_value
        current_location = WorldLocations[CurrentLocation]
        ActionResponseText = current_location['description']
        print("new location desc " + ActionResponseText)


def wait_at_location():
    global ActionResponseText
    ActionResponseText = "You better do something"


def describe_location():
    global ActionResponseText
    current_location = WorldLocations[CurrentLocation]
    ActionResponseText = current_location['description']


'''
describe
move north
move west
move south
move east
attack
defend
hide
wait'''


def parse_command(command):
    if command == 'move north':
        move_from_location('north')
    elif command == 'move west':
        move_from_location('west')
    elif command == 'move south':
        move_from_location('south')
    elif command == 'move east':
        move_from_location('east')
    elif command == 'describe':
        describe_location()
    elif command == 'wait':
        wait_at_location()
    elif command == 'attack':
        wait_at_location()
    elif command == 'defend':
        wait_at_location()
    elif command == 'hide':
        wait_at_location()


# don't copy below this line


def main():
    startloc = WorldLocations[CurrentLocation]

    for key in startloc:
        print(key)
        value = startloc[key]
        print(value)

    parse_command('move north')
    parse_command('move west')
    parse_command('move east')


if __name__ == "__main__":
    main()


