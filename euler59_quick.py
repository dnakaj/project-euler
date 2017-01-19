from collections import Counter
    
def findPasswordFrequencyAnalysis(fileName):
    
    f = open(fileName, 'r')
    
    list1 = []
    list2 = []
    list3 = []
    
    values = f.read().split(',')
    
    # Fill validChars with the letters a-z
    validChars = []
    
    for i in range(ord('a'), ord('z')+1):
        validChars.append(chr(i))
    
    temp = []
    
    for c in values:
        temp.append(chr(int(c)))
    
    # Frequency analysis to get characters
    for i in range(len(values)):
        if (i%3 == 0): # gets every 3rd character (starting at the 1st character)
            list1.append(chr(int(values[i])))
        elif (i%3 == 1): # gets every 2nd character (starting from the 2nd character)
            list2.append(chr(int(values[i])))
        else:
            list3.append(chr(int(values[i])))
            
            
    list1Counter = Counter(list1)
    list2Counter = Counter(list2)
    list3Counter = Counter(list3)
    
    firstKeyChar = list1Counter.most_common(1)[0]
    secondKeyChar = list2Counter.most_common(1)[0]
    thirdKeyChar = list3Counter.most_common(1)[0]
    
    fullKey = firstKeyChar[0] + secondKeyChar[0] + thirdKeyChar[0]
    
    fullKey = fullKey * (len(values) // 3) + fullKey[:(len(values) % 3)]
    dec = xorDecrypt(values, fullKey.lower()) 
    
    return ''.join(dec)
    
def main():   
    print(findPasswordFrequencyAnalysis("cipher.txt"))
    
main()
