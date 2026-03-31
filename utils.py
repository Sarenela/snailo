import random
# Ustawienia ekranu
WIDTH = 900
HEIGHT = 1000
FPS = 30 #liczba kratek na sekundę

#box settings
BOX_WIDTH =130
BOX_HEIGHT =130
BOX_SEP =20

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PISTACHIO = (147,197,114)
LIGHT_PISTACHIO = (210, 240, 180)
PINK = (222,165,164)

# metryki
speed = 0
score = 0


#util methods:
def draw6():
    numbers = [0, 1, 2, 3, 4, 5]
    drawn_numbers = set(random.sample(numbers, k=4))
    number1 = random.choice(numbers)
    number2 = random.choice(numbers)
    drawn_numbers.add(number1)
    drawn_numbers.add(number2)
    return drawn_numbers