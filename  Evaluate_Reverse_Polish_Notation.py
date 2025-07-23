class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #create empty stack
        stack = []

        #loop through tokens
        for token in tokens:
            
            if token in {"+","-","*","/"}:

                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    result = left +right
                elif token == "-":
                    result = left - right
                elif token == "*":
                    result = left * right
                elif token == "/":
                    result = int(left/right)

                stack.append(result)

            else :
                val = int(token)
                stack.append(val)
        
        return stack[0]
        