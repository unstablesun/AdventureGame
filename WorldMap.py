


Location0 = {'id': 0, 'north': 'area1', 'west': 'blocked', 'south': 'blocked', 'east': 'blocked', 'description': 'you are in a clearing'}
Location1 = {'id': 1, 'north': 'area2', 'west': 'area3', 'south': 'blocked', 'east': 'blocked', 'description': 'you are in a wooded area with spoungy turf'}
Location2 = {'id': 2, 'north': 'area3', 'west': 'blocked', 'south': 'blocked', 'east': 'blocked', 'description': 'you are at the edge of a cliff over looking a river'}
Location3 = {'id': 3, 'north': 'blocked', 'west': 'blocked', 'south': 'blocked', 'east': 'area1', 'description': 'you are at mouth of a cave blocked by dead bodies'}

WorldLocations = {'area0':Location0,'area1':Location1,'area2':Location2,'area3':Location3}

CurrentLocation = 'area0'



def MoveFromLocation(direction):
    curloc = WorldLocations[CurrentLocation]
    direction_value = curloc[direction]
    if direction_value == 'blocked':
        print(direction_value + " no the way is blocked")
    else:
        print(direction_value + " yes the way is clear")


def main():
    startloc = WorldLocations[CurrentLocation]


    for key in startloc:
        print(key)
        value = startloc[key]
        print(value)

    MoveFromLocation('north')


if __name__ == "__main__":
    main()


