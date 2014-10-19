from common_def import *
import MessageParser
import FindMessageContent


def GetDotCppFilePointer():
    dotCpp = file(GetDotCppFileName(), "w")
    return dotCpp

def GetDotCppFileName():
    proto_filename = FindMessageContent.GetProtoFileName()
    return proto_filename.split(".")[0] + CppExtender()

def GetEveryClassHeader(allMessageName):
    class_header = []
    for name in allMessageName:
        header = ClassPrefix() + name  + LCurlyBraket()
        class_header.append(header)
    return class_header

def GetEveryClassCtor(allMessageName):
    class_ctor = []
    for name in allMessageName:
        class_name = name.split('\n')[0]
        class_ctor.append(class_name + ControlName() + class_name + \
                          RoundBraket() + NextLine() + LCurlyBraket() + NextLine() + RCurlyBraket())
    return class_ctor

def GetEveryClassDtor(allMessageName):
    class_dtor = []
    for name in allMessageName:
        class_name = name.split('\n')[0]
        class_dtor.append(class_name + ControlName() + DtorStart() + class_name +\
                          RoundBraket() + NextLine() + LCurlyBraket() + NextLine() + RCurlyBraket())
    return class_dtor

def WriteInDotCppFile(str1, dotCpp):
    dotCpp.write(str1)    
    
def WriteMemberFunctionInDotCppFile(class_member_list, dotCpp):
    for every_member_function in range(len(class_member_list)):
        for line in class_member_list[every_member_function]:
            WriteInDotCppFile(line, dotCpp)
            
def WriteEveryClassInDotCppFile(allMessageName, dotCppPointer):
    all_class_header = GetEveryClassHeader(allMessageName)
    all_class_ctor = GetEveryClassCtor(allMessageName)
    all_class_dtor = GetEveryClassDtor(allMessageName)
    for i in range(len(allMessageName)):
        #WriteInDotCppFile(all_class_header[i] + NextLine() + PublicDeclaration() + \
                       # all_class_ctor[i] + NextLine() + all_class_dtor[i] + PublicDeclaration(), dotCppPointer)
        every_class_member_function_name = MessageParser.GetEveryClassMemberFunction(i, "dotCpp", allMessageName[i])
        WriteMemberFunctionInDotCppFile(every_class_member_function_name, dotCppPointer)
        #WriteInDotCppFile(NextLine() + ClassEnder() + NextLine(), dotCppPointer)
            

def GenerateDotCppFile():
    dotCpp = GetDotCppFilePointer()
    WriteEveryClassInDotCppFile(FindMessageContent.GetAllMessageName(), dotCpp)