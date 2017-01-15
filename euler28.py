def sumSpiralDiagonals():
    n = 1001  # n is the max side length of the spiral
    cornerSum = 1
    dimension = 3
    corner = 1
    while (dimension <= n):
        for count in range(1, 5):
            corner = corner + dimension - 1
            cornerSum = cornerSum + corner
            
        dimension = dimension + 2
        
    return cornerSum
  
def main():
  print("The sum of a 1000x1000 spiral's diagonals is:", sumSpiralDiagonals())
 
main()
  
