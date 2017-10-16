# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:47:56 2017

@author: Полина
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:52:05 2017

@author: Полина
"""
#ochko
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

S_BOX = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def binvalue(val, n):#Возвращает двоичное значение стркои заданой длины
    if type(val) == int:
        binval = bin(val)[2:]
    else:
        binval = bin(ord(val))[2:]
    
    while len(binval) < n:
        binval = "0"+binval
    return binval

def s2ba(text):#string to bit array
    array = list()
    
    for char in text:
        binval = binvalue(char, 8)
        
        for x in list(binval):
            array.extend([int(x)])
            
    return array

def ba2s(array): #bit array to string
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in bytes]) for bytes in  split(array,8)]])   
    return res

def permutation(block, table):
    new_block = []
    for x in table:
       new_block.append(block[x-1]) 
    return new_block

def split(s, n):
    rez = []
    for k in range(0, len(s), n):
        rez.append(s[k:k+n])
    return rez
def shift(c, d, n):
    return c[n:]+c[:n], d[n:]+d[:n]

def generate_key(password):
    keys = []
    key = s2ba(password)
    key = permutation(key, CP_1)
    c, d = split(key, 28)
    for i in range(16):
        c, d = shift(c, d, SHIFT[i])
        keys.append(permutation(c+d, CP_2))
    return keys

def substitute( d_e):
    subblocks = split(d_e, 6)
    result = list()
    for i in range(len(subblocks)): 
        block = subblocks[i]
        row = int(str(block[0])+str(block[5]),2)
        column = int(''.join([str(x) for x in block[1:][:-1]]),2) 
        val = S_BOX[i][row][column] 
        bin = binvalue(val, 4)
        result += [int(x) for x in bin]
    return result

def DES(password, text, action):
    keys = generate_key(password)
    text_block = split(text, 8)
    
    res = []
    for block in text_block:
        block = s2ba(block)
        block = permutation(block, IP)
        l, r = split(block, 32)
        for i in range(16):
            r_e = permutation(r, E)
            
            if action == 0:
                tmp = [x^y for x,y in zip(keys[i], r_e)]
                
            else: tmp = [x^y for x,y in zip(keys[15 - i], r_e)]
            
            tmp = substitute(tmp)
            tmp = permutation(tmp, P)
            tmp = [x^y for x,y in zip(l, tmp)]
            l = r
            r = tmp
        res += permutation(r+l, PI_1)
    final_res = ba2s(res)
    return final_res

def triple_DES(passwords, text, action):
    text_en = text
    if action == 0:
        for i in range(3):
            #print("coding", text_en)
            #print("password", password[i])
            text_en = DES(password[i], text_en, action)
            #print("result_cod", text_en)
            #print("\n")
        
    if action == 1:
        for i in range(3):
            #print("decoding", text_en)
            #print("password", password[2-i])
            text_en = DES(password[2 - i], text_en, action)
            #print("result_dec", text_en)
            #print("\n")
    return text_en
            
    
password = ["11111111", "22222222", "33333333"]
text = open("txt.txt")
t = text.read()
t_e = triple_DES(password, t, 0)
t_d = triple_DES(password, t_e, 1)
print(t)
print(t_e)
print(t_d)
text.close()


