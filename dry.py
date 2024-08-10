# DRY -> Don't Repeat Yourself

def say_hi(name):
    print(f"Hey {name} I love you")

names = ["Veronica", "Richard", "Lisboa", "Gary"]

for name in names:
    say_hi(name)
