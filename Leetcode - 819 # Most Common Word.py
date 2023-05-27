import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Replace special chars from paragraph
        filter_paragraph = re.sub(r'[^\w\s]', ' ', paragraph)

        # Convert paragraph to lower case and create a list
        word_list = filter_paragraph.lower().split()

        # Get the frequency of each word
        word_count = {}
        for word in word_list:
            if word not in banned:
                word_count[word] = word_count.get(word, 0) + 1

        most_common_count = -1
        most_common_word = ""
        for word, count in word_count.items():
             if count > most_common_count:
                most_common_count = count
                most_common_word = word

        return most_common_word
