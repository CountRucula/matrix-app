from rendering.RenderMode import RenderMode
import numpy as np
import enum
from collections import deque
import time
import random
from typing import Literal
from PIL import Image
from fonts import font_5x7
from pathlib import Path
import logging
from functools import total_ordering

@total_ordering
class Direction(enum.Enum):
    UP      = 0
    DOWN    = 1
    LEFT    = 2
    RIGHT   = 3
    
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    

    inverse = {
        LEFT    : RIGHT,
        RIGHT   : LEFT,
        UP      : DOWN,
        DOWN    : UP,        
    }
    
    def inv(self):
        return Direction(Direction.inverse.value[self.value])

def load_img(path):
    try:
        with Image.open(path) as img:
            return np.array(img.convert('RGB'))
    except Exception as e:
        logging.error(f"can't load image: {e}")

def load_gif(path):
    try:
        with Image.open(path) as img:
            frames = []
            
            while True:
                duration = img.info.get('duration', 50)  # Duration in milliseconds
                
                frames.append((np.array(img.convert('RGB')), duration))
                try:
                    img.seek(img.tell() + 1)
                except EOFError:
                    break

            return frames
    except Exception as e:
        logging.error(f"can't load gif: {e}")

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
                self.start_mode()
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

class PongMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.ball_size = 2
        self.ball_color = np.array((255,255,255))

        self.player_length = 4
        self.player_speed = 15.0
        self.player_color = np.array((255,255,255))

        self.middle_line_width = 2
        self.middle_line_color = np.array((255, 0, 0))

        self.score_color = np.array((0, 255, 0))

        self.start_time = time.time()

        self.winning_score = 9

        self.start_mode()

    def start_mode(self):
        self.game_running = False
        self.ball = None
        self.ball_speed = 0.0

        self.player1 = self.height/2
        self.player1_speed = 0
        self.player1_score = 0

        self.player2 = self.height/2
        self.player2_speed = 0
        self.player2_score = 0

        self.round = 0
        self.round_running = False
        self.round_countdown = 1.0

    def set_player_pos(self, player: int, pos: float):
        max_y = float(self.height-self.player_length) - 1e-6

        pos = pos/100.0*max_y
        pos = max(min(pos, max_y), 0)

        match player:
            case 1:
                self.player1 = pos

            case 2:
                self.player2 = pos


    def set_player_dir(self, player: int, direction: int):
        direction = max(min(direction, 1), -1)

        match player:
            case 1:
                self.player1_speed = direction * self.player_speed

            case 2:
                self.player2_speed = direction * self.player_speed

    def move_ball(self, phi: int, delta_t: float):
        # wrap phase
        phi = (phi+np.pi) % (2*np.pi) - np.pi

        x,y = self.ball

        x += np.cos(phi) * self.ball_speed * delta_t
        y += np.sin(phi) * self.ball_speed * delta_t

        # reflect left 
        if (1+self.ball_size/2 + 1e-6) >= x and not (-np.pi/2 < phi < np.pi/2):
            if not self.handle_collision('left'):
                self.round_over('right')

            x = self.ball_size/2 + 1e-6
        
        # reflect right 
        if x >= (self.width - 1 - self.ball_size/2 - 1e-6) and (-np.pi/2 < phi < np.pi/2):
            if not self.handle_collision('right'):
                self.round_over('left')

            x = self.width - (self.ball_size/2 + 1e-6)

        # reflect top 
        if (self.ball_size/2 + 1e-6) >= y and (-np.pi < phi < 0):
            self.ball_dir = -self.ball_dir
            y = self.ball_size/2 + 1e-6
        
        # reflect bottom 
        if y >= (self.height - self.ball_size/2 - 1e-6) and (0 < phi < np.pi):
            self.ball_dir = -self.ball_dir
            y = self.height - (self.ball_size/2 + 1e-6)

        self.ball = (x,y)

    def handle_collision(self, side: Literal['left', 'right']) -> bool:
        _,yb = self.ball

        if side == 'left':
            self.ball_speed += 0.1*abs(self.player1_speed)

            if (yb+self.ball_size/2) < self.player1:
                return False

            # top corner
            elif yb < (self.player1 + self.ball_size/2):
                if (self.ball_dir) > 0 or (self.ball_dir < -9/10*np.pi):
                    self.ball_dir = -self.ball_dir - 4/3*np.pi
                else:
                    self.ball_dir = -self.ball_dir - np.pi

                return True

            # body
            elif yb < (self.player1+self.player_length-self.ball_size/2):
                self.ball_dir = -self.ball_dir - np.pi
                return True

            # bottom corner
            elif (yb-self.ball_size/2) < (self.player1 + self.player_length):
                if (self.ball_dir < 0) or (self.ball_dir > 9/10*np.pi):
                    self.ball_dir = -self.ball_dir - 2/3*np.pi
                else:
                    self.ball_dir = -self.ball_dir - np.pi

                return True

            else:
                return False
        else:
            self.ball_speed += 0.1*abs(self.player2_speed)

            if (yb+self.ball_size/2) < self.player2:
                return False

            # top corner
            elif yb < (self.player2 + self.ball_size/2):
                if self.ball_dir > -np.pi/10:
                    self.ball_dir = -self.ball_dir + 4/3*np.pi
                else:
                    self.ball_dir = -self.ball_dir - np.pi

                return True

            # body
            elif yb < (self.player2+self.player_length-self.ball_size/2):
                self.ball_dir = -self.ball_dir - np.pi
                return True

            # bottom corner
            elif (yb-self.ball_size/2) < (self.player2 + self.player_length):
                if self.ball_dir > np.pi/10:
                    self.ball_dir = -self.ball_dir - np.pi
                else:
                    self.ball_dir = -self.ball_dir + 2/3*np.pi
                return True

            else:
                return False


    def game_start(self):
        self.reset()
        self.round_start()

        self.game_running = True

    def round_start(self):
        self.player1 = self.height/2
        self.player1_speed = 0

        self.player2 = self.height/2
        self.player2_speed = 0

        self.ball_speed = 20.0
        self.ball_dir = (np.random.random() * np.pi/2) - np.pi/4 - (np.random.randint(0, 2)*np.pi)
        self.ball = (self.width/2, self.height/2)

        self.round_running = True
        self.round += 1

    def round_over(self, winner: Literal['left', 'right']):
        self.round_running = False
        self.round_countdown = 1.0

        if winner == 'left':
            self.player1_score += 1

            if self.player1_score >= self.winning_score:
                self.game_over()

        elif winner == 'right':
            self.player2_score += 1

            if self.player2_score >= self.winning_score:
                self.game_over()

    def game_over(self):
        self.ball_speed = 0
        self.game_running = False
        print("game-over")

    def move_player(self, pos: int, speed: float, delta_t: float):
        pos += speed * delta_t

        pos = max(pos, 0)
        pos = min(pos, self.height - self.player_length - 1e-6)

        return pos

    def draw_ball(self):
        x,y = self.ball

        x -= self.ball_size/2
        y -= self.ball_size/2

        ix = int(x)
        iy = int(y)

        intensity_right = x - ix
        intensity_left  = 1 - intensity_right

        intensity_bot   = y - iy
        intensity_top   = 1 - intensity_bot

        # corners
        self.framebuffer[iy,                ix]                 = self.ball_color * intensity_top * intensity_left  # top-left
        self.framebuffer[iy,                ix+self.ball_size]  = self.ball_color * intensity_top * intensity_right # top-right
        self.framebuffer[iy+self.ball_size, ix]                 = self.ball_color * intensity_bot * intensity_left  # bottom-left
        self.framebuffer[iy+self.ball_size, ix+self.ball_size]  = self.ball_color * intensity_bot * intensity_right # bottom-right

        # edges
        self.framebuffer[iy,                        ix+1:ix+self.ball_size] = self.ball_color * intensity_top   # top
        self.framebuffer[iy+self.ball_size,         ix+1:ix+self.ball_size] = self.ball_color * intensity_bot   # bottom
        self.framebuffer[iy+1:iy+self.ball_size,    ix]                     = self.ball_color * intensity_left  # left
        self.framebuffer[iy+1:iy+self.ball_size,    ix+self.ball_size]      = self.ball_color * intensity_right # right

        # body
        self.framebuffer[iy+1:iy+self.ball_size, ix+1:ix+self.ball_size] = self.ball_color

    def draw_player(self, x, pos):
        ipos_start = int(pos)
        ipos_end = ipos_start+self.player_length

        self.framebuffer[ipos_start,            x] = self.player_color * (ipos_start + 1 - pos)
        self.framebuffer[ipos_start+1:ipos_end, x] = self.player_color
        self.framebuffer[ipos_end,              x] = self.player_color * (pos - ipos_start)

    def draw_middle_line(self):
        size = self.middle_line_width

        coords = np.array([(y, x + self.width//2 - size/2) for y in range(self.height) for x in range(size) if ((y-1) % (2*size)) < size], dtype=int)

        self.framebuffer[coords[:,0], coords[:,1]] = self.middle_line_color

    def draw_score(self, score: int, position: Literal['left', 'right']):
        score_str = str(score)
        bitmap = font_5x7.Characters[score_str[0]]

        char_width = len(bitmap[0])
        char_height = len(bitmap)

        if position == 'left':
            x_start = self.width//2 - self.middle_line_width//2 - 2 - char_width
        else:
            x_start = self.width//2 + self.middle_line_width//2 + 2

        self.framebuffer[1:1+char_height, x_start:x_start+char_width] = np.einsum('ik,j->ikj', bitmap, self.score_color)

    def render(self):
        elapsed = time.time() - self.start_time
        self.start_time = time.time()

        # clear buffer
        self.clear()

        if self.game_running:

            if not self.round_running:
                self.round_start()

            if self.round_countdown <= 0:
                # move players
                self.player1 = self.move_player(self.player1, self.player1_speed, elapsed)
                self.player2 = self.move_player(self.player2, self.player2_speed, elapsed)

                # move ball
                if self.ball is not None:
                    self.move_ball(self.ball_dir, elapsed)

            else:
                self.round_countdown -= elapsed
            
        # draw objects
        self.draw_middle_line()
        self.draw_score(self.player1_score, 'left')
        self.draw_score(self.player2_score, 'right')
    
        if self.ball is not None:    
            self.draw_ball()

        self.draw_player(0, self.player1)
        self.draw_player(-1, self.player2)

        return self.framebuffer
    
class Sprite:
    def __init__(self, pixels, grid, animated):
        self.pixels = pixels
        self.is_animated = animated
        self.grid = grid
        
        if self.is_animated:
            self.w = self.pixels[0][0].shape[1]
            self.h = self.pixels[0][0].shape[0]
        else:
            self.w = self.pixels.shape[1]
            self.h = self.pixels.shape[0]

        self.abs_speed = 10

        self.dir: Direction = Direction.LEFT
        self.new_dir: Direction = Direction.LEFT

        self.speed = np.array([0,0], float)
        self.new_speed = np.array([0,0], float)
        self.idx = 0
        
        self.pos = (1, 0)
        self.next_stop = self.pos

        self.start = time.time()
        
    def reset_animation(self):
        self.start = time.time()
        self.idx = 0
        
    def set_pos(self, pos) -> None:
        self.pos = pos
        self.find_next_turn(self.pos)
    
    def set_new_dir(self, direction: Direction) -> None:
        if direction is None:
            self.speed[:] = [0, 0]
            return

        self.new_dir = direction

        match self.new_dir:
            case Direction.LEFT:
                self.new_speed[:] = [-1, 0]

            case Direction.RIGHT:
                self.new_speed[:] = [1, 0]

            case Direction.UP:
                self.new_speed[:] = [0, -1]

            case Direction.DOWN:
                self.new_speed[:] = [0, 1]
                
        self.new_speed *= self.abs_speed
        self.find_next_turn(self.pos)
        
    def set_dir(self, direction: Direction):
        self.set_new_dir(direction)
        self.dir = self.new_dir
        self.speed = self.new_speed.copy()

    def available_directions(self, pos) -> list[Direction]:
        x, y = pos
        
        neighbours = [
            [Direction.RIGHT, x + 1, y],
            [Direction.LEFT, x - 1, y],
            [Direction.DOWN, x, y + 1],
            [Direction.UP, x, y - 1]
        ]
        
        return [direction for direction, x, y in neighbours if (0 <= x <= self.grid.shape[1]) and (0 <= y <= self.grid.shape[0]) and self.grid[y,x]]
        
    def find_next_turn(self, pos):
        x,y = pos
        x = int(x)
        y = int(y)

        moves = {
            Direction.LEFT:     (-1,  0),
            Direction.RIGHT:    ( 1,  0),
            Direction.UP:       ( 0, -1),
            Direction.DOWN:     ( 0,  1)
        }
        
        # move until next stop
        xn = x
        yn = y
        
        directions = self.available_directions((xn,yn))
        i = 0
        while self.dir in directions and (len(directions) <= 2 or i == 0):
            xn += moves[self.dir][0]
            yn += moves[self.dir][1]

            directions = self.available_directions((xn,yn))
            i += 1

        self.next_stop = (xn, yn)
        
    def reached_pos(self, pos, target):
        reached = {
            Direction.LEFT  : int(pos[0]) <= target[0],
            Direction.RIGHT : int(pos[0]) >= target[0],
            Direction.UP    : int(pos[1]) <= target[1],
            Direction.DOWN  : int(pos[1]) >= target[1]
        }

        return reached[self.dir]
    
    def move(self, elapsed: float) -> None:
        new_pos = self.pos + self.speed*elapsed
        
        if self.new_dir == self.dir.inv():
            self.speed = self.new_speed.copy()
            self.dir = self.new_dir
            
            # find next turn
            self.find_next_turn(self.pos)
            
        elif self.reached_pos(new_pos, self.next_stop): 
            x, y = self.next_stop
                
            # can't continue => stop
            if not self.check_dir(self.dir, x, y):
                self.speed[0] = 0
                self.speed[1] = 0
                new_pos = self.next_stop

            # can turn => turn
            if self.check_dir(self.new_dir, x, y):
                new_pos = self.next_stop
                    
                self.speed = self.new_speed.copy()
                self.dir = self.new_dir

                # find next turn
                self.find_next_turn(new_pos)

        elif np.all(self.speed == 0):
            x,y = self.pos
            x = int(x)
            y = int(y)

            if self.check_dir(self.new_dir, x, y):
                self.speed = self.new_speed.copy()
                self.dir = self.new_dir

                # find next turn
                self.find_next_turn(self.pos)
             
        # limit field
        field_width = self.grid.shape[1]
        field_height = self.grid.shape[0]
        
        x_new, y_new = new_pos
        if not 0 <= x_new <= (field_width-self.w):
            x_new = max(0, min(x_new, field_width-self.w))
            self.speed[:] = [0, 0]

        if not 0 <= y_new <= (field_height-self.h):
            y_new = max(0, min(y_new, field_height-self.h))
            self.speed[:] = [0, 0]

        self.pos = (x_new, y_new)

    def check_dir(self, direction: Direction, x: int, y: int) -> bool:
        field_width = self.grid.shape[1]
        field_height = self.grid.shape[0]

        match direction:
            case Direction.LEFT:
                x -= 1
                # x = max(0, x-1)

            case Direction.RIGHT:
                x += 1
                # x = min(field_width-self.w, x+1)

            case Direction.UP:
                y -= 1
                # y = max(0, y-1)

            case Direction.DOWN:
                y += 1
                # y = min(field_height-self.h, y+1)

        if not 0 <= x <= (field_width-self.w):
            return False
        if not 0 <= y <= (field_height-self.h):
            return False

        return self.grid[y,x]

    def draw_aa(self, x: float, y: float, sprite: np.ndarray, buffer: np.ndarray) -> None:
        def ipart(x): return int(x)    
        def fpart(x): return x - int(x)
        def rfpart(x): return 1 - x + int(x)

        w,h = sprite.shape[:2]
        
        ix, iy = ipart(x), ipart(y)
        fx, fy = fpart(x), fpart(y)
        rfx, rfy = rfpart(x), rfpart(y)

        buffer[iy, ix] =  rfx*rfy*sprite[0, 0]
        
        buffer[iy,   ix+1:ix+w] = rfy*(fx*sprite[ 0, :-1] + rfx*sprite[ 0, 1:]) # top row
        if fy > 10e-3:
            buffer[iy+h, ix+1:ix+w] =  fy*(fx*sprite[-1, :-1] + rfx*sprite[-1, 1:]) # bottom row
            buffer[iy+h, ix       ] = rfx*fy*sprite[-1, 0] # bottom-left corner
        
        buffer[iy+1:iy+h, ix  ] = rfx*(fy*sprite[:-1,  0] + rfy*sprite[1:,  0]) # left column
        if fx > 10e-3:
            buffer[iy+1:iy+h, ix+w] =  fx*(fy*sprite[:-1, -1] + rfy*sprite[1:, -1]) # right column
            buffer[iy, ix+w] = fx*rfy*sprite[0, -1] # top-right cornen
            
        if (fx > 10e-3) and (fy > 10e-3):
            buffer[iy+h, ix+w] = fx*fy*sprite[-1, -1] # bottom-right corner
        
        buffer[iy+1:iy+h, ix+1:ix+w] = fy*(fx*sprite[:-1, :-1] + rfx*sprite[:-1, 1:]) + rfy*(fx*sprite[1:, :-1] + rfx*sprite[1:, 1:]) # body
    
    def draw(self, buffer: np.ndarray, rotate: bool = False) -> None:
        # animated sprite
        if self.is_animated:
            elapsed = (time.time() - self.start) * 1000

            if elapsed >= self.pixels[self.idx][1]:
                self.idx += 1
                self.idx %= len(self.pixels)
                self.start = time.time()
                
            sprite = self.pixels[self.idx][0]
            
        # static sprite
        else:
            sprite = self.pixels
            
        # rotate
        if rotate:
            match self.dir:
                case Direction.LEFT:
                    pass

                case Direction.RIGHT:
                    sprite = np.fliplr(sprite)
                    
                case Direction.UP:
                    sprite = np.rot90(sprite, -1)
                    
                case Direction.DOWN:
                    sprite = np.rot90(sprite, 1)

        x,y = self.pos
        
        # draw
        self.draw_aa(x,y,sprite, buffer)
        
class GhostState(enum.Enum):
    Waiting     = 0
    Scatter     = 1
    Chase       = 2
    Running     = 3
    Eaten       = 4

class Ghost:
    def __init__(self, home, corner, grid_move_table, grid_cost_table, grid, start_pos=None):
        # positions
        self.home = home
        self.corner = corner
        self.start = start_pos or self.home
        
        # grid
        self.grid = grid
        
        # move tables
        self.grid_mvtbl = grid_move_table
        self.grit_cotbl = grid_cost_table
        
        # states
        self.state = GhostState.Scatter
        self.move_timer = time.time()
        self.state_timer = time.time()
        
        self.duration_wait = 5
        self.duration_scatter = 3
        self.duration_chase = 20
        self.duration_frightened = 5
        
        # sprites
        self.sprite_normal: Sprite = None
        self.sprite_frightened: Sprite = None
        self.sprite_eyes: Sprite = None
        
        self.load_sprites()
        self.reset()

    def reset(self):
        self.frightened = False
        self.state = GhostState.Waiting

        self.state_timer = time.time()
        self.move_timer = time.time()
        self.frightened_timer = time.time()

        self.sprite_normal.set_dir(Direction.UP)
        self.sprite_normal.set_pos(self.start)
        
    def set_speed(self, speed):
        self.sprite_normal.abs_speed = speed
        self.sprite_frightened.abs_speed = speed*0.6
        self.sprite_eyes.abs_speed = speed*5
        
    def pos(self):
        if self.state == GhostState.Eaten:
            return self.sprite_eyes.pos
        elif self.frightened:
            return self.sprite_frightened.pos
        else:
            return self.sprite_normal.pos
        
    def load_sprites(self):
        assets = (Path(__file__).parent / '../../assets').resolve()

        # frightened ghost
        self.sprite_frightened = Sprite(load_gif(assets/'Ghost-Frightened.gif'), self.grid ,animated=True)
        self.duration_frightened = sum(frame[1] for frame in self.sprite_frightened.pixels)/1000

        # just eyes
        self.sprite_eyes = Sprite(load_img(assets/'Ghost-Eyes.png'), self.grid, animated=False)

        return assets

    def available_directions(self, sprite: Sprite, offset=True) -> list[Direction]:
        if offset:
            x, y = sprite.pos + sprite.speed/sprite.abs_speed
        else:
            x, y = sprite.pos

        x = int(x)
        y = int(y)
        
        neighbours = [
            [Direction.RIGHT, x + 1, y],
            [Direction.LEFT, x - 1, y],
            [Direction.DOWN, x, y + 1],
            [Direction.UP, x, y - 1]
        ]
        
        return [direction for direction, x, y in neighbours if (0 <= x <= self.grid.shape[1]) and (0 <= y <= self.grid.shape[0]) and self.grid[y,x]]
    
    def random_direction(self, sprite: Sprite) -> Direction:
        possible_dirs = self.available_directions(sprite)
        
        if len(possible_dirs) == 1:
            sprite.set_new_dir(possible_dirs[0])
            return

        # remove reverse direction
        reverse = sprite.dir.inv()
        if reverse in possible_dirs:
            possible_dirs.remove(reverse)
        
        # random index
        n = len(possible_dirs)
        i = random.randint(0, n-1)

        sprite.set_new_dir(possible_dirs[i])

    def optimal_direction(self, sprite: Sprite, target):
        x,y = sprite.pos
        xt, yt = target

        sprite.set_new_dir(self.grid_mvtbl[sprite.dir][round(y),round(x),round(yt),round(xt)])

    def chase(self, pacman: Sprite):
        self.optimal_direction(self.sprite_normal, pacman.pos)
        
    def move(self, sprite: Sprite):
        sprite.move(time.time() - self.move_timer)
        
    def sync_sprites(self, src: Sprite, dst: Sprite):
        dst.set_pos(src.pos)
        dst.set_dir(src.dir)
            
    def frighten(self, pacman: Sprite):
        if not self.frightened:
            self.sync_sprites(self.sprite_normal, self.sprite_frightened)
            
        if self.state in [GhostState.Scatter, GhostState.Chase]:
            self.state = GhostState.Running

            # get available directions
            possible_dirs = self.available_directions(self.sprite_frightened, offset=False)
            
            # select best direction
            xt,yt = pacman.pos
            xt = round(xt)
            yt = round(yt)
            
            x,y = self.sprite_frightened.pos
            x = round(x)
            y = round(y)
            
            # get distance to pacman for each possible direction
            distance = [d for direction in possible_dirs if (d := self.grit_cotbl[direction][y,x,yt,xt]) != -1]

            # choose direction with largest distance
            new_dir = possible_dirs[np.argmax(distance)]

            # update direction
            self.sprite_frightened.set_new_dir(new_dir)

        self.frightened = True
        self.frightened_timer = time.time()
        self.sprite_frightened.reset_animation()
        
    def get_eaten(self):
        if self.state == GhostState.Eaten:
            return

        self.state = GhostState.Eaten
        self.sync_sprites(self.sprite_frightened, self.sprite_eyes)
        
        xt,yt = self.home
        xt = round(xt)
        yt = round(yt)
        
        x,y = self.sprite_eyes.pos
        x = round(x)
        y = round(y)
        
        # select best direction
        possible_dirs = np.array(
            [
                (dist, direction)
                for direction in self.available_directions(self.sprite_eyes, offset=False) 
                if (dist := self.grit_cotbl[direction][y, x, yt, xt]) != -1
            ]
        )
        
        if len(possible_dirs) > 0:
            new_dir = possible_dirs[np.argmin(possible_dirs[:,0]), 1]
            self.sprite_eyes.set_new_dir(new_dir)
        
    def update(self, *args, **kwargs):
        if self.frightened:
            if (time.time() - self.frightened_timer) > self.duration_frightened:
                # sync sprites
                self.sync_sprites(self.sprite_frightened, self.sprite_normal)
                
                # unfrighten
                self.frightened = False

        match self.state:
            # wait in home position
            case GhostState.Waiting:
                if (time.time() - self.state_timer) > self.duration_wait:
                    self.state_timer = time.time()
                    self.sprite_frightened.speed[:] = 0
                    self.sprite_normal.speed[:] = 0
                    
                    if self.frightened:
                        self.state = GhostState.Running
                        self.random_direction(self.sprite_frightened)
                    else:
                        self.state = GhostState.Scatter
                        self.optimal_direction(self.sprite_normal, self.corner)
                        self.move(self.sprite_normal)

            # move towards corner
            case GhostState.Scatter:
                # if ghost has stopped choose a random direction
                if np.all(self.sprite_normal.speed == 0):
                    self.random_direction(self.sprite_normal)
                else:
                    self.optimal_direction(self.sprite_normal, self.corner)

                # move
                self.move(self.sprite_normal)
                
                if (time.time() - self.state_timer) > self.duration_scatter:
                    self.state = GhostState.Chase
                    self.state_timer = time.time()
            
            # chase pacman
            case GhostState.Chase:
                # if ghost has stopped choose a random direction
                if np.all(self.sprite_normal.speed == 0):
                    self.random_direction(self.sprite_normal)
                else:
                    self.chase(*args, **kwargs)

                # move
                self.move(self.sprite_normal)

                if (time.time() - self.state_timer) > self.duration_chase:
                    self.state = GhostState.Scatter
                    self.state_timer = time.time()
            
            # run from pacman
            case GhostState.Running:
                if self.sprite_frightened.dir == self.sprite_frightened.new_dir:
                    self.random_direction(self.sprite_frightened)

                self.move(self.sprite_frightened)
                
                if not self.frightened:
                    self.state = GhostState.Scatter
                    self.state_timer = time.time()
                
            # move towards home
            case GhostState.Eaten:
                self.move(self.sprite_eyes)
                self.optimal_direction(self.sprite_eyes, self.home)

                distance = np.sum(np.abs(np.array(self.sprite_eyes.pos) - np.array(self.home)))
                
                if distance < 0.1:
                    self.state = GhostState.Waiting
                    self.duration_wait = 5
                    self.state_timer = time.time()
                    
                    self.sync_sprites(self.sprite_eyes, self.sprite_normal)
                    self.sync_sprites(self.sprite_eyes, self.sprite_frightened)

        self.move_timer = time.time()

    def draw(self, buffer):
        if self.state == GhostState.Eaten:
            self.sprite_eyes.draw(buffer)
        elif self.frightened:
            self.sprite_frightened.draw(buffer)
        else:
            self.sprite_normal.draw(buffer)
        
class GhostBlinky(Ghost):
    def load_sprites(self):
        assets = super().load_sprites()

        # base ghost
        pixels = load_img(assets/'Ghost-Blinky.png')
        self.sprite_normal = Sprite(pixels, self.grid, animated=False)

    def chase(self, pacman: Sprite, collectables: np.ndarray):
        n_dots = np.count_nonzero(np.any(collectables, axis=-1))

        if self.max_dots < n_dots:
            self.max_dots = n_dots
            
        eaten = (self.max_dots - n_dots) / self.max_dots
        speed_level = int(eaten * 3)
            
        if self.last_speed_level != speed_level:
            self.sprite_normal.abs_speed *= 1.05
            self.sprite_frightened.abs_speed *= 1.05
            
        self.last_speed_level = speed_level

        self.optimal_direction(self.sprite_normal, pacman.pos)
    
    def reset(self):
        super().reset()

        self.max_dots = 0
        self.last_speed_level = 0
        self.duration_wait = 0
        
class GhostPinky(Ghost):
    def load_sprites(self):
        assets = super().load_sprites()

        # base ghost
        pixels = load_img(assets/'Ghost-Pinky.png')
        self.sprite_normal = Sprite(pixels, self.grid, animated=False)

    def chase(self, pacman: Sprite):
        self.target = self.predict_location(pacman, distance=12)
        self.optimal_direction(self.sprite_normal, self.target)
        
    def predict_location(self, pacman: Sprite, distance = 4) -> tuple[int, int]:
        pos = (int(pacman.pos[0]), int(pacman.pos[1]))
        direction = pacman.dir

        moves = {
            Direction.LEFT:     (-1,  0),
            Direction.RIGHT:    ( 1,  0),
            Direction.UP:       ( 0, -1),
            Direction.DOWN:     ( 0,  1)
        }
        
        # coordinate is in top-left corner => compensate for right and down direction
        if direction in [Direction.RIGHT, Direction.DOWN]:
            distance += 2
        
        for i in range(distance):
            # choose new direction if possible
            next_pos = {d: (pos[0]+m[0], pos[1]+m[1]) for d, m in moves.items()}
            possible_moves = [
                (direction, (x,y))
                for direction, (x, y) in next_pos.items()
                if (0 <= x <= self.grid.shape[1])
                and (0 <= y <= self.grid.shape[0])
                and self.grid[y, x]
            ]
            
            if len(possible_moves) == 1:
                move = possible_moves[0]

            else:
                # remove reverse direction
                reverse = direction.inv()
                possible_moves = [(d, p) for d, p in possible_moves if d != reverse]
            
                # random index
                n = len(possible_moves)
                i = random.randint(0, n-1)
                
                move = possible_moves[i]

            # next postion & direction
            direction, pos = move
            
        return pos

    def reset(self):
        super().reset()

        self.duration_wait = 10
        self.target = None

class GhostInky(Ghost):
    def load_sprites(self):
        assets = super().load_sprites()

        # base ghost
        pixels = load_img(assets/'Ghost-Inky.png')
        self.sprite_normal = Sprite(pixels, self.grid, animated=False)

    def chase(self, pacman: Sprite, blinky_pos):
        moves = {
            Direction.LEFT:     (-1,  0),
            Direction.RIGHT:    ( 1,  0),
            Direction.UP:       ( 0, -1),
            Direction.DOWN:     ( 0,  1)
        }
        blinky_pos = np.array(blinky_pos)
        
        vec = np.array(pacman.pos) + 2*np.array(moves[pacman.dir]) - blinky_pos
        target = 1.5*vec + blinky_pos
        
        # find best match in allowed positions
        allowed = np.array(np.nonzero(self.grid)).T[:, ::-1]
        dist = np.sum(np.abs(allowed-target), axis=1)
        best_match = allowed[dist.argmin()]
        
        self.target = best_match
        self.optimal_direction(self.sprite_normal, self.target)

    def reset(self):
        super().reset()

        self.duration_wait = 15
        self.target = None

class GhostClyde(Ghost):
    def load_sprites(self):
        assets = super().load_sprites()

        # base ghost
        pixels = load_img(assets/'Ghost-Clyde.png')
        self.sprite_normal = Sprite(pixels, self.grid, animated=False)

    def chase(self, pacman: Sprite):
        xt, yt = pacman.pos
        x, y = self.sprite_normal.pos
        
        distance = self.grit_cotbl[self.sprite_normal.dir][round(y), round(x), round(yt), round(xt)]

        if distance > 30:
            self.optimal_direction(self.sprite_normal, pacman.pos)
        else:
            self.optimal_direction(self.sprite_normal, self.corner)

    def reset(self):
        super().reset()

        self.duration_wait = 5


class PacManGameState(enum.Enum):
    Idle            = 0
    LevelBegin      = 1
    Running         = 2
    Death           = 3
    LevelOver       = 4
    GameOver        = 5
    Paused          = 6

class PacManMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)
        
        self.load_assets()
        self.duration_start = 1
        
        self.max_speed = 8

        self.start_mode()
        
    def start_mode(self):
        self.score = 0
        self.lives = 0
        self.running = False
        self.state = PacManGameState.Idle

        # set positions
        self.pacman.set_new_dir(None)
        self.pacman.set_pos((24, 16))
        
        self.blinky.reset()
        self.pinky.reset()
        self.inky.reset()
        self.clyde.reset()
        
        self.load_collectables()
        self.last_time = time.time()
        self.timer = time.time()
        
    def start_stop(self):
        match self.state:
            case PacManGameState.Idle | PacManGameState.GameOver:
                self.game_begin()
                
            case PacManGameState.Running:
                self.state = PacManGameState.Paused
                
            case PacManGameState.Paused:
                self.state = PacManGameState.Running

    def level_begin(self):
        self.state = PacManGameState.LevelBegin
        
        # reset pacman
        self.pacman.set_pos((24, 16))
        self.pacman.set_new_dir(None)
        
        # reset ghosts
        self.blinky.reset()
        self.pinky.reset()
        self.inky.reset()
        self.clyde.reset()
        
        # set speeds
        if self.level > 4:
            ghost_speed = self.max_speed
            pac_speed = self.max_speed
        elif self.level > 1:
            ghost_speed = 0.85*self.max_speed
            pac_speed = 0.9*self.max_speed
        else:
            ghost_speed = 0.75*self.max_speed
            pac_speed = 0.8*self.max_speed
            
        self.pacman.abs_speed = pac_speed
        self.blinky.set_speed(ghost_speed)
        self.pinky.set_speed(ghost_speed)
        self.inky.set_speed(ghost_speed)
        self.clyde.set_speed(ghost_speed)
        
        # load collectables
        self.load_collectables()

        # restart timers
        self.last_time = time.time()
        self.timer = time.time()
    
    def level_over(self):
        self.state = PacManGameState.LevelOver
        self.level += 1
        self.timer = time.time()
            
    def died(self):
        self.lives -= 1
        
        print(f"{self.lives} lives left")
        if self.lives > 0:
            self.state = PacManGameState.LevelBegin
            self.pacman.set_pos((24, 16))
            self.pacman.set_new_dir(None)
            
            self.blinky.reset()
            self.pinky.reset()
            self.inky.reset()
            self.clyde.reset()
            
            self.last_time = time.time()
            self.timer = time.time()
            
        else:
            self.game_over()
    
    def game_begin(self):
        self.running = True
        self.lives = 3
        self.level = 1
        self.level_begin()
    
    def game_over(self):
        print("game-over!")
        print(f"score = {self.score}")
        self.state = PacManGameState.GameOver
        
    def load_assets(self):
        assets = (Path(__file__).parent / '../../assets').resolve()

        # grid
        self.grid = load_img(assets/'PacMan-Grid.png')
        self.pacman_grid = np.any(load_img(assets/'PacMan-Coords.png'), axis=2)
        self.ghost_grid = np.any(load_img(assets/'Ghost-Coords.png'), axis=2)
        self.powerups = np.any(load_img(assets/'PacMan-Powerups.png'), axis=2) 
        self.powerup = load_img(assets/'Power-Up.png')

        # pacman
        pixels = load_gif(assets/'Pacman.gif')
        self.pacman = Sprite(pixels, self.pacman_grid, animated=True)
        self.pacman.abs_speed = 9

        pixels = load_gif(assets/'Pacman-Death.gif')
        self.pacman_death = Sprite(pixels, self.pacman_grid, animated=True)
        self.duration_death = sum(frame[1] for frame in pixels)/1000

        # move table for ghosts
        with np.load(assets/'PacMan-Move-Table.npz', "r", allow_pickle=True) as data:
            self.move_table = {Direction[direction]: data[direction] for direction in data}

        with np.load(assets/'PacMan-Cost-Table.npz', "r", allow_pickle=True) as data:
            self.cost_table = {Direction[direction]: data[direction] for direction in data}

        # ghosts
        self.blinky = GhostBlinky((24, 8), (50-3, 0), self.move_table, self.cost_table, self.ghost_grid, start_pos=(24, 4))
        self.pinky = GhostPinky((27, 8), (50-3, 20-4), self.move_table, self.cost_table, self.ghost_grid)
        self.inky = GhostInky((21, 8), (1, 0), self.move_table, self.cost_table, self.ghost_grid)
        self.clyde = GhostClyde((24, 8), (1, 20-4), self.move_table, self.cost_table, self.ghost_grid)

    def load_collectables(self):
        assets = (Path(__file__).parent / '../../assets').resolve()

        self.collectables = load_img(assets/'PacMan-Collectables.png')
        self.powerups = np.any(load_img(assets/'PacMan-Powerups.png'), axis=2) 
        
    def set_player_dir(self, direction: Direction | None):
        self.pacman.set_new_dir(direction)
        
    def eat(self):
        x,y = self.pacman.pos
        x = round(x)
        y = round(y)
                
        # eat dots
        cy,cx = np.nonzero(np.any(self.collectables[y:y+3,x:x+3], axis=2))
        cx += x
        cy += y
        
        for y, x in zip(cy, cx):
            self.collectables[y,x] = np.array((0,0,0))
            self.score += 20
            
        if not np.any(self.collectables):
            self.level_over()

        # eat powerups
        cy,cx = np.nonzero(self.powerups[y:y+3,x:x+3])
        cx += x
        cy += y
        
        for y, x in zip(cy, cx):
            self.powerups[y,x] = False
            
            # frighten ghosts
            self.blinky.frighten(self.pacman)
            self.pinky.frighten(self.pacman)
            self.inky.frighten(self.pacman)
            self.clyde.frighten(self.pacman)
            
        for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:
            # ghost and pacman touch?
            if (abs(int(ghost.pos()[0]) - x) + abs(int(ghost.pos()[1]) - y)) <= 2:
                # eat ghosts
                if ghost.state != GhostState.Eaten:
                    if ghost.frightened: 
                        ghost.get_eaten()
                        self.score += 500
                        
                    # eat pacman
                    else:
                        self.pacman_death.set_pos(self.pacman.pos)
                        self.pacman_death.set_dir(self.pacman.dir)
                        self.pacman_death.reset_animation()
                        self.state = PacManGameState.Death
                        self.timer = time.time()

    def draw_powerups(self):
        y,x = np.nonzero(self.powerups)
        
        for y, x in zip(y,x):
            self.framebuffer[y-1:y+2, x-1:x+2] = self.powerup

    def render(self):
        # elapsed time
        elapsed = time.time() - self.last_time
        self.last_time = time.time()
        
        # game state machine
        match self.state:
            case PacManGameState.LevelBegin:
                if (time.time() - self.timer) > self.duration_start:
                    self.state = PacManGameState.Running
            
            case PacManGameState.Running:
                self.blinky.update(self.pacman, self.collectables)
                self.pinky.update(self.pacman)
                self.inky.update(self.pacman, self.blinky.pos())
                self.clyde.update(self.pacman)

                self.pacman.move(elapsed)
            
                self.eat()
                
            case PacManGameState.Death:
                if (time.time() - self.timer) > self.duration_death:
                    self.died()
            
            case PacManGameState.LevelOver:
                if (time.time() - self.timer) > self.duration_start:
                    self.level_begin()
            
            case PacManGameState.GameOver:
                pass

            case PacManGameState.Paused:
                self.blinky.move_timer = time.time()
                self.pinky.move_timer = time.time()
                self.inky.move_timer = time.time()
                self.clyde.move_timer = time.time()

        # draw objects
        match self.state:
            case PacManGameState.Death:
                self.framebuffer = self.grid.copy()
                self.framebuffer += self.collectables
                self.draw_powerups()
                self.blinky.draw(self.framebuffer)
                self.pinky.draw(self.framebuffer)
                self.inky.draw(self.framebuffer)
                self.clyde.draw(self.framebuffer)
                self.pacman_death.draw(self.framebuffer, rotate=True)
                
            case PacManGameState.Idle:
                self.framebuffer = self.grid.copy()
                self.framebuffer += self.collectables
                self.draw_powerups()
                self.blinky.draw(self.framebuffer)
                self.pinky.draw(self.framebuffer)
                self.inky.draw(self.framebuffer)
                self.clyde.draw(self.framebuffer)
                
            case PacManGameState.GameOver:
                self.framebuffer.fill(0)
                self.draw_text("You Died", (0,2), fg=(215, 0, 0), hcenter=True)
                self.draw_text(self.score, (0,11), fg=(215, 0, 0), hcenter=True)

            case _:
                self.framebuffer = self.grid.copy()
                self.framebuffer += self.collectables
                self.draw_powerups()
                self.blinky.draw(self.framebuffer)
                self.pinky.draw(self.framebuffer)
                self.inky.draw(self.framebuffer)
                self.clyde.draw(self.framebuffer)
                self.pacman.draw(self.framebuffer, rotate=True)

        return self.framebuffer