
# test_snake.py
from snake import Snake

# 1) Initialization
s = Snake(start_pos=(5,5), start_length=3, direction=(1,0))
assert s.segments == [(5,5), (4,5), (3,5)]

# 2) Move without growing
s.move()
assert s.segments == [(6,5), (5,5), (4,5)]

# 3) Grow then move
s.grow()
s.move()
assert len(s.segments) == 4

# 4) Prevent reverse direction
s.change_direction((-1,0))
assert s.direction == (1,0)

# 5) Self-collision
s = Snake((2,2), 4, (0,1))
s.segments = [(2,2),(2,3),(3,3),(3,2)]
s.direction = (0,1)
s.move()
assert s.collides_with_self()







