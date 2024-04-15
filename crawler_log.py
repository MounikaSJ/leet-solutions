def minOperations(logs) -> int:
        logs_stack = []
        for i in range(len(logs)):
            if logs[i] == '../':
                if len(logs_stack) > 0:
                    logs_stack.pop()
            elif logs[i] == './':
                continue
            else :
                logs_stack.append(logs[i])

        return len(logs_stack)


logs = ["d1/","d2/","./","d3/","../","d31/"]

result = minOperations(logs)
print(result)