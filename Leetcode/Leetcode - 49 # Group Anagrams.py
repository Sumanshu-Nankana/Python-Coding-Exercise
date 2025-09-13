from typing import List


class Solution:
    def groupAnagramsMethod1(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        result = []

        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in hash_map:
                hash_map[sorted_str] = [str]
            else:
                hash_map[sorted_str].append(str)

        for k, v in hash_map.items():
            result.append(v)

        return result

    def groupAnagramsMethod2(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for str in strs:
            sorted_str = "".join(sorted(str))
            hash_map[sorted_str] = hash_map.get(sorted_str, []) + [str]

        return hash_map.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagramsMethod1(strs))
print(Solution().groupAnagramsMethod2(strs))
