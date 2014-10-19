from common_def import *
import MessageParser
import FindMessageContent

def GetDotHFilePointer():
    dotH = file(GetDotHFileName(), "w")
    return dotH

def GetDotHFileName():
    proto_filename = FindMessageContent.GetProtoFileName()
    return proto_filename.split(".")[0] + DotHExtender()

def GetDotHFileHeader():
    proto_filename = FindMessageContent.GetProtoFileName()
    proto = proto_filename.split(".")[0]
    header_first = proto.upper() + "__H" +"\n"
    header = "#ifndef __H_" + header_first + \
             "#define __H_" + header_first 
    return header

def GetDotHFileEnder():
    return "#endif"

def GetEveryClassHeader(allMessageName):
    class_header = []
    for name in allMessageName:
        header = "class " + name  + "{"
        class_header.append(header)
    return class_header

def GetEveryClassCtor(allMessageName):
    class_ctor = []
    for name in allMessageName:
        class_name = name.split('\n')[0]
        class_ctor.append(Tab() + class_name + RoundBraket() + Semicolon() + NextLine())
    return class_ctor

def GetEveryClassDtor(allMessageName):
    class_dtor = []
    for name in allMessageName:
        class_name = name.split('\n')[0]
        class_dtor.append(Tab() + DtorStart() + class_name + RoundBraket() + Semicolon() + NextLine())
    return class_dtor


def WriteInDotHFile(str, dotH):
    dotH.write(str)
    
def WriteMemberFunctionInDotHFile(class_member_list, dotH):
    for every_member_function in range(len(class_member_list)):
        for line in class_member_list[every_member_function]:
            WriteInDotHFile(line, dotH)
    
def WriteEveryClassInDotHFile(allMessageName, dotHPointer):
    all_class_header = GetEveryClassHeader(allMessageName)
    all_class_ctor = GetEveryClassCtor(allMessageName)
    all_class_dtor = GetEveryClassDtor(allMessageName)
    for i in range(len(allMessageName)):
        #dotHPointer.write(all_class_header[i] + NextLine() + PublicDeclaration() + \
                       # NextLine() + all_class_ctor[i] + NextLine() + all_class_dtor[i])
        every_class_member_function_name = MessageParser.GetEveryClassMemberFunction(i, "dotH", allMessageName[i])
        #dotHPointer.write(every_class_member_function_name)
        WriteInDotHFile(all_class_header[i] + NextLine() + PublicDeclaration() + \
                        all_class_ctor[i] + NextLine() + all_class_dtor[i] + PublicDeclaration(), dotHPointer)
        WriteMemberFunctionInDotHFile(every_class_member_function_name, dotHPointer)
        WriteInDotHFile(NextLine() + ClassEnder() + NextLine(), dotHPointer)
  
def GetEveryClassInDotH():
    pass


def WriteDotHHeader(dotHPointer):
    WriteInDotHFile(GetDotHFileHeader(), dotHPointer)

def WriteDotHEnder(dotHPointer):
    WriteInDotHFile(GetDotHFileEnder(), dotHPointer)

def GenerateDotHFile():
    dotH = GetDotHFilePointer()
    WriteDotHHeader(dotH)
    WriteEveryClassInDotHFile(FindMessageContent.GetAllMessageName(), dotH)
    WriteDotHEnder(dotH)