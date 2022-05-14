# import math
# def calAngle(a, b):
#     x = a[0] * b[0] + a[1] * b[1]
#     y = math.sqrt(a[0] ** 2 + a[1] ** 2) * math.sqrt(b[0] ** 2 + b[1] ** 2)
#     rad =  math.acos(x / y)
#     return math.degrees(rad)

# def Input():
#     points = []
#     for i in range(4):
#         temp = [int(x) for x in input().split()]
#         points.append(temp)
#     return points

# def Check(points):
#     vectors = []
#     angles = []

#     # Compute Vector
#     for i in range(3):
#         temp = [points[i][0] - points[-1][0], points[i][1] - points[-1][1]]
#         vectors.append(temp)
#     # Compute Angle
#     for i in range(3):
#         if i == 2:
#             angle = calAngle(vectors[i], vectors[0])
#         else:
#             angle = calAngle(vectors[i], vectors[i + 1])
#         angles.append(angle)
#     sumAngle = round(sum(angles))
#     print(sumAngle)
#     if sumAngle == 360:
#         return True
#     else:
#         return False

# points = Input()
# if Check(points):
#     print("Inside")
# else:
#     print("Not Inside")


a = [-2,2]
b = [-1,-2]
print(a[0] * b[1] - a[1] * b[0])