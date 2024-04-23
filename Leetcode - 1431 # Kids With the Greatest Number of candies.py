class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []

        # Instead of comparing with all candies one by one
        # we can compare with the one which is maximum
        # Because if it is greater than the maximum, Then it will greater from all others
        max_candies = max(candies)
        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result


# We can use the ListComprehension as well
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy+extraCandies >= max_candies for candy in candies]
