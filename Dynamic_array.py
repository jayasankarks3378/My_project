import ctypes

class Array:

    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size = self.size
        self.A = self.__make_array(self.size)

    def __make_array(self,capacity):
        # creates z C type array(static,referential) with size capacity
        return (capacity*ctypes.py_object)()

    def __len__(self):
        return self.n

    def __resize(self,new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity

        # copy the contents of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        
        # re-assign A
        self.A = B

    def append(self,item):
        if self.size == self.n :
            # resize
            self.__resize(self.size*2)

        # append
        self.A[self.n] = item
        self.n = self.n + 1

    def __getitem__(self,index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - index out of bounds'
        
    def pop(self):
        if self.n == 0:
            return 'Empty list'
        
        self.n -= 1
        return self.A[self.n]
    
    def clear(self):
        self.size = 1
        self.n = 0

    def find(self,item):
        for i in range (self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - Not In List'
    
    def insert(self,index,item):
        if self.size == self.n :
            self.__resize(self.size*2)

        for i in range(self.n,index,-1):
            self.A[i] = self.A[i - 1]
        self.A[i] = item
        self.n += 1

    def __delitem__(self,index):
        if 0 < index < self.n :
            for i in range (index,self.n-1):
                self.A[index] = self.A[index+1]

            self.n -= 1

    def remove(self,item):
        index = self.find(item)

        if type(index) == int:
            self.__delitem__(index)
        else:
            return index

    def __str__(self):
        result = ''
        for i in range (self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
    