class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""
        roman_integer_pairs = (
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        )

        for symbol, value in roman_integer_pairs:
            while num >= value:
                output = output + symbol
                num = num - value

        return output


sol = Solution()
sol.intToRoman(3289)


# If we just run our code using the roman provided in question,
# we will get wrong answer (example Below)
# example we write 9 as IX instead of VIIII
# Thus for those extra integers, we need to define the values in advance.


# 3289
# 3289 - 1000 => 2289 => M
# 2289 - 1000 => 1189 => MM
# 1289 - 1000 => 289 => MMM
# 289 - 100 => 189 => MMMC
# 189 - 100 => 89 => MMMCC
# 89 - 50 => 39 => MMMCCL
# 39 - 10 => 29 => MMMCCLX
# 29 - 10 > 19 => MMMCCLXX
# 19 - 10 => 9 => MMMCCLXXX
# 19 - 5 => 4 => MMMCCLXXXV
# 4 - 1 => 3 => MMMCCLXXXVI
# 3 -1 => 2 => MMMCCLXXXVII
# 2 - 1 => 1 => MMMCCLXXXVIII
# 1 - 1 => 0 => MMMCCLXXXVIIII


# But correct is if we consider 9, 4 these numbers as well

# 3289
# 3289 - 1000 => 2289 => M
# 2289 - 1000 => 1189 => MM
# 1289 - 1000 => 289 => MMM
# 289 - 100 => 189 => MMMC
# 189 - 100 => 89 => MMMCC
# 89 - 50 => 39 => MMMCCL
# 39 - 10 => 29 => MMMCCLX
# 29 - 10 > 19 => MMMCCLXX
# 19 - 10 => 9 => MMMCCLXXX
# 9 - 9 => 0 => MMMCCLXXXIX
