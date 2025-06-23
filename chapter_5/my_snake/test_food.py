
from food import Food

def test_food_never_on_snake():
    snake_segments = [(0,0), (1,0), (2,0)]

    f = Food(grid_width=5, grid_height=5, snake_segments=snake_segments)
    
    assert f.position not in snake_segments

def test_respawn_moves_food():
    snake = [(0,0), (1,0), (2,0)]
    f = Food(5,5, snake)
    old_pos = f.position
    # pretend snake grows to cover new head
    snake.append(old_pos)
    f.respawn(snake)
    assert f.position not in snake  # new food is in a fresh spot



