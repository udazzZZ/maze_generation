import matplotlib.pyplot as plt
from generate import generate_maze

N = 30
LINE_WIDTH = 50


def draw_maze(maze):
    x = 0
    y = 0
    for i in maze:
        for j in i:
            if j.walls[0]:
                plt.plot([x, x + LINE_WIDTH], [y, y], 'k-', lw=2)
            if j.walls[3]:
                plt.plot([x, x], [y, y - LINE_WIDTH], 'k-', lw=2)
            if j.walls[1]:
                plt.plot([x + LINE_WIDTH, x + LINE_WIDTH], [y, y - LINE_WIDTH], 'k-', lw=2)
            if j.walls[2]:
                plt.plot([x, x + LINE_WIDTH], [y - LINE_WIDTH, y - LINE_WIDTH], 'k-', lw=2)
            x += LINE_WIDTH
        y -= LINE_WIDTH
        x = 0


maze = generate_maze(N)

fig = plt.figure(figsize=(10, 10))

draw_maze(maze)

plt.show()