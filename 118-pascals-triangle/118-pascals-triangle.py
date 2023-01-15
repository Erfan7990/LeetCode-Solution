from math import factorial
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        for i in range(numRows):
            row = []
            for j in range (i+1):
                row.append(factorial(i)//(factorial(i-j)*factorial(j)))
            arr.append(row)
        return arr
                    