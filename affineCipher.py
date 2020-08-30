from random import *

freqE = [.0804, .0154,.0306,.0399,.1251,.023,.0196,.0549,
         .0726, .0016, .0067,.0414,.0253,.0709,.076,.020,
         .0011,.0612, .0654,.0925,.0271,.0099,.0192,.0019,
         .0173,.0009]

def stringToIntList(text):
    text = text.lower()
    
    lst = [(ord(letter) - ord('a')) for letter in text if letter.isalpha()]
    return lst

def intListToString(lst):
    text = ''.join([chr(ord('a')+code) for code in lst])
    return text

#affine cipher

def affine_h(pt,a,b):
    #helper function: works on coded text
    return [(a*x+b)%26 for x in pt]

def antiAffine_h(pt,inverseA,minusB):
    #helper function: works on coded text
    return [((x+minusB)*inverseA)%26 for x in pt] # Change that first x!

def affine_encode(pt,a,b):
    pt = stringToIntList(pt)
    return intListToString(affine_h(pt,a,b))

def affine_decode(pt,inverseA,minusB):
    pt = stringToIntList(pt)
    return intListToString(antiAffine_h(pt,inverseA,minusB))

def affine_decode_brute():
    #'gjccz' = 'hello'
    #inverseA = 25
    #minusB = 13
    #This function brute forces every possible combination
    #of inverseA and minusB
    
    pt = 'gjccz'
    for i in range(0, 26):
        print("i = " + str(i))
        for j in range(0, 26):
            print("j = " + str(j))
            x = affine_decode(pt,i,j)
            print(x) 

        
