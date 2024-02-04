class Solution:
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
 
    def romanToInt(self, s: str) -> int:
        integer = 0
        i = 0

        while i < len(s):
            char = s[i]
            if(i != len(s) - 1):
                if char == 'I' and s[i+1] == "V" or char == 'I' and s[i+1] == "X":
                    integer += self.roman_dict[s[i] + s[i+1]]
                    i += 2
                    continue
                
                if char == 'X' and s[i+1] == "L" or char == 'X' and s[i+1] == "C":
                    integer += self.roman_dict[s[i] + s[i+1]]
                    i += 2
                    continue
                
                if char == 'C' and s[i+1] == "D" or char == 'C' and s[i+1] == "M":
                    integer += self.roman_dict[s[i] + s[i+1]]
                    i += 2
                    continue
            
            integer += self.roman_dict[char]
            i += 1
            
        return integer

"""
Could also for less specific cases:
    1. replace subtractions with "wrong numbers
        - count them normally
        - butchers roman numerals but works
        - example:
    
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    
    2. actually compare the characters, and if a smaller value 
        appears before a larger value it is a subtraction
        - example: 
        
        for i in range(len(s)):
            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
                ans -= roman_dict[s[i]]
            else:
                ans += roman_dict[s[i]]
        
        return ans
"""
        
class main:
    solution = Solution()
    
    print(solution.romanToInt("III"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))