from dataclasses import dataclass, field
import numpy
from random import choice

@dataclass
class MazeCell:
    x: int
    y: int
    component: int
    is_open: bool = field(default=False)
    walls: list = field(default_factory=list)

def find(x):
    return x.component

def union(x: MazeCell, y: MazeCell):
    global components
    global current_maze
    x_count = 0
    y_count = 0
    for i in components:
        if i == x.component:
            x_count += 1
        if i == y.component:
            y_count += 1

    if x_count > y_count:
        big_component = x.component
        small_component = y.component
    else:
        big_component = y.component
        small_component = x.component

    for i in range(len(components)):
        if components[i] == small_component:
            components[i] = big_component

    for i in current_maze:
        for j in i:
            if j.component == small_component:
                j.component = big_component

    if x.x > y.x:
        x.walls[3] = False
        y.walls[1] = False
    elif y.x > x.x:
        y.walls[3] = False
        x.walls[1] = False
    elif x.y > y.y:
        x.walls[0] = False
        y.walls[2] = False
    else:
        y.walls[0] = False
        x.walls[2] = False

def generate_maze(size) -> list[list[MazeCell]]:
    global current_maze
    global components
    current_maze = []

    for i in range(size):
        current_maze.append([])
        for j in range(size):
            current_maze[i].append(MazeCell(j, i, (j + i * size), False, [True, True, True, True]))

    components = numpy.arange(size**2)
    while len(numpy.unique(components)) != 1:
        x = numpy.random.choice(numpy.arange(size))
        y = numpy.random.choice(numpy.arange(size))
        neighbours = list()
        if y != 0:
            neighbours.append((y - 1, x))
        if x != size - 1:
            neighbours.append((y, x + 1))
        if y != size - 1:
            neighbours.append((y + 1, x))
        if x != 0:
            neighbours.append((y, x - 1))
        random_neighbour = choice(neighbours)
        if find(current_maze[random_neighbour[0]][random_neighbour[1]]) != find(current_maze[y][x]):
            union(current_maze[random_neighbour[0]][random_neighbour[1]], current_maze[y][x])

    current_maze[0][0].is_open = True
    current_maze[-1][-1].is_open = True
    current_maze[0][0].walls[0] = False
    current_maze[-1][-1].walls[2] = False

    return current_maze
