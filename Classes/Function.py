__author__ = 'Iclavdivs'
# todo: CFFunction and CPFunction subclasses
import math
class Function:
    def defaultFunct(self, input ):
        return 1
    #
    # Add support for basic math functions
    # a * f(x) + c
    #
    # sin(x)
    def sin(self, x):
        return math.sin(x)

    # cos(x)
    # tan(x)
    # cot(x)
    # b*x^n
    #
    # Add support for derivatives of the provided cantus firmus function
    #     (f(xm) - f(xn))/(xm - xn)
    #
    # def postFixFunction(self, function,x):
    #     queue: < + x y <
    #             + - 2 3 + 3 4
    #             + - 2 4 5
    #
    #     recursive
    #     def recursivePostFix( queue )
    #         element = queue.pop()
    #         if num
    #             return num
    #         else if known operation
    #             return recursivePostFix(queue) oper recurvsivePostFix (queue)
    #     What if it is malformed? how to validate?
    #     what about functions with more than 2 inputs?
    #
    #     iterative
    #     def iterativePostFix( splitEquation )
    #         numStack = empty
    #         equationStack = splitEquation
    #         while equationStack is not empty
    #             element = equationStack.pop
    #             if element is num
    #                 numStack.push (element)
    #             else if known oper
    #                 result = numStack.pop oper numStack.pop
    #                 numStack.push (result)
    #
    #         return numStack.pop
    #
    #     IN FIX
    #     Three parts:
    #         0. Eval operand
    #         1. four basic arithmetica operations
    #         2. Parenthesis
    #         3. Functions
    #
    #     Steps:
    #         Evaluate all steps inside parenthesis first
    #             iterate through the parsed string: 1 + ( 5 - 5*6 + sin(0) - (4-5))
    #         Then functions
    #         Then 4 arithmetic steps
    #
    #     assumes that index is a value in the interior of the list, assumes list is >= 3
    #     assumes list is perfecctly parsed e.g. ['1','+','2']
    #     modifies list with the result of the operation
    #     returns result of operation

    def evalOperand(self, index, list):
        operand = list[index]

        arg1 = list[index -1 ]
        arg2 = list[index + 1]
        result = performOp(operand, arg1, arg2) #TODO: performOp uses switch logic to choose +,-,/,*. Maybe use a factory design?
        evaluatedList = list[0:index -1] + result + list[index+2:len(list)]
        list = evaluatedList
        return result

    def performOp(self, operand, arg1, arg2):
        return 1

    # assumes list is perfectly parsed e.g. ['1','+','2'] and formatted, with no hanging operators
    # returns result of all operations
    # TODO: write unit tests
    def evalFourArith(self, list): #TODO: Add self
        # TODO: Add support for '^'
        # eval */ first
        for i in range(len(list)):
            if list[i] in ['*','/']:
                evalOperand(i,list) #updates list with evaluation

        # eval +- second
        for i in range(len(list)):
            if list[i] in ['-','+']:
                evalOperand(i,list) #updates list with evaluation
        # TODO: throw error if not entirely evaluated, meaning if list length > 1
        return list[0]

    # Assumes list is a perfectly formatted arithmetic equation with matching parens
    def evalParenthesis(self, list):
        leftParenStack = [0]
        while (len(leftParenStack) > 0 ):
            someBooleanToContinueLoop = True
            i = leftParenStack.pop()
            while (i < len(list) and someBooleanToContinueLoop):
                if list[i] == '(':
                    # push the leftParenIndex
                    leftParenStack.append(i)
                elif list[i] == ')':
                    # peak the top of the stack
                    idx1 = leftParenStack.index(len(leftParenStack) - 1)
                    # evaluate the 4operand arithmetic function
                    result = evalFourArith(list[idx1:i]) # TODO: add self
                    # append evaluated parenthesis to list
                    list = list[0:idx1] + result + list[i+1:]
                    # TODO: check if list[idx1 - 1] is a function, after adding function support
                    someBooleanToContinueLoop = False
                i += 1
        # TODO: CHECK THAT LIST IS PROPERLY EVALUATED ie LENGTH = 1
        return list[0]

