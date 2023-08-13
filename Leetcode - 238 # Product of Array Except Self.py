# Without using divison operator
# But using O(n^2)
# 18/22 Test Cases Passed
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        for i in range(n):
            for j in range(n):
                if i != j:
                    output[i] = output[i] * nums[j]

        return output


# Using Division Operator
# And using O(n) Time complexity
# if we don't consider zero elements, then when element is zero
# it wil give ZeroDivisionError or Module Error.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total_product = 1
        total_zeros = 0

        for num in nums:
            if num != 0:
                total_product = total_product * num
            else:
                total_zeros += 1

        for num in nums:
            if total_zeros == 0:
                output.append(total_product // num)
            elif total_zeros == 1 and num == 0:
                output.append(total_product)
            else:
                output.append(0)

        return output


# Without Division Operator
# And In O(n)
# but using Extra space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)

        prefix_products = [1] * n
        postfix_products = [1] * n

        prefix_product = 1
        for i in range(n):
            prefix_products[i] = prefix_product
            prefix_product = prefix_product * nums[i]

        postfix_product = 1
        for i in range(n-1, -1, -1):
            postfix_products[i] = postfix_product
            postfix_product = postfix_product * nums[i]

        for i in range(n):
            result.append(prefix_products[i] * postfix_products[i])

        return result
