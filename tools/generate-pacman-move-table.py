import sys
import numpy as np
import heapq
from pathlib import Path
from PIL import Image

sys.path.append(str((Path(__file__).parent / '../src').resolve()))

from rendering.GameMode import Direction 

def dijkstra(ghost_pos, ghost_dir, allowed_positions) -> list[Direction]:
    # Positions are (x, y) tuples
    # allowed_positions is a set of (x, y) positions where movement is allowed

    # Priority queue: (distance, position, path_so_far)
    queue = [(0, ghost_pos, [ghost_dir])]
    visited = set()
    
    width = allowed_positions.shape[1]
    height = allowed_positions.shape[0]

    move_table = np.ndarray(allowed_positions.shape, dtype=Direction)
    cost_table = np.ndarray(allowed_positions.shape, dtype=int)

    move_table[:, :] = ghost_dir
    cost_table[:, :] = -1
    
    x,y = ghost_pos
    if not allowed_positions[y,x]:
        return move_table, cost_table

    while queue:
        dist, current_pos, path = heapq.heappop(queue)

        # if current_pos == pacman_pos:
        #     return path  # Found the path to Pac-Man

        if current_pos in visited:
            continue
        
        if current_pos != ghost_pos:
            visited.add(current_pos)

        # Explore neighbors: up, down, left, right
        x, y = current_pos

        if len(path) > 1:
            move_table[y, x] = path[1]
            cost_table[y, x] = dist

        neighbors = [
            (Direction.LEFT,  x - 1, y    ),
            (Direction.RIGHT, x + 1, y    ),
            (Direction.UP,    x,     y - 1),
            (Direction.DOWN,  x,     y + 1),
        ]

        possible_moves = {direction: False for direction in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]}
        n_moves = 0
        for direction, x, y in neighbors:
            # don't turn around
            if (
                (path[-1] == Direction.LEFT and direction == Direction.RIGHT)
                or (path[-1] == Direction.RIGHT and direction == Direction.LEFT)
                or (path[-1] == Direction.UP and direction == Direction.DOWN)
                or (path[-1] == Direction.DOWN and direction == Direction.UP)
            ):
                continue

            if path[-1] != direction:
                new_path = path + [direction]
            else:
                new_path = path

            if (0 <= x < width) and (0 <= y < height) and allowed_positions[y,x]:
                possible_moves[direction] = True
                n_moves += 1

        for direction, x, y in neighbors:
            if not possible_moves[direction]:
                continue

            if n_moves > 1:
                new_path = path + [direction]
            else:
                new_path = path

            heapq.heappush(queue, (dist + 1, (x,y), new_path))

    return move_table, cost_table

def load_img(path):
    try:
        with Image.open(path) as img:
            return np.array(img.convert('RGB'))
    except Exception as e:
        print(f"can't load image: {e}")
        
def save_table(path, table):
    np.savez(path, **table)

if __name__ == '__main__':
    print("loading coordinate grid ... ", end='', flush=True)
    assets = (Path(__file__).parent / '../assets').resolve()
    allowed_coords = np.any(load_img(assets/'Ghost-Coords.png'), axis=2)

    width = allowed_coords.shape[1]
    height = allowed_coords.shape[0]
    print("done")

    print("calculating shortest paths ... ", end='', flush=True)
    move_table = {}
    cost_table = {}
    for direction in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]:
        move_table[direction.name] = np.ndarray((height, width, height, width), dtype=Direction)
        cost_table[direction.name] = np.ndarray((height, width, height, width), dtype=int)
        
        for y in range(height):
            for x in range(width):
                mtbl, ctbl = dijkstra((x,y), direction, allowed_coords)
                move_table[direction.name][y,x] = mtbl
                cost_table[direction.name][y,x] = ctbl
    print("done")

    # table = {direction.name: np.array([[dijkstra((x,y), direction, allowed_coords) for x in range(width)] for y in range(height)]) for direction in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]}
    
    print("saving tables ... ", end='', flush=True)
    save_table(assets/'PacMan-Move-Table', move_table)
    save_table(assets/'PacMan-Cost-Table', cost_table)
    print("done")