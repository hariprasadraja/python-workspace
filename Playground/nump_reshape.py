import numpy 


numpyArray = numpy.zeros((3, 4))

print("2-dimentional array", numpyArray.shape)

print("reshaping 2-d array")

reshapedArray=  numpy.reshape(numpyArray, (3*4,-1))

print("reshaped array", reshapedArray.shape)

numpyArray = numpy.zeros((3, 4, 5))

print("3-dimentional array", numpyArray.shape)


reshapedArray = numpy.reshape(numpyArray, (3 * 4, 5))
print("reshaped array", reshapedArray.shape)

print("transposed array", reshapedArray.transpose().shape)
