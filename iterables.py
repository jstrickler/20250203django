colors = ['purple', 'green', 'orange']
for color in colors:
    print(color)
print('-' * 60)

for color in reversed(colors):
    print(color)
print('-' * 60)

rcolors = reversed(colors)
print(f"{rcolors = }")
for color in rcolors:
    print(color)
print('-' * 60)
for color in rcolors:
    print(color)
print('-' * 60)
