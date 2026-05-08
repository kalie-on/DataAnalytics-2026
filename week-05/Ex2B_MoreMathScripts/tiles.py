
import math

length = float(input("Enter room length in feet: "))
width = float(input("Enter room width in feet: "))

area = length * width
tiles_needed = area * 1.10

boxes_needed = math.ceil(tiles_needed / 12)

print(f"Room area: {area:.2f} square feet")
print(f"Tiles needed with 10% extra: {tiles_needed:.2f}")
print(f"Boxes to buy: {boxes_needed}")