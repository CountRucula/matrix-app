from rendering.RenderMode import RenderMode
import numpy as np
import enum
from collections import deque
import time
import random

class Direction(enum.Enum):
    UP      = 0
    DOWN    = 1
    LEFT    = 2
    RIGHT   = 3

class SnakeMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.start_coords = [(10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15,10)]

        self.snake_color        = ( 62, 137,  72)
        self.dark_snake_color   = ( 25,  60,  62)
        self.eye_color          = (251, 192,  45)
        self.apple_color        = (255,   0,   0)
        self.apple_stem_color   = ( 86,  59,  12)

        self.reset()

        self.f = 5

    def reset(self):
        self.clear()
        self.game_running = False
        self.game_over = True

        self.dir = Direction.RIGHT
        self.new_dir = Direction.RIGHT
        self.last_dir = Direction.RIGHT
        self.moved_since_turn = 0

        self.apple = (None, None)
        self.apple_body = []

        self.snake = deque(self.start_coords)
        self.snake_growing = 0
        self.snake_body = set()

        self.draw_snake()

    def start_pause(self):
        if self.game_running:
            self.game_running = False

        else:
            if self.game_over:
                self.reset()
                self.place_apple()
                self.game_over = False

            self.start_time = time.time()
            self.game_running = True
        

    def place_apple(self):
        free = [
            (x, y)
            for x in range(1, self.width - 1)
            for y in range(2, self.height - 1)
            if all(
                (xi, yi) not in self.snake_body
                for xi in range(x - 1, x + 2)
                for yi in range(y - 1, y + 2)
            )
        ]

        n_free = len(free)

        pos = random.randint(0, n_free-1)

        self.apple = free[pos]

    def move(self):
        head = self.snake[-2]
        nose = self.snake[-1]

        x_head, y_head = head
        x_nose, y_nose = nose

        # make a turn
        if self.dir != self.new_dir:
            if ( not (
                    (self.last_dir == Direction.UP and self.new_dir == Direction.DOWN)
                    or (self.last_dir == Direction.DOWN and self.new_dir == Direction.UP) 
                    or (self.last_dir == Direction.LEFT and self.new_dir == Direction.RIGHT) 
                    or (self.last_dir == Direction.RIGHT and self.new_dir == Direction.LEFT)
                )
                or self.moved_since_turn >= 3
            ):
                self.last_dir = self.dir
                self.dir = self.new_dir
                self.moved_since_turn = 0

        self.moved_since_turn += 1

        # move head & nose
        match self.dir:
            case Direction.RIGHT:
                x_head += 1
                x_nose = x_head + 1

                y_nose = y_head

                eyes = ((x_head,y_head-1), (x_head,y_head+1))

            case Direction.LEFT:
                x_head -= 1
                x_nose = x_head - 1

                y_nose = y_head

                eyes = ((x_head,y_head-1), (x_head,y_head+1))

            case Direction.UP:
                x_nose = x_head

                y_head -= 1
                y_nose = y_head - 1

                eyes = ((x_head-1,y_head), (x_head+1,y_head))

            case Direction.DOWN:
                x_nose = x_head

                y_head += 1
                y_nose = y_head + 1

                eyes = ((x_head-1,y_head), (x_head+1,y_head))

        head = (x_head,y_head)
        nose = (x_nose,y_nose)

        # check if game over
        lost = self.check(nose, eyes)

        if not lost:
            # grow
            if nose in self.apple_body:
                self.place_apple()
                self.snake_growing = 3
            
            # still growing
            if self.snake_growing:
                self.snake_growing -= 1

            # moving normal
            else:
                self.snake.popleft()

            self.snake[-1] = head
            self.snake.append(nose)

    def change_direction(self, direction: Direction):
        if direction in (Direction.UP, Direction.DOWN):
            if self.dir not in (Direction.UP, Direction.DOWN):
                self.new_dir = direction

        else:
            if self.dir not in (Direction.LEFT, Direction.RIGHT):
                self.new_dir = direction


    def check(self, nose, eyes):
        x,y = nose

        # nose touched body
        if nose in self.snake_body:
            self.game_end()
            return True

        # eyes touched body
        if (eyes[0] in self.snake_body or eyes[1] in self.snake_body) and self.moved_since_turn > 1:
            self.game_end()
            return True

        # nose touch game edges
        if y < 0 or y >= self.height:
            self.game_end()
            return True

        if x < 0 or x >= self.width:
            self.game_end()
            return True

        return False

    def game_end(self):
        self.game_over = True
        self.game_running = False
        print("game over")

    def draw_snake(self):
        length = len(self.snake)
        old = (0,0)

        self.snake_body = set()

        for i, pos in enumerate(self.snake):
            direction = self.get_dir(pos, old)
            x,y = pos

            # tail
            if i == 0:
                self.framebuffer[y,x] = self.snake_color
                self.snake_body.add(pos)

            # head
            elif i == (length - 1):
                self.framebuffer[y,x] = self.snake_color

            # eyes
            elif i == (length - 2):
                self.framebuffer[y,x] = self.snake_color

                if direction in (Direction.UP, Direction.DOWN):
                    self.framebuffer[y, x-1] = self.eye_color
                    self.framebuffer[y, x+1] = self.eye_color

                elif direction in (Direction.LEFT, Direction.RIGHT):
                    self.framebuffer[y-1, x] = self.eye_color
                    self.framebuffer[y+1, x] = self.eye_color
                
            # body
            else:
                self.framebuffer[y-1:y+2,x] = self.snake_color
                self.framebuffer[y,x-1:x+2] = self.snake_color

                self.snake_body.add(pos)
                if direction in (Direction.UP, Direction.DOWN):
                    self.snake_body.add((x-1, y))
                    self.snake_body.add((x+1, y))

                elif direction in (Direction.LEFT, Direction.RIGHT):
                    self.snake_body.add((x, y-1))
                    self.snake_body.add((x, y+1))

            old = (x,y)

        for i, (x,y) in enumerate(self.snake):
            if ((i % 3) == 1) and (i < (length - 1)):
                self.framebuffer[y,x] = self.dark_snake_color


    def get_dir(self, pos, old_pos) -> Direction:
        if pos[0] > old_pos[0]:
            return Direction.RIGHT
        elif pos[0] < old_pos[0]:
            return Direction.LEFT
        
        if pos[1] > old_pos[1]:
            return Direction.DOWN
        elif pos[1] < old_pos[1]:
            return Direction.UP
        
        return None

    def draw_apple(self):
        x,y = self.apple

        self.apple_body = [(xi,yi) for xi in range(x-1,x+2) for yi in range(y-1,y+2)]

        self.framebuffer[y-2, x] = self.apple_stem_color
        self.framebuffer[y-1:y+2,x-1:x+2] = self.apple_color

        corners = np.array([[y-1, y-1, y+1, y+1], 
                            [x-1, x+1, x-1, x+1]])

        self.framebuffer[*corners] = self.framebuffer[*corners] * 0.6

    def render(self):
        if self.game_running:
            elapsed = time.time() - self.start_time

            if elapsed >= (1/self.f):
                self.start_time = time.time()
                self.move()
                self.clear()
                self.draw_apple()
                self.draw_snake()

        return self.framebuffer