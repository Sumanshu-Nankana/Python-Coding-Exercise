# Design an Iterator class, which has:

#  A constructor that takes a string characters of sorted distinct lowercase English 
#  letters and a number combinationLength as arguments.
#  A function next() that returns the next combination of length combinationLength in 
#  lexicographical order.
#  A function hasNext() that returns True if and only if there exists a next combination.

 

# Example:

# CombinationIterator iterator = new CombinationIterator("abc", 2); 
# // creates the iterator.

# iterator.next(); // returns "ab"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "ac"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "bc"
# iterator.hasNext(); // returns false

 

# Constraints:

#     1 <= combinationLength <= characters.length <= 15
#     There will be at most 10^4 function calls per test.
#     It's guaranteed that all calls of the function next are valid.

# =====================================================
# Accepted in Leetcode
# Approach - First create all combinations and append in a queue


class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.q = []
        
        def getCombination(start, length, txt):
            if length == 0:
                self.q.append(txt)
                return
            
            for i in range(start, len(characters)-length+1):
                getCombination(i+1, length-1, txt+characters[i])
        
        getCombination(0, combinationLength, "")

    def next(self):
        """
        :rtype: str
        """
        str_ = self.q[0]
        self.q.pop(0)
        return str_

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q) > 0
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# ====================================================================