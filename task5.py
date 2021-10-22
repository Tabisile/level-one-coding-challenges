def triangle(x):
    if x > 0:
       for i in range(1,x+1):
           for j in range(1,i+1):
               print('#', end= '')
           print()
    elif x < 0:
       for i in range(x,0):
           for j in range(i,0):
               print('#', end = '')
           print()
