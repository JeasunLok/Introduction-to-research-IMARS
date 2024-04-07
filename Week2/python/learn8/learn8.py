import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(1, 5)
print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(a**2)
print(np.sin(a)*10)
print(a>20)

c = np.linspace(10, 20, 50)
print(c)
c = np.reshape(c, (2, 5, -1))
print(c)
print(c[1][1][1])
print(c[1, 1, 1])
print(c[1][:][1])
print(c[1, :, 1])
print(c[1, 2:, 1])

d = np.floor(np.random.random((2, 2)) * 10)
e = np.floor(np.random.random((2, 2)) * 10)
dev = np.vstack((d, e))
deh = np.hstack((d, e))
print(dev)
print(deh)

array = a
array = np.reshape(array, (2, 2))
print(array)
print(array.transpose())
print(np.linalg.inv(array))
print(np.dot(array, np.linalg.inv(array)))
print(np.round(np.dot(array, np.linalg.inv(array)), 3))
print(np.mat(array))
m = np.mat(array)
print(m.getI()) # getI是matrix类型才有
print(m.getI() * m)

print(np.zeros(5))
print(np.zeros([2, 5, 5]))
print(np.ones(5))
print(np.zeros([2, 4, 5]))
print(np.eye(5))
print(np.diag(array))

x = np.random.random((5, 5))
y = np.random.random((5, 5))
print(x)
print(y)
print(np.linalg.solve(x, y))
print(np.dot(np.linalg.inv(x), y))

print(np.linalg.det(x))

A = np.array([[1, 2, 1], [2, -1, 3], [3, 1, 2]])
B = np.array([7, 7, 8])
X = np.linalg.solve(A, B)
print(X)

np.savetxt(r"./learn8/matrix.txt", A+100)
np.save(r"./learn8/matrix.npy", A+200)
input1 = np.loadtxt(r"./learn8/matrix.txt")
input2 = np.load(r"./learn8/matrix.npy")
print(input1)
print(input2)