import numpy

if __name__ == "__main__":
    def arrays(arr):
        # complete this function
        return numpy.array(arr,float)[::-1]
        # use numpy.array


    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)