import turtle
import math
import time

class TulipBouquet:
    """A class to create an animated 3D tulip bouquet with ribbon over ~30 seconds."""
    
    def __init__(self):
        self.screen = turtle.Screen()
        
        # Auto fullscreen setup
        self.root = self.screen.getcanvas().winfo_toplevel()
        self.root.attributes('-fullscreen', True)
        
        self.screen.bgcolor("#0a0a0a")
        self.screen.title("30-Second Animated Tulip Bouquet")
        
        # Slower tracer for smoother animation
        self.screen.tracer(1, 15) 
        
        self.t = turtle.Turtle()
        self.t.speed(0) # Fastest movement speed
        self.t.hideturtle()
        
        self.shades = [
            ("#C71585", "#FF69B4", "#FFB6C1"),
            ("#8B008B", "#FF1493", "#FF85C1"),
            ("#DB7093", "#FFC0CB", "#FFE4E1"),
            ("#D946A6", "#FF5EC7", "#FFA8E0")
        ]
        
        self.bouquet_data = [
            (0, 200, 22, 2, 90),
            (-80, 160, 24, 1, 105),
            (80, 160, 24, 0, 75),
            (-130, 90, 27, 3, 115),
            (130, 90, 27, 2, 65),
            (-50, 70, 30, 1, 95),
            (50, 70, 30, 1, 85),
            (-100, 30, 26, 0, 100),
            (100, 30, 26, 2, 80),
            (0, 20, 34, 3, 90)
        ]
        
        # Bind Escape key to exit fullscreen
        self.screen.onkey(self.exit_fullscreen, "Escape")
        self.screen.listen()
    
    def exit_fullscreen(self):
        """Exit fullscreen mode when Escape is pressed."""
        self.root.attributes('-fullscreen', False)
    
    def draw_petal(self, size, colors):
        shadow, base, highlight = colors
        self.t.fillcolor(base)
        self.t.pencolor(shadow)
        self.t.begin_fill()
        self.t.circle(size, 90)
        self.t.left(90)
        self.t.circle(size, 90)
        self.t.end_fill()
        
        self.t.penup()
        self.t.left(90)
        self.t.circle(size, 15)
        self.t.pendown()
        self.t.pencolor(highlight)
        self.t.pensize(2)
        self.t.circle(size, 50)
        self.t.penup()

    def draw_tulip(self, x, y, size, colors, angle):
        self.t.penup()
        self.t.goto(x, y)
        self.t.setheading(angle)
        self.t.pendown()
        
        for i in range(3):
            self.t.setheading(angle - 30 + (i * 30))
            self.draw_petal(size, colors)
            self.t.penup()
            self.t.goto(x, y)
            self.t.pendown()
        
        self.t.setheading(angle + 10)
        self.draw_petal(size * 0.95, colors)
        
        self.t.penup()
        self.t.goto(x, y - size * 0.3)
        self.t.dot(size * 0.3, "#FFD700")

    def draw_stem(self, start_x, start_y, end_x, end_y):
        self.t.penup()
        self.t.goto(start_x, start_y)
        self.t.pendown()
        self.t.pensize(8)
        self.t.pencolor("#1B4D1B")
        self.t.goto(end_x, end_y)
        
        self.t.penup()
        self.t.goto(start_x + 2, start_y)
        self.t.pendown()
        self.t.pensize(3)
        self.t.pencolor("#45a045")
        self.t.goto(end_x + 2, end_y)

    def draw_leaf(self, x, y, angle, size):
        self.t.penup()
        self.t.goto(x, y)
        self.t.setheading(angle)
        self.t.pendown()
        self.t.fillcolor("#228B22")
        self.t.pencolor("#004400")
        self.t.pensize(2)
        self.t.begin_fill()
        self.t.circle(size, 90)
        self.t.left(90)
        self.t.circle(size, 90)
        self.t.end_fill()
        
        self.t.penup()
        self.t.goto(x, y)
        self.t.setheading(angle + 45)
        self.t.pendown()
        self.t.pencolor("#90EE90")
        self.t.pensize(1)
        self.t.forward(size * 1.2)

    def draw_ribbon_wrap(self, x, y, width):
        self.t.penup()
        self.t.goto(x, y)
        self.t.setheading(0)
        self.t.pensize(30)
        self.t.pencolor("#FFB6D9")
        self.t.pendown()
        self.t.forward(width)
        
        self.t.penup()
        self.t.goto(x, y + 8)
        self.t.pendown()
        self.t.pensize(8)
        self.t.pencolor("#FFDDF4")
        self.t.forward(width)

    def draw_bow(self, x, y):
        ribbon_pink = "#FFB6D9"
        ribbon_shadow = "#FF85C1"
        self.t.pensize(1)
        self.t.fillcolor(ribbon_pink)
        self.t.pencolor(ribbon_shadow)
        
        for angle, turn in [(-65, 90), (-115, -90)]:
            self.t.penup()
            self.t.goto(x, y)
            self.t.setheading(angle)
            self.t.pendown()
            self.t.begin_fill()
            self.t.forward(90)
            self.t.setheading(self.t.heading() + turn)
            self.t.forward(28)
            self.t.goto(x, y)
            self.t.end_fill()
        
        for angle in [35, 145]:
            self.t.penup()
            self.t.goto(x, y)
            self.t.setheading(angle)
            self.t.pendown()
            self.t.begin_fill()
            self.t.circle(45, 210)
            self.t.goto(x, y)
            self.t.end_fill()
        
        self.t.penup()
        self.t.goto(x - 20, y - 14)
        self.t.setheading(0)
        self.t.fillcolor(ribbon_pink)
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(40)
            self.t.circle(14, 90)
            self.t.forward(18)
            self.t.circle(14, 90)
        self.t.end_fill()

    def draw_sparkles(self):
        sparkle_positions = [(-200, 150), (200, 150), (-150, 250), (150, 250), (0, 350)]
        for x, y in sparkle_positions:
            self.t.penup()
            self.t.goto(x, y)
            self.t.pencolor("#FFD700")
            for angle in range(0, 360, 72):
                self.t.setheading(angle)
                self.t.pendown()
                self.t.forward(8)
                self.t.penup()
                self.t.goto(x, y)

    def draw(self):
        # 1. Stems (~5 seconds total)
        for x, y, size, col_idx, angle in self.bouquet_data:
            self.draw_stem(0, -280, x, y)
            time.sleep(0.4)  # Increased from 0.05 to 0.4
        
        # 2. Leaves (~4 seconds total)
        for x, y, size, col_idx, angle in self.bouquet_data:
            if abs(x) > 40:
                leaf_x = x * 0.5
                leaf_y = y * 0.5 - 120
                self.draw_leaf(leaf_x, leaf_y, angle + 35, 60)
                time.sleep(0.5)  # Increased from 0.08 to 0.5

        # 3. Ribbon & Bow (~2 seconds)
        self.draw_ribbon_wrap(-65, -240, 130)
        time.sleep(0.5)
        self.draw_bow(0, -240)
        time.sleep(1.0)

        # 4. Tulip heads (~15 seconds total)
        for x, y, size, col_idx, angle in self.bouquet_data:
            self.draw_tulip(x, y, size, self.shades[col_idx], angle)
            time.sleep(1.3)  # Increased from 0.3 to 1.3

        # 5. Final Details (~3 seconds)
        time.sleep(0.5)
        self.draw_sparkles()
        time.sleep(1.0)
        
        self.t.penup()
        self.t.goto(0, 360)
        self.t.pencolor("#FFB6D9")
        self.t.write("Hand-Tied Pink Bouquet", align="center", font=("Georgia", 28, "italic"))
        
        time.sleep(1.0)
        self.screen.update()

    def run(self):
        self.draw()
        self.screen.mainloop()

if __name__ == "__main__":
    bouquet = TulipBouquet()
    bouquet.run()
