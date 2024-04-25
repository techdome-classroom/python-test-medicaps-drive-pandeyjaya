class Solution(object):
    def romanToInt(self, s):
       def romanToInt(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for c in reversed(s):
        curr_value = roman_dict[c]
        if curr_value < prev_value:
            result -= curr_value
        else:
            result += curr_value
        prev_value = curr_value
    
    return result

# Test cases
print(romanToInt("III"))       # Output: 3
print(romanToInt("LVIII"))     # Output: 58
print(romanToInt("MCMXCIV"))   # Output: 1994

        pass
