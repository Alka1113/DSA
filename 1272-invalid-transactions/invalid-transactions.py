class Solution(object):
    def invalidTransactions(self, transactions):
        data = []
        groups = {}

        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")

            time = int(time)
            amount = int(amount)

            data.append((name, time, amount, city, i))

            if name not in groups:
                groups[name] = []

            groups[name].append((time, city, i))

        invalid = set()

        for name in groups:
            groups[name].sort()

            arr = groups[name]

            for i in range(len(arr)):
                time1, city1, index1 = arr[i]

                if data[index1][2] > 1000:
                    invalid.add(index1)

                for j in range(i + 1, len(arr)):
                    time2, city2, index2 = arr[j]

                    if time2 - time1 > 60:
                        break

                    if city1 != city2:
                        invalid.add(index1)
                        invalid.add(index2)

        return [transactions[i] for i in invalid]