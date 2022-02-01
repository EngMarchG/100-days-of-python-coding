import colorgram as cg
import turtle as t

tim = t.Turtle()
colors = cg.extract('images.jpg', 84)

print(colors)

# for _ in len(colors):
#     print(colors[_])