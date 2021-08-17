# Generated from LCC.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LCCParser import LCCParser
else:
    from LCCParser import LCCParser

# This class defines a complete listener for a parse tree produced by LCCParser.
class LCCListener(ParseTreeListener):

    # Enter a parse tree produced by LCCParser#start.
    def enterStart(self, ctx:LCCParser.StartContext):
        pass

    # Exit a parse tree produced by LCCParser#start.
    def exitStart(self, ctx:LCCParser.StartContext):
        pass


    # Enter a parse tree produced by LCCParser#funclist.
    def enterFunclist(self, ctx:LCCParser.FunclistContext):
        pass

    # Exit a parse tree produced by LCCParser#funclist.
    def exitFunclist(self, ctx:LCCParser.FunclistContext):
        pass


    # Enter a parse tree produced by LCCParser#funcdef.
    def enterFuncdef(self, ctx:LCCParser.FuncdefContext):
        pass

    # Exit a parse tree produced by LCCParser#funcdef.
    def exitFuncdef(self, ctx:LCCParser.FuncdefContext):
        pass


    # Enter a parse tree produced by LCCParser#paramlist.
    def enterParamlist(self, ctx:LCCParser.ParamlistContext):
        pass

    # Exit a parse tree produced by LCCParser#paramlist.
    def exitParamlist(self, ctx:LCCParser.ParamlistContext):
        pass


    # Enter a parse tree produced by LCCParser#statement.
    def enterStatement(self, ctx:LCCParser.StatementContext):
        pass

    # Exit a parse tree produced by LCCParser#statement.
    def exitStatement(self, ctx:LCCParser.StatementContext):
        pass


    # Enter a parse tree produced by LCCParser#vardecl.
    def enterVardecl(self, ctx:LCCParser.VardeclContext):
        pass

    # Exit a parse tree produced by LCCParser#vardecl.
    def exitVardecl(self, ctx:LCCParser.VardeclContext):
        pass


    # Enter a parse tree produced by LCCParser#atribstat.
    def enterAtribstat(self, ctx:LCCParser.AtribstatContext):
        pass

    # Exit a parse tree produced by LCCParser#atribstat.
    def exitAtribstat(self, ctx:LCCParser.AtribstatContext):
        pass


    # Enter a parse tree produced by LCCParser#funccall.
    def enterFunccall(self, ctx:LCCParser.FunccallContext):
        pass

    # Exit a parse tree produced by LCCParser#funccall.
    def exitFunccall(self, ctx:LCCParser.FunccallContext):
        pass


    # Enter a parse tree produced by LCCParser#paramlistcall.
    def enterParamlistcall(self, ctx:LCCParser.ParamlistcallContext):
        pass

    # Exit a parse tree produced by LCCParser#paramlistcall.
    def exitParamlistcall(self, ctx:LCCParser.ParamlistcallContext):
        pass


    # Enter a parse tree produced by LCCParser#printstat.
    def enterPrintstat(self, ctx:LCCParser.PrintstatContext):
        pass

    # Exit a parse tree produced by LCCParser#printstat.
    def exitPrintstat(self, ctx:LCCParser.PrintstatContext):
        pass


    # Enter a parse tree produced by LCCParser#readstat.
    def enterReadstat(self, ctx:LCCParser.ReadstatContext):
        pass

    # Exit a parse tree produced by LCCParser#readstat.
    def exitReadstat(self, ctx:LCCParser.ReadstatContext):
        pass


    # Enter a parse tree produced by LCCParser#returnstat.
    def enterReturnstat(self, ctx:LCCParser.ReturnstatContext):
        pass

    # Exit a parse tree produced by LCCParser#returnstat.
    def exitReturnstat(self, ctx:LCCParser.ReturnstatContext):
        pass


    # Enter a parse tree produced by LCCParser#ifstat.
    def enterIfstat(self, ctx:LCCParser.IfstatContext):
        pass

    # Exit a parse tree produced by LCCParser#ifstat.
    def exitIfstat(self, ctx:LCCParser.IfstatContext):
        pass


    # Enter a parse tree produced by LCCParser#forstat.
    def enterForstat(self, ctx:LCCParser.ForstatContext):
        pass

    # Exit a parse tree produced by LCCParser#forstat.
    def exitForstat(self, ctx:LCCParser.ForstatContext):
        pass


    # Enter a parse tree produced by LCCParser#statelist.
    def enterStatelist(self, ctx:LCCParser.StatelistContext):
        pass

    # Exit a parse tree produced by LCCParser#statelist.
    def exitStatelist(self, ctx:LCCParser.StatelistContext):
        pass


    # Enter a parse tree produced by LCCParser#allocexpression.
    def enterAllocexpression(self, ctx:LCCParser.AllocexpressionContext):
        pass

    # Exit a parse tree produced by LCCParser#allocexpression.
    def exitAllocexpression(self, ctx:LCCParser.AllocexpressionContext):
        pass


    # Enter a parse tree produced by LCCParser#expression.
    def enterExpression(self, ctx:LCCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LCCParser#expression.
    def exitExpression(self, ctx:LCCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LCCParser#numexpression.
    def enterNumexpression(self, ctx:LCCParser.NumexpressionContext):
        pass

    # Exit a parse tree produced by LCCParser#numexpression.
    def exitNumexpression(self, ctx:LCCParser.NumexpressionContext):
        pass


    # Enter a parse tree produced by LCCParser#term.
    def enterTerm(self, ctx:LCCParser.TermContext):
        pass

    # Exit a parse tree produced by LCCParser#term.
    def exitTerm(self, ctx:LCCParser.TermContext):
        pass


    # Enter a parse tree produced by LCCParser#unaryexpr.
    def enterUnaryexpr(self, ctx:LCCParser.UnaryexprContext):
        pass

    # Exit a parse tree produced by LCCParser#unaryexpr.
    def exitUnaryexpr(self, ctx:LCCParser.UnaryexprContext):
        pass


    # Enter a parse tree produced by LCCParser#factor.
    def enterFactor(self, ctx:LCCParser.FactorContext):
        pass

    # Exit a parse tree produced by LCCParser#factor.
    def exitFactor(self, ctx:LCCParser.FactorContext):
        pass


    # Enter a parse tree produced by LCCParser#lvalue.
    def enterLvalue(self, ctx:LCCParser.LvalueContext):
        pass

    # Exit a parse tree produced by LCCParser#lvalue.
    def exitLvalue(self, ctx:LCCParser.LvalueContext):
        pass


    # Enter a parse tree produced by LCCParser#types.
    def enterTypes(self, ctx:LCCParser.TypesContext):
        pass

    # Exit a parse tree produced by LCCParser#types.
    def exitTypes(self, ctx:LCCParser.TypesContext):
        pass


    # Enter a parse tree produced by LCCParser#openParantheses.
    def enterOpenParantheses(self, ctx:LCCParser.OpenParanthesesContext):
        pass

    # Exit a parse tree produced by LCCParser#openParantheses.
    def exitOpenParantheses(self, ctx:LCCParser.OpenParanthesesContext):
        pass


    # Enter a parse tree produced by LCCParser#closeParantheses.
    def enterCloseParantheses(self, ctx:LCCParser.CloseParanthesesContext):
        pass

    # Exit a parse tree produced by LCCParser#closeParantheses.
    def exitCloseParantheses(self, ctx:LCCParser.CloseParanthesesContext):
        pass


    # Enter a parse tree produced by LCCParser#openBraces.
    def enterOpenBraces(self, ctx:LCCParser.OpenBracesContext):
        pass

    # Exit a parse tree produced by LCCParser#openBraces.
    def exitOpenBraces(self, ctx:LCCParser.OpenBracesContext):
        pass


    # Enter a parse tree produced by LCCParser#closeBraces.
    def enterCloseBraces(self, ctx:LCCParser.CloseBracesContext):
        pass

    # Exit a parse tree produced by LCCParser#closeBraces.
    def exitCloseBraces(self, ctx:LCCParser.CloseBracesContext):
        pass


    # Enter a parse tree produced by LCCParser#openBrackets.
    def enterOpenBrackets(self, ctx:LCCParser.OpenBracketsContext):
        pass

    # Exit a parse tree produced by LCCParser#openBrackets.
    def exitOpenBrackets(self, ctx:LCCParser.OpenBracketsContext):
        pass


    # Enter a parse tree produced by LCCParser#closeBrackets.
    def enterCloseBrackets(self, ctx:LCCParser.CloseBracketsContext):
        pass

    # Exit a parse tree produced by LCCParser#closeBrackets.
    def exitCloseBrackets(self, ctx:LCCParser.CloseBracketsContext):
        pass


    # Enter a parse tree produced by LCCParser#comma.
    def enterComma(self, ctx:LCCParser.CommaContext):
        pass

    # Exit a parse tree produced by LCCParser#comma.
    def exitComma(self, ctx:LCCParser.CommaContext):
        pass


    # Enter a parse tree produced by LCCParser#semicolon.
    def enterSemicolon(self, ctx:LCCParser.SemicolonContext):
        pass

    # Exit a parse tree produced by LCCParser#semicolon.
    def exitSemicolon(self, ctx:LCCParser.SemicolonContext):
        pass


    # Enter a parse tree produced by LCCParser#assignment.
    def enterAssignment(self, ctx:LCCParser.AssignmentContext):
        pass

    # Exit a parse tree produced by LCCParser#assignment.
    def exitAssignment(self, ctx:LCCParser.AssignmentContext):
        pass


    # Enter a parse tree produced by LCCParser#plus.
    def enterPlus(self, ctx:LCCParser.PlusContext):
        pass

    # Exit a parse tree produced by LCCParser#plus.
    def exitPlus(self, ctx:LCCParser.PlusContext):
        pass


    # Enter a parse tree produced by LCCParser#minus.
    def enterMinus(self, ctx:LCCParser.MinusContext):
        pass

    # Exit a parse tree produced by LCCParser#minus.
    def exitMinus(self, ctx:LCCParser.MinusContext):
        pass


    # Enter a parse tree produced by LCCParser#multiply.
    def enterMultiply(self, ctx:LCCParser.MultiplyContext):
        pass

    # Exit a parse tree produced by LCCParser#multiply.
    def exitMultiply(self, ctx:LCCParser.MultiplyContext):
        pass


    # Enter a parse tree produced by LCCParser#divide.
    def enterDivide(self, ctx:LCCParser.DivideContext):
        pass

    # Exit a parse tree produced by LCCParser#divide.
    def exitDivide(self, ctx:LCCParser.DivideContext):
        pass


    # Enter a parse tree produced by LCCParser#percent.
    def enterPercent(self, ctx:LCCParser.PercentContext):
        pass

    # Exit a parse tree produced by LCCParser#percent.
    def exitPercent(self, ctx:LCCParser.PercentContext):
        pass


    # Enter a parse tree produced by LCCParser#lessThan.
    def enterLessThan(self, ctx:LCCParser.LessThanContext):
        pass

    # Exit a parse tree produced by LCCParser#lessThan.
    def exitLessThan(self, ctx:LCCParser.LessThanContext):
        pass


    # Enter a parse tree produced by LCCParser#greatherThan.
    def enterGreatherThan(self, ctx:LCCParser.GreatherThanContext):
        pass

    # Exit a parse tree produced by LCCParser#greatherThan.
    def exitGreatherThan(self, ctx:LCCParser.GreatherThanContext):
        pass


    # Enter a parse tree produced by LCCParser#lessThanOrEqual.
    def enterLessThanOrEqual(self, ctx:LCCParser.LessThanOrEqualContext):
        pass

    # Exit a parse tree produced by LCCParser#lessThanOrEqual.
    def exitLessThanOrEqual(self, ctx:LCCParser.LessThanOrEqualContext):
        pass


    # Enter a parse tree produced by LCCParser#greatherThanOrEqual.
    def enterGreatherThanOrEqual(self, ctx:LCCParser.GreatherThanOrEqualContext):
        pass

    # Exit a parse tree produced by LCCParser#greatherThanOrEqual.
    def exitGreatherThanOrEqual(self, ctx:LCCParser.GreatherThanOrEqualContext):
        pass


    # Enter a parse tree produced by LCCParser#equal.
    def enterEqual(self, ctx:LCCParser.EqualContext):
        pass

    # Exit a parse tree produced by LCCParser#equal.
    def exitEqual(self, ctx:LCCParser.EqualContext):
        pass


    # Enter a parse tree produced by LCCParser#different.
    def enterDifferent(self, ctx:LCCParser.DifferentContext):
        pass

    # Exit a parse tree produced by LCCParser#different.
    def exitDifferent(self, ctx:LCCParser.DifferentContext):
        pass



del LCCParser