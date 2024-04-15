def isValid(s: str) -> bool:
        p_dict = {'(' : ')', '[' : ']','{':'}'}
        p_stack = []
        for i in range(len(s)):
            if s[i] in p_dict.keys():
                p_stack.append(s[i])
            else :
                if len(p_stack) > 0 and s[i] == p_dict[p_stack[len(p_stack)-1]]:
                    p_stack.pop()
                else:
                    return False
        if len(p_stack) == 0:
            return True
        else :
            return False
            


s = "()[]{}"

res = isValid(s)
print(res)


