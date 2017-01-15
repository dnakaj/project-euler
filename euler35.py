import math

def isCircularPrime(n):
    numString = str(n)
    for i in range(len(numString)):
        firstSection = numString[:i+1]
        secondSection = numString[i+1:]
        # print(secondSection,firstSection)
        if not (isPrime(int(str(secondSection) + str(firstSection)))):
            return False
    return True
        
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n % i == 0):
            return False
    return True

def main():
    count = 0
    for i in range(2,1000000):
        if (isPrime(i) and isCircularPrime(i)):
            count = count + 1
    print("There are",count,"circular primes below 1 million.")

main()
