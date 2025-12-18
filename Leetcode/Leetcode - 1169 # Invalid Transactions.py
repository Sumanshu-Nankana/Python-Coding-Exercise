from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        name_map  = defaultdict(list)
        for idx, t in enumerate(transactions):
            name, time, amount, city = t.split(",")
            txn_data = [int(time), int(amount), city, idx]
            name_map [name].append(txn_data)

        output  = []
        for idx, t in enumerate(transactions):
            name, time, amount, city = t.split(",")
            time, amount = int(time), int(amount)
            if amount >= 1000:
                output.append(t)
            else:
                # lookup for the other txns
                for other_time, other_amount, other_city, other_idx in name_map[name]:
                    if other_idx != idx and (abs(time - other_time)) <= 60 and city != other_city:
                            output.append(t)
                            break

        return output

s = Solution()

#transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
#transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
#transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
transactions = ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
output = s.invalidTransactions(transactions)
print(output)