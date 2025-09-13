class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0

        # Base Condition, if flowers == 0, Then no need to run loop, Simply return True
        if n == 0: return True

        for i in range(length):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1

                # As we can directly return as soon as we placed all flowers
                # There is no need to go till end of flowerbed.
                if count == n:
                    return True

        return False
