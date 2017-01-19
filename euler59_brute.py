# Converts a string to an array of ints (for use in xorDecrypt)
def stringToIntArray(s):
    result = []
    for ch in s:
        result.append(ord(ch)) # ord converts a character to its ascii equivalent
    return result

# Method to decrypt an encrypted array of ints; returns an array of characters
def xorDecrypt(enc, k):
    key = stringToIntArray(k)
    
    if (len(enc) != len(key)):
        return -1
    
    dec = []
    for i in range(len(enc)):
        dec.append(chr(int(enc[i]) ^ key[i]))
    
    return dec
        
# Fill validChars with the letters a-z
validChars = []

for i in range(ord('a'), ord('z')+1):
    validChars.append(chr(i))

# This list contains the 5 most common English words
keyWords = [' the ', ' be ', ' to ', ' of ', ' and ']    

file = open("cipher.txt", 'r')
fileContents = file.read().split(',')

# Solves the problem; returns an array of strings
def findPassword(key):
    
    dec = []
    
    if (len(key) < 3):
        for c in validChars:
            result = findPassword(key + c)
            if (str(result)[0] != "0"):
                return result
    else:
        
        fullKey = (key * (len(fileContents) // 3)) + key[:(len(fileContents) % 3)]
        
        dec = ''.join(xorDecrypt(fileContents, fullKey))
        
        # Code used only to test if the decrypted text contained a word
        #if "the" in dec:
        #   print(''.join(dec))
        
        keyWordCount = 0
        
        for word in keyWords:
            if word in dec:
                keyWordCount = keyWordCount + dec.count(word)
                
        if (keyWordCount > 5):
            return dec
    return 0

def main():   
    print(''.join(findPassword('')))

main()
    
