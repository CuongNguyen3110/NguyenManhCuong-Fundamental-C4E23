size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Cuong and these are my sheep sizes: ", size)

n = int(input("Month: "))
for i in range(n):
    print("Month", i+1)
    for j in range(len(size)):
        size[j] += 50
    print("One month has passed, now here is my flock: ", size)
    print("Now my biggest sheep has size", max(size), "lets shear it")
    size[size.index(max(size))] = 8
    print("After shearing, here is my flock", size)