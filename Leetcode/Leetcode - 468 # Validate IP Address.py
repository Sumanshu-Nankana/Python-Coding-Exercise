import re

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        """
        For IPv4 - if we able to create the regular expression for first segment
        Then, same regular expression just needs to be repeated 4 times seperated by dot

        We know for digits we can use \d
        But here every segment maximum range is 0 to 255
        So, if we use just \d (which means 0 to 9)
        if we use \d{2} (which means 10 to 99)
        if we use \d{3}  (which means 100 to 999)

        But we want a range from 0 to 255, basically stops at 255
        So, we can't simply use \d
        We need to use something else, Thus we divided it in ranges

        250 to 255 : 25[0-5]
        200 to 249 : 2[0-4]\d
        100 to 199 : 1\d{2}
        10 to 99   : [1-9]\d
        1 to 9     : [1-9]
        0          : 0
        So, first segment can be any of these expression, so simply combined using | (or) operator
        So first segment is:
        ipv4_octet = r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|[1-9]|0)"

        Here 'r' means a raw-string, It's useful to use because if we will not use then backslash part will
        treated as python escape sequence, like \n is for new line ; \t for tab
        Though \d is nothing in Python, But python treated backspash as escape sequence and trying to find
        meaning of \d, but there is no meaning, So it will give Syntax Warning : <stdin>:1: SyntaxWarning: invalid escape sequence '\d'
        and simply print \d

        Thus, we need to use 'r' so that python code do not treat them as escape sequence.
        So this is a raw-string

        Now, we just need to repeat these raw string 3 more times and seperated by a dot(.)

        We CAN NOT Simply DO:

        ipv4_pattern = ipv4_octet.ipv4_octet.ipv4_octet.ipv4_octet
        Because This is Python String, to concatenate python string we need to use + operator

        But if you do :

        ipv4_pattern = ipv4_octet + "." + ipv4_octet + "." + ipv4_octet + "." + ipv4_octet

        This is also WRONG, because dot means (any character), to treat them as a DOT we need to use backslash
        So, correct first segment is

        ipv4_pattern = ipv4_octet + r"\." + ipv4_octet + r"\." + ipv4_octet + r"\." + ipv4_octet

        The other way, is we can repeat this three times using {3} (which means repeat the expresison three times)

        We have TWO functions, re.match() and re.fullmatch()
        if we use re.match(), then it will just match the starting example
        10.10.10.10abc (treated as a Valid String) - which is Wrong

        So, Either we need to use fullmatch() OR we need to add ^ and $
        i.e. caret symbols (i.e. string should start and end at that)

        SIMILARLY, to create the IPv6 Pattern, if we create just the first part, we can repeat it 8 times
        and combine them with colon (:)

        in IPV6 - it can be

        [0-9a-fA-F] --> i.e. any character between 0 to 9, a to f and A to F
        and This can be repeated from 1 to 4 times

        So,

        ipv6_octet = r"[0-9a-fA-F]{1,4}"

        """

        # Creating the IPv4 Regex
        ipv4_octet = r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|[1-9]|0)"

        ipv4_pattern = ipv4_octet + r"\." + ipv4_octet + r"\." + ipv4_octet + r"\." + ipv4_octet

        ipv4_pattern = fr"^{ipv4_pattern}$"

        # Creating the IPv6 Regex
        ipv6_octet = r"[0-9a-fA-F]{1,4}"
        ipv6_pattern = ipv6_octet + ":" + ipv6_octet + ":" + ipv6_octet + ":" + ipv6_octet + ":" + ipv6_octet + ":" + ipv6_octet + ":" + ipv6_octet + ":" + ipv6_octet
        ipv6_pattern = fr"^{ipv6_pattern}$"

        ipv4_regex = re.compile(ipv4_pattern)

        ipv6_regex = re.compile(ipv6_pattern)

        if re.match(ipv4_regex, queryIP):
            return "IPv4"
        elif re.match(ipv6_regex, queryIP):
            return "IPv6"
        else:
            return "Neither"


# Method-2

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        """
        For IPv4 - if we able to create the regular expression for first segment
        Then, same regular expression just needs to be repeated 4 times seperated by dot

        We know for digits we can use \d
        But here every segment maximum range is 0 to 255
        So, if we use just \d (which means 0 to 9)
        if we use \d{2} (which means 10 to 99)
        if we use \d{3}  (which means 100 to 999)

        But we want a range from 0 to 255, basically stops at 255
        So, we can't simply use \d
        We need to use something else, Thus we divided it in ranges

        250 to 255 : 25[0-5]
        200 to 249 : 2[0-4]\d
        100 to 199 : 1\d{2}
        10 to 99   : [1-9]\d
        1 to 9     : [1-9]
        0          : 0
        So, first segment can be any of these expression, so simply combined using | (or) operator
        So first segment is:
        ipv4_octet = r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|[1-9]|0)"

        Here 'r' means a raw-string, It's useful to use because if we will not use then backslash part will
        treated as python escape sequence, like \n is for new line ; \t for tab
        Though \d is nothing in Python, But python treated backspash as escape sequence and trying to find
        meaning of \d, but there is no meaning, So it will give Syntax Warning : <stdin>:1: SyntaxWarning: invalid escape sequence '\d'
        and simply print \d

        Thus, we need to use 'r' so that python code do not treat them as escape sequence.
        So this is a raw-string

        Now, we just need to repeat these raw string 3 more times and seperated by a dot(.)

        We CAN NOT Simply DO:

        ipv4_pattern = ipv4_octet.ipv4_octet.ipv4_octet.ipv4_octet
        Because This is Python String, to concatenate python string we need to use + operator

        But if you do :

        ipv4_pattern = ipv4_octet + "." + ipv4_octet + "." + ipv4_octet + "." + ipv4_octet

        This is also WRONG, because dot means (any character), to treat them as a DOT we need to use backslash
        So, correct first segment is

        ipv4_pattern = ipv4_octet + r"\." + ipv4_octet + r"\." + ipv4_octet + r"\." + ipv4_octet

        The other way, is we can repeat this three times using {3} (which means repeat the expresison three times)

        We have TWO functions, re.match() and re.fullmatch()
        if we use re.match(), then it will just match the starting example
        10.10.10.10abc (treated as a Valid String) - which is Wrong

        So, Either we need to use fullmatch() OR we need to add ^ and $
        i.e. caret symbols (i.e. string should start and end at that)

        SIMILARLY, to create the IPv6 Pattern, if we create just the first part, we can repeat it 8 times
        and combine them with colon (:)

        in IPV6 - it can be

        [0-9a-fA-F] --> i.e. any character between 0 to 9, a to f and A to F
        and This can be repeated from 1 to 4 times

        So,

        ipv6_octet = r"[0-9a-fA-F]{1,4}"

        """

        ipv4_octet = r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|[1-9]|0)"
        repeated_part = r"\." + ipv4_octet
        last_part = f"({repeated_part}){{3}}"
        complete_ipv4_pattern = ipv4_octet + last_part

        # Creating the iPv6 Regex
        ipv6_octet = r"[0-9a-fA-F]{1,4}"
        repeated_part = r":" + ipv6_octet
        last_part = f"({repeated_part}){{7}}"
        complete_ipv6_pattern = ipv6_octet + last_part

        ipv4_regex = re.compile(complete_ipv4_pattern)
        ipv6_pattern = re.compile(complete_ipv6_pattern)

        if re.fullmatch(ipv4_regex, queryIP):
            return "IPv4"
        elif re.fullmatch(ipv6_pattern, queryIP):
            return "IPv6"
        else:
            return "Neither"