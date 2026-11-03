
import math

NAME = "illya vorobey"
GROUP = "it-31"

LENGTH = 4.3
WIDTH = 3.5
HEIGHT = 2.7

DOOR_WIDTH = 0.9
DOOR_HEIGHT = 2.0

WINDOW_WIDTH = 1.4
WINDOW_HEIGHT = 1.5

TILE_LENGTH = 0.3
TILE_WIDTH = 0.3
TILE_PRICE = 42.30

print(f"{NAME}, {GROUP}")

floor_area = LENGTH * WIDTH

wall_area = (
    2 * (LENGTH + WIDTH) * HEIGHT
    - DOOR_WIDTH * DOOR_HEIGHT
    - WINDOW_WIDTH * WINDOW_HEIGHT
)

floor_diag = math.hypot(LENGTH, WIDTH)

room_diag = math.dist(
    (0, 0, 0),
    (LENGTH, WIDTH, HEIGHT)
)
tile_area = TILE_LENGTH * TILE_WIDTH
tiles_exact = floor_area / tile_area

tiles_round = round(tiles_exact)
tiles_floor = math.floor(tiles_exact)
tiles_ceil = math.ceil(tiles_exact)

tiles_to_buy = math.ceil(tiles_exact * 1.10)

paint_liters = wall_area / 10 * 2
paint_cans = math.ceil(paint_liters / 2.5)

# Вартість плитки
cost_mul = tiles_to_buy * TILE_PRICE

cost_sum = 0.0
for i in range(tiles_to_buy):
    cost_sum += TILE_PRICE

difference = abs(cost_mul - cost_sum)

# Результати
print(f"room:          {LENGTH} x {WIDTH} x {HEIGHT} m")
print(f"floor area:    {floor_area:.2f} m2")
print(f"wall area:     {wall_area:.2f} m2")
print(f"floor diag:    {floor_diag:.2f} m")
print(f"room diag:     {room_diag:.2f} m")

print()
print(f"tiles exact:   {tiles_exact:.2f}")
print(f"  round:       {tiles_round}")
print(f"  floor:       {tiles_floor}")
print(f"  ceil:        {tiles_ceil}")
print(f"tiles to buy:  {tiles_to_buy} (+10% spare)")

print(
    f"paint:         {paint_liters:.2f} l "
    f"-> {paint_cans} cans of 2.5 l"
)

print()
print(f"tiles cost:    {cost_mul:.2f} UAH")
print(f"sum == mul:    {cost_sum == cost_mul}")
print(f"isclose:       {math.isclose(cost_sum, cost_mul)}")
print(f"difference:    {difference}")
