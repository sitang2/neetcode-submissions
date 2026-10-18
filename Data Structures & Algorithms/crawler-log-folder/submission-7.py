class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            stack.append(log)

            if log == './':
                stack.pop()
                continue
            elif log == '../':
                stack.pop()
                if stack:
                    stack.pop()
                continue

            print(stack)
        return len(stack)