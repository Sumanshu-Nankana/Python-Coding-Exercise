import math


class Solution:
    def countPrimesBruteForce(self, n: int) -> int:
        count = 0
        if n < 2: return count
        for i in range(2, n):
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                count = count + 1
        return count

    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        is_prime = [True]*n
        is_prime[0] = is_prime[1] = False

        for i in range(2, n):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False

        return sum(is_prime)

    def countPrimesOptimalApproach(self, n: int) -> int:
        if n < 2: return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for i in range(2, math.ceil(math.sqrt(n))):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False

        return sum(isPrime)

n = 10
s = Solution()
print(s.countPrimesBruteForce(n))
print(s.countPrimes(n))
print(s.countPrimesOptimalApproach(n))
