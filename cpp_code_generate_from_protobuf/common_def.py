
def NextLine():
    return "\n"

def LCurlyBraket():
    return "{"

def RCurlyBraket():
    return "}"

def Semicolon():
    return ";"

def LRoundBraket():
    return "("

def RRoundBraket():
    return ")"

def RoundBraket():
    return "()"

def Tab():
    return "\t"

def DtorStart():
    return "~"

def Equal():
    return "="

def ClassEnder():
    return RCurlyBraket() + Semicolon() + NextLine()

def ClassPrefix():
    return "class "

def IntegerType():
    return "int32_t"

def Void():
    return "void"

def ControlName():
    return "::"

def PrefixSetFunctionForDotH():
    return Tab() + Void() + " " + "set_"

def PrefixGetFunctionForDotH():
    return Tab()+ IntegerType() + " " + "get_"

def PrefixSetFunctionForDotCpp(class_name):
    return Void() + " " + class_name + ControlName() + "set_"

def PrefixGetFunctionForDotCpp(class_name):
    return IntegerType() + " " + class_name + ControlName() + "get_"

def EndSetFuncDeclara(dotHorCpp):
    if dotHorCpp == "dotH":
        return LRoundBraket() + IntegerType() + " value" + RRoundBraket() + Semicolon() + NextLine()*2
    else:
        return LRoundBraket() + IntegerType() + " value" + RRoundBraket() + NextLine() + \
               LCurlyBraket() + NextLine() # + RCurlyBraket() + NextLine()*2   

def EndGetFuncDeclara(dotHorCpp):
    if dotHorCpp == "dotH":
        return LRoundBraket() + Void() + RRoundBraket() + Semicolon() + NextLine()*2
    else:
        return LRoundBraket() + Void() + RRoundBraket() + NextLine() + \
        LCurlyBraket() + NextLine() #+ RCurlyBraket() + NextLine()*2
    
def SetFunctionContentForCpp(member_name):
    return Tab() + member_name + " " + Equal() + " value" + Semicolon() + NextLine()

def GetFunctionContentForCpp(member_name):
    return Tab() + "return " + member_name + Semicolon() + NextLine()

def PublicDeclaration():
    return "public:" + NextLine()

def CppExtender():
    return ".cpp"

def DotHExtender():
    return ".h"

def GlobalEnumStartPrefix():
    return "//start global enum"

def GlobalEnumEndPrefix():
    return "//end global enum"

def LocalEnumStartPrefix():
    return "//start local enum"

def LocalEnumEndPrefix():
    return "//end local enum"


