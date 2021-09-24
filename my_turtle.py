import turtle

# turtle.shape('turtle')
# turtle.speed(500)
# turtle.penup()
# turtle.forward(20)
# turtle.left(90)
# turtle.pendown()
#
#
# f = 5
# l = 2
# t = 0
# while t <= 180:
#     turtle.forward(f)
#     turtle.left(l)
#     t += 1
# круг

# turtle.shape('turtle')
# turtle.speed(20)
#
#
# f = 20
# for k in range(10):
#     for i in range(4):
#         i += 1
#         turtle.forward(f)
#         turtle.left(90)
#
#     k += 1
#     turtle.penup()
#     turtle.left(45)
#     turtle.back(10)
#     turtle.right(45)
#     turtle.pendown()
#     f += 15
# 10 квадратов

# turtle.shape('turtle')
# turtle.speed(20)
#
# n = 12
# for i in range(n):
#     turtle.right(30)
#     turtle.forward(100)
#     turtle.stamp()
#     turtle.right(180)
#     turtle.forward(100)
#     turtle.right(180)
# паук

#turtle.shape('turtle')
#turtle.speed(20)
l = 60
f = 5

for i in range(200):
    i += 1
    turtle.left(l)
    turtle.forward(f)
    l += (2*l)/3.14
    #f += 1





