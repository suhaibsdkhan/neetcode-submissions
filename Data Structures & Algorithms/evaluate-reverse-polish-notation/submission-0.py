class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for i in tokens:

            if i =="+":
                stack.append(stack.pop()+stack.pop())

            elif i =="-":
                a=stack.pop() #number on top of stack
                b=stack.pop() #number more inside stack

                stack.append(b-a)

            elif i=="*":
                stack.append(stack.pop() * stack.pop())
            elif i=="/":
                a=stack.pop() #number on top of stack
                b=stack.pop() #number more inside stack
                stack.append(int(b/a))
            else:
                stack.append(int(i))

        return stack[0]

