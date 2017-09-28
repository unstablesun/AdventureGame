


Location0 = {'id': 0, 'north': 'area1', 'west': 'blocked', 'south': 'blocked', 'east': 'blocked', 'description': 'you are in a clearing'}
Location1 = {'id': 1, 'north': 'area2', 'west': 'area3', 'south': 'blocked', 'east': 'blocked', 'description': 'you are in a wooded area with spoungy turf'}
Location2 = {'id': 2, 'north': 'area3', 'west': 'blocked', 'south': 'blocked', 'east': 'blocked', 'description': 'you are at the edge of a cliff over looking a river'}
Location3 = {'id': 3, 'north': 'blocked', 'west': 'blocked', 'south': 'blocked', 'east': 'area1', 'description': 'you are at mouth of a cave blocked by dead bodies'}

WorldLocations = {'area0':Location0,'area1':Location1,'area2':Location2,'area3':Location3}


CurrentLocation = 'area0'
ActionResponseText = 'none'


def MoveFromLocation(direction):
    global ActionResponseText
    global CurrentLocation
    curloc = WorldLocations[CurrentLocation]
    direction_value = curloc[direction]
    if direction_value == 'blocked':
        ActionResponseText = "The way is blocked"
        print(direction_value + ActionResponseText)
    else:
        print("Moving to " + direction_value + " yes the way is clear")
        CurrentLocation = direction_value
        curloc = WorldLocations[CurrentLocation]
        ActionResponseText = curloc['description']
        print("new location desc " + ActionResponseText)

def WaitAtLocation():
    global ActionResponseText
    ActionResponseText = "You better do something"

def DescribeLocation():
    global ActionResponseText
    curloc = WorldLocations[CurrentLocation]
    ActionResponseText = curloc['description']

#commands
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

def ParseCommand(command):
    if command == 'move north':
        MoveFromLocation('north')
    elif command== 'move west':
        MoveFromLocation('west')
    elif command== 'move south':
        MoveFromLocation('south')
    elif command== 'move east':
        MoveFromLocation('east')
    elif command== 'describe':
        DescribeLocation()
    elif command== 'wait':
        WaitAtLocation()
    elif command== 'attack':
        WaitAtLocation()
    elif command== 'defend':
        WaitAtLocation()
    elif command== 'hide':
        WaitAtLocation()





#don't copy below this line

def main():
    startloc = WorldLocations[CurrentLocation]


    for key in startloc:
        print(key)
        value = startloc[key]
        print(value)

    ParseCommand('move north')
    ParseCommand('move west')
    ParseCommand('move east')


if __name__ == "__main__":
    main()


