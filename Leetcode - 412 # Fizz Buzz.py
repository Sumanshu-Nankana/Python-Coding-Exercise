from typing import List


# In this solution, we are unnecessary checking i % 5 twice
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [""] * n
        for i in range(1, n + 1):
            if i % 5 and i % 3 == 0:
                answer[i - 1] = "FizzBuzz"
            elif i % 3 == 0:
                answer[i - 1] = "Fizz"
            elif i % 5 == 0:
                answer[i - 1] = "Buzz"
            else:
                answer[i - 1] = str(i)
        return answer


# Method-2 - Using List Comprehension
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i) for i in range(1, n + 1)]


# Method-3
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [""] * n
        for i in range(1, n + 1):
            if i % 3 == 0: answer[i - 1] = answer[i - 1] + "Fizz"
            if i % 5 == 0: answer[i - 1] = answer[i - 1] + "Buzz"
            if answer[i - 1] == "": answer[i - 1] = answer[i - 1] + str(i)
        return answer


# Method-4
# Modulus operator is little costly, as compare to addition and subtraction
# So in this method, we are trying using addition and subtraction
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [""] * n
        c3, c5 = 0, 0
        for i in range(1, n + 1):
            c3 = c3 + 1
            c5 = c5 + 1
            if c3 == 3: answer[i - 1] = answer[i - 1] + "Fizz"; c3 = 0
            if c5 == 5: answer[i - 1] = answer[i - 1] + "Buzz"; c5 = 0
            if answer[i - 1] == "": answer[i - 1] = answer[i - 1] + str(i)
        return answer
