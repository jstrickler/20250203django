import sys
# import pkg.pkg.module
import alpha.mathlib.geometry as geometry  # find geometry.py and run the code in it

circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

# module search order:
# 1. current folder
# 2. folders in PYTHONPATH    "FOLDER1;FOLDER2;..." Windows  "f1:f2:f3:"  Non-windows
# 3. installation_folder + 'lib'  (and maybe a few other places)

print(f"{sys.prefix = }\n")

for path in sys.path:
    print(path)

