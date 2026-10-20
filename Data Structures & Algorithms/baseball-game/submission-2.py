class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == "+":
                record.append(record[-1] + record[-2])
            elif op == 'C':
                record.pop()
            elif op == 'D':
                a = record[-1]
                doub = a * 2
                record.append(doub)
            else:
                record.append(int(op))

        return sum(record)