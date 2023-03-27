from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        if len(digits) == 0:
            return None

        # if there are 1 or more digits,  store first digit subsets
        # Example if first digit is '2' : ['a', 'b', 'c']
        output = [ch for ch in hash_map.get(digits[0])]

        i = 1
        n = len(digits)

        # Now we can add other digits element with current output
        while i < n:
            temp = []
            for ch in output:
                for h in hash_map.get(digits[i]):
                    temp.append(ch + h)

            output = temp
            i = i + 1

        return output



# Example & Explanation
# "2     3       4"
# "abc"  "def"   "ghi"

# ['a', 'b', 'c']

# Add 'd' with all elements
# Then add 'e' with all elements
# Then add 'f' with all elements

# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

# Add 'g' with all elements
# Add 'h' with all elements
# Add 'i' with all elements

# ['adg', 'aeg', 'afg', 'bdg', 'beg', 'bfg', 'cdg', 'ceg', 'cfg',
#  'adh', 'aeh', 'afh', 'bdh', 'beh', 'bfh', 'cdh', 'ceh', 'cfh',
#  'adi', 'aei', 'afi', 'bdi', 'bei', 'bfi', 'cdi', 'cei', 'cfi']