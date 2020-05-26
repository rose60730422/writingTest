
def reverseString(t):
    reverseString = t[::-1]
    return reverseString

def reverseWords(s):
    s = s.split(" ")
    for index, word in enumerate(s) :
        s[index] = reverseString(word)
    r = ' '.join(s)    
    return r

def countingFactor(n):
    cnt = 0
    for i in range(n):
        if ((i+1) % 3 == 0) and ((i+1) % 5 == 0):
            cnt = cnt + 1
        elif ((i+1) % 3 != 0) and ((i+1) % 5 != 0):
            cnt = cnt + 1
    return cnt


text_A = input('Please enter your string : ')
print(reverseString(text_A))
text_B = input('Please enter your sentence : ')
print(reverseWords(text_B))
number = input('Please enter your number : ')
print(countingFactor(int(number)))

