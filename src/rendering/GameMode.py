from rendering.RenderMode import RenderMode
import numpy as np
import enum
from collections import deque
import time
import random
from typing import Literal

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

class PongMode(RenderMode):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.ball_size = 2
        self.ball_color = np.array((255,255,255))

        self.player_length = 4
        self.player_speed = 15.0
        self.player_color = np.array((255,255,255))

        self.start_time = time.time()

        self.winning_score = 10

        self.reset()

    def reset(self):
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
        print(f"round {self.round}, player-1: {self.player1_score}, player-2: {self.player2_score}")

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
        if self.ball is not None:    
            self.draw_ball()

        self.draw_player(0, self.player1)
        self.draw_player(-1, self.player2)

        return self.framebuffer