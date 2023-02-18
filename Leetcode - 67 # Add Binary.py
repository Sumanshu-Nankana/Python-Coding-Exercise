class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a.zfill(max(len(a), len(b)))
        b = b.zfill(max(len(a), len(b)))

        i = len(a) - 1
        output = ''
        carry = 0
        while i >= 0:
            temp = int(a[i]) + int(b[i]) + carry
            if temp <= 1:
                output = str(temp) + output
                carry = 0
            elif temp == 2:
                output = '0' + output
                carry = 1
            else:
                output = '1' + output
                carry = 1
            i = i - 1
            print(output)

        if carry == 1:
            output = str(carry) + output

        return output


a = '11'
b = '1'
print(Solution().addBinary(a, b))