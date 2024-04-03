import numpy as np
#Tehtävä 1A
A = np.array([[-1, 2],
              [3, 1]])

B = np.array([[0, 1, 3],
              [2, -3, 5]])

C = np.dot(A, B)
print(C)


#tehtävä 1B
A = np.array([[1, 3, 5],
              [0, -2, 1],
              [2, -1, 4]])
B = np.array([1, -3, -1])
C = np.dot(A, B)
print(f"{C}tehtävä 1b vastaus")


#tehtävä 1C
A = np.array([[2, 0, 1],
              [1, -3, 4],
              [0, 1, 5]])
B = np.array([3, -5, 7])

C = np.dot(A, B)


print(f"{C}tehtävä 1C vastaus")

#tehtävä 1d
A = np.array([[1, -4, 2],
              [3, 0, -2],
              [2, 1, 0]])
B = np.array([[5, 1, -1],
              [-2, 1, 3],
              [0, 3, 4]])
C = np.dot(A, B)

print(f"{C}tehtävä 1D vastaus")

