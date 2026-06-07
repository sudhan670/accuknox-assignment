from rectangle import Rectangle

rectangle = Rectangle(10, 5)
ans = 1
for item in rectangle:
    ans *= item
print("Rectangle Item", ans)