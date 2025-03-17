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

        self.snake_color        = (  0, 255,   0)
        self.dark_snake_color   = ( 13, 102,  14)
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

        self.apple = (None, None)

        self.snake = deque(self.start_coords)
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
        free = [(x,y) for x in range(1, self.width-1) for y in range(1, self.height-1) if (x,y) not in self.snake]
        n_free = len(free)

        pos = random.randint(0, n_free-1)

        self.apple = free[pos]

    def move(self):
        head = self.snake[-1]
        x,y = head

        self.dir = self.new_dir

        match self.dir:
            case Direction.RIGHT:
                x += 1

            case Direction.LEFT:
                x -= 1

            case Direction.UP:
                y -= 1

            case Direction.DOWN:
                y += 1

        head = (x,y)

        lost = self.check(head)

        if not lost:
            if head == self.apple:
                self.place_apple()
            else:
                self.snake.popleft()

            self.snake.append(head)

    def change_direction(self, direction: Direction):
        if direction in (Direction.UP, Direction.DOWN):
            if self.dir not in (Direction.UP, Direction.DOWN):
                self.new_dir = direction

        else:
            if self.dir not in (Direction.LEFT, Direction.RIGHT):
                self.new_dir = direction


    def check(self, new_head):
        x,y = new_head

        if new_head in self.snake:
            self.game_end()
            return True

        if y < 1 or y >= self.height-1 :
            self.game_end()
            return True

        if x < 1 or x >= self.width-1:
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

        for i, pos in enumerate(self.snake):
            direction = self.get_dir(pos, old)
            x,y = pos

            # tail
            if i == 0:
                self.framebuffer[y,x] = self.snake_color

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
                self.framebuffer[y,x-1:x+2] = self.snake_color
                self.framebuffer[y-1:y+2,x] = self.snake_color

            old = (x,y)

        for i, (x,y) in enumerate(self.snake, 1):
            if ((i % 3) == 2) and (i < (length - 2)):
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