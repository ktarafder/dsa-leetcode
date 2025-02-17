'''
Write a function solve that converts an integer to a roman numeral. More info about roman numerals can be found here.

Example:
Input: 58
Output: "LVIII" 
'''

# Better solution
def solve(num: int):
    '''
    Could use an array of tuples here like this:
        roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
    '''
    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbols = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    result = ''
    for i, value in enumerate(values):
        while num >= value:
            result += symbols[i]
            num -= value
    return result

print(solve(4))
print(solve(58))

# My solution or the one gpt half generated for me, I didn't want to write out every elif, just wrote the main ones
def solve(num):
    res = []
    
    while num != 0:
        if num >= 1000:
            res.append('M')
            num -= 1000
        elif num >= 900:
            res.append('CM')
            num -= 900
        elif num >= 500:
            res.append('D')
            num -= 500
        elif num >= 400:
            res.append('CD')
            num -= 400
        elif num >= 100:
            res.append('C')
            num -= 100
        elif num >= 90:
            res.append('XC')
            num -= 90
        elif num >= 50:
            res.append('L')
            num -= 50
        elif num >= 40:
            res.append('XL')
            num -= 40
        elif num >= 10:
            res.append('X')
            num -= 10
        elif num >= 9:
            res.append('IX')
            num -= 9
        elif num >= 5:
            res.append('V')
            num -= 5
        elif num >= 4:
            res.append('IV')
            num -= 4
        else:
            res.append('I')
            num -= 1
    
    return ''.join(res)

print(solve(4))


