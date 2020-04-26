# Use override to rederince special methods

# 특정 object에 [] 사용 시, 내부적으로 __getitem__ 메소드 실행
class Vector(object):
    '''representign a vector in a multidimentsional space'''
    def __init__(self,d, li = None):
        '''Create d-dimensional vector of zeros'''
        self._coords = [0]*d
        if li and d == len(li) :
            for j in range(d):
                self.__setitem__(j,li[j])


    def __getitem__(self,j):
        # Overriding .__getitem__ method
        # a[k] -> a.__getitem__(k)
        '''return jth coordinate of vector'''
        return self._coords[j]

    def __setitem__(self,j,val):
        # Overriding .__setitem__ method
        # a[k] = v -> a.__setitem__(k,v)
        self._coords[j] = val

    def __len__(self):
        return len(self._coords)

    def __add__(self, other):
        ''' Overriding the predefined "add class ( + )" '''
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._cooords

    def __ne__(self, other):
        return not self == other # __eq__ 에서 처리

    def __str__(self):
        '''produce string representation of vector'''
        return '<' + str(self._coords)[1:-1] + '>'


def main():
    v3_1 = Vector(3, [1,2,3])
    v3_2 = Vector(3, [3,2,1])







main()
