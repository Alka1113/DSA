class Solution(object):
    def invalidTransactions(self, transactions):
        invalid = []

        for i in range(len(transactions)):
            name1, time1, amount1, city1 = transactions[i].split(",")
            time1 = int(time1)
            amount1 = int(amount1)

            is_invalid = False

            # Check amount
            if amount1 > 1000:
                is_invalid = True

            # Compare with every other transaction
            for j in range(len(transactions)):
                if i == j:
                    continue

                name2, time2, amount2, city2 = transactions[j].split(",")
                time2 = int(time2)

                if (name1 == name2 and
                    city1 != city2 and
                    abs(time1 - time2) <= 60):
                    is_invalid = True

            if is_invalid:
                invalid.append(transactions[i])

        return invalid