import tkinter as tk
import time

# Create window
window = tk.Tk()
window.title("Love Messages for Valentine Day")
window.geometry("400x400")

# Create canvas
canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack()

# Draw person
def draw_person():
    # Head
    canvas.create_oval(150, 50, 200, 100, fill="pink")
    # Body
    canvas.create_line(175, 100, 175, 200, width=2)
    # Arms
    canvas.create_line(175, 130, 125, 170, width=2)
    canvas.create_line(175, 130, 225, 170, width=2)
    # Legs
    canvas.create_line(175, 200, 150, 300, width=2)
    canvas.create_line(175, 200, 200, 300, width=2)

# Draw heart
def draw_heart(x, y):
    heart = canvas.create_polygon(
        x, y,
        x-10, y-20,
        x-20, y,
        x, y+20,
        x+20, y,
        x+10, y-20,
        fill="red",
        outline="red"
    )
    return heart

# Move heart
def move_heart(heart):
    for _ in range(50):
        canvas.move(heart, 5, -5)
        window.update()
        time.sleep(0.05)

# Main function
def main():
    draw_person()
    heart = draw_heart(175, 170)  
    
# Heart starts from the left hand of the person
    move_heart(heart)

# Button triggers the launch of the heart animation
button = tk.Button(window, text="ik hou van je", command=main)
button.pack()

# Enter main loop
window.mainloop()