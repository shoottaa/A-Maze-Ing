from src.maze import Maze

DIGIT_4 = [
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
]

DIGIT_2 = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
]

GAP = 2


def pattern_42(maze: Maze) -> None:
    h = len(DIGIT_4)
    w4 = len(DIGIT_4[0])
    w2 = len(DIGIT_2[0])
    total_w = w4 + GAP + w2

    x0 = (maze.width - total_w) // 2
    y0 = (maze.height - h) // 2
    x2 = x0 + w4 + GAP

    maze.stamp_y0 = y0
    maze.stamp_h = h

    for row in range(h):
        for col in range(w4):
            pos = (x0 + col, y0 + row)
            if DIGIT_4[row][col]:
                maze.get_cell(*pos).walls = 0xF

        for col in range(w2):
            pos = (x2 + col, y0 + row)
            if DIGIT_2[row][col]:
                maze.get_cell(*pos).walls = 0xF
