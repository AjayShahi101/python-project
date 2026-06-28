import numpy as np
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg



# listarray = np.array([[1,2,3],[4,5,6],[7,8,9]])ff

# print(listarray)
# print("dtype :", listarray.dtype)
# print(listarray.size)
#print(listarray.shape)

# zeros=np.zeros((1,3))
# print(zeros)
# print(zeros.dtype)
# print(zeros.size)
# print(zeros.shape)

# rng=np.arange(15)
# print(rng)

# arr=np.arange(99)
# print(arr)

# arr=arr.reshape(3,33)
# print(arr)

# arr=arr.ravel()
# print(arr)




# x=[[1,2,3]]
# arr=np.array([0,4,55,2])

# print(arr)
# print(arr.sum(axis=0))
# print(arr.sum(axis=1))
# print(arr.T)

# for item in arr.flat:
#     print(item)



# one=np.array([1,3,4,634,2])

# print(one.argmax())
# print(one.argmin())
# print(one.argsort())

# print(arr.argmin(axis=0))
# print(arr.argmax(axis=1))
# print(arr.argsort())
# print(arr)


# arr2=np.array([[4,5,6],[7,8,9],[1,2,3]])
# print(arr2)
# print(arr-arr2)

# print(np.where(arr>5))

# arr=.array([0,4,55,2])
# list=[0,4,55,2]
# print(sys.getsizeof(1)*len(list))
# print(arr.itemsize*arr.size)

# arr_rg=gen(pcg(seed=200))
# arr=arr_rg.integers(low=10, high=100, size=(5,5))

# arr=np.random.randint(1,101,5)
# print(arr)

# arr2=np.random.rand()
# print(arr2)

# arr3=np.random.uniform(1,10,2)
# print(arr3)

# arr4=np.array([[1,2,3],[4,5,6]])
# np.random.shuffle(arr4)
# print(arr4)

# arr5=np.random.randn()
# print(arr5)

arr=np.array([1,2,3,4,5,6])
print(np.random.choice(arr))