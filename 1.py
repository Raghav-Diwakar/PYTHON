class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
    # initialize the matrix with zeros
        matrix = [[0 for j in range(n)] for i in range(n)]
        
        # define the boundary of the matrix
        top, bottom, left, right = 0, n-1, 0, n-1
        
        # define the current direction
        direction = 0 # 0: right, 1: down, 2: left, 3: up
        
        # fill the matrix with numbers in a spiral pattern
        number = 1
        while top <= bottom and left <= right:
            if direction == 0: # move right
                for i in range(left, right+1):
                    matrix[top][i] = number
                    number += 1
                top += 1
            elif direction == 1: # move down
                for i in range(top, bottom+1):
                    matrix[i][right] = number
                    number += 1
                right -= 1
            elif direction == 2: # move left
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = number
                    number += 1
                bottom -= 1
            elif direction == 3: # move up
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = number
                    number += 1
                left += 1
            
            # change the direction
            direction = (direction + 1) % 4
        
        return matrix
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
    # initialize the matrix with zeros
        matrix = [[0 for j in range(n)] for i in range(n)]
        
        # define the boundary of the matrix
        top, bottom, left, right = 0, n-1, 0, n-1
        
        # define the current direction
        direction = 0 # 0: right, 1: down, 2: left, 3: up
        
        # fill the matrix with numbers in a spiral pattern
        number = 1
        while top <= bottom and left <= right:
            if direction == 0: # move right
                for i in range(left, right+1):
                    matrix[top][i] = number
                    number += 1
                top += 1
            elif direction == 1: # move down
                for i in range(top, bottom+1):
                    matrix[i][right] = number
                    number += 1
                right -= 1
            elif direction == 2: # move left
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = number
                    number += 1
                bottom -= 1
            elif direction == 3: # move up
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = number
                    number += 1
                left += 1
            
            # change the direction
            direction = (direction + 1) % 4
        
        return matrix
