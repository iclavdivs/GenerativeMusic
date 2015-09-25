import unittest
import math
from Classes.Function import Function

class FunctionTests(unittest.TestCase):

    function = Function()

    def setUp(self):
        function = Function()

    def test_sin(self):
        self.assertEqual(self.function.sin(0), math.sin(0))

    def test_performOp(self):
        x = 1.0
        y = 2.0
        self.assertEquals(self.function.performOp('+', x, y), x + y)
        self.assertEquals(self.function.performOp('-', x, y), x - y)
        self.assertEquals(self.function.performOp('*', x, y), x * y)
        self.assertEquals(self.function.performOp('/', x, y), x / y)

    # def test_evalOperand(self):
    #
    #     equation  = ['1', '+', '1', '*', '2']
    #     #self.assertEquals(self.function.evalOperand(equation.index('*'), equation), 1 * 2 )
    #     equation = self.function.evalOperand(equation.index('*'),equation)
    #     self.assertEquals(equation, ['1', '+', '2.0'])
    #     #self.assertNotEquals(self.function.evalOperand(equation.index('+'), equation), 1 + 2 )
    #     equation = self.function.evalOperand(equation.index('+'), equation)
    #     self.assertEquals(equation, ['2.0'])


    def test_simplifyEquations(self):
        equation  = ['1.0', '+', '1.0', '*', '2.0', '/', '0.5', '-', '2.0']
        operandList = ['*','/']

        equation  = self.function.simplifyEquation(equation, operandList)

        self.assertEquals(equation, ['1.0','+','4.0','-','2.0'])

        operandList = ['+','-']
        equation = self.function.simplifyEquation(equation, operandList)

        self.assertEquals(equation, ['3.0'])

    def test_evalFourArith(self):
        equation  = ['1.0', '+', '1.0', '*', '2.0', '/', '0.5', '-', '2.0']

        equation = self.function.evalFourArith(equation)

        self.assertEquals(equation, '3.0')

    def test_evalParenthesis(self):
        equation  = ['(', '1.0', '+', '1.0', '*', '2.0', '/', '0.5', '-', '2.0',')']
        equation2 = ['(', '1.0', ')']
        equation3 = ['1', '+', '3', '*', '(', '1.0', '+', '1.0', '*', '2.0', '/', '0.5', '-', '2.0',')']
        equation4 = ['(', '4.0','+','3.0','*','3.0',')','-','4','*','(','1.0','+','8','*','(','1.0','+','5.0',')',')']

        self.assertEquals(self.function.evalParenthesis(equation), '3.0')
        self.assertEquals(self.function.evalParenthesis(equation2), '1.0')
        self.assertEquals(self.function.evalParenthesis(equation3), str(float( 1+ 3*(1.0+1.0*2.0/0.5-2.0))))
        self.assertEquals(self.function.evalParenthesis(equation4), str(float((4.0+3.0*3.0)-4*(1.0+8*(1.0+5.0)))))