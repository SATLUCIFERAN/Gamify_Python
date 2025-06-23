
# game.py
import tkinter as tk
from snake import Snake
from food import Food
from board import Board

class Game:
    def __init__(self, grid_w=20, grid_h=20, cell_size=20, speed=150):
        """
        grid_w, grid_h: number of cells
        cell_size: pixels per cell
        speed: ms between each move
        """
        self.master = tk.Tk()
        self.master.title("Snake")
        self.board = Board(self.master, grid_w, grid_h, cell_size)
        
        # 1) Model components
        start = (grid_w//2, grid_h//2)
        self.snake = Snake(start, start_length=3, direction=(1,0))
        self.food  = Food(grid_w, grid_h, self.snake.segments)
        self.score = 0
        self.speed = speed

        # 2) Bind keys
        self.master.bind("<Up>",    lambda e: self.snake.change_direction((0,-1)))
        self.master.bind("<Down>",  lambda e: self.snake.change_direction((0,1)))
        self.master.bind("<Left>",  lambda e: self.snake.change_direction((-1,0)))
        self.master.bind("<Right>", lambda e: self.snake.change_direction((1,0)))        
        self.master.bind("r", lambda e: self.restart())
        self.master.bind("R", lambda e: self.restart())

        # 3) Start the game loop
        self.loop()
        self.master.mainloop()

    def loop(self):
        """One tick of the game: move, check, redraw, and reschedule."""
        # a) Move the snake
        self.snake.move()

        # b) Check for wall collision
        head_x, head_y = self.snake.segments[0]
        if not (0 <= head_x < self.board.grid_width and
                0 <= head_y < self.board.grid_height):
            return self.game_over()

        # c) Check for self‐collision
        if self.snake.collides_with_self():
            return self.game_over()

        # d) Check for eating food
        if self.snake.segments[0] == self.food.position:
            self.snake.grow()
            self.score += 10
            self.board.update_score(self.score)
            self.food.respawn(self.snake.segments)

        # e) Redraw
        self.board.clear()
        self.board.draw_snake(self.snake.segments)
        self.board.draw_food(self.food.position)

        # f) Schedule next tick
        self.master.after(self.speed, self.loop)

    def game_over(self):
        """Stop the loop and display 'Game Over'."""
        self.board.canvas.create_text(
            self.board.grid_width*self.board.cell_size//2,
            self.board.grid_height*self.board.cell_size//2,
            text="GAME OVER\nPress R to restart",
            fill="red", font=("Arial", 14)
        )


    def restart(self):
        '''
        Reset the entire game state and start over.
        '''
        # 1) Clear canvas completely (including GAME OVER text)
        self.board.canvas.delete("all")

        # 2) Re‐create snake, food, score
        start = (self.board.grid_width//2, self.board.grid_height//2)
        self.snake = Snake(start, start_length=3, direction=(1,0))
        self.food  = Food(self.board.grid_width, self.board.grid_height, self.snake.segments)
        self.score = 0
        self.board.update_score(self.score)

        # 3) Redraw initial state
        self.board.draw_snake(self.snake.segments)
        self.board.draw_food(self.food.position)

        # 4) Restart the main loop
        self.master.after(self.speed, self.loop)


if __name__ == "__main__":
    Game()
