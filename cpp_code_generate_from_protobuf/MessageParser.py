import FindMessageContent
from common_def import *

def ParseEveryMessageStruct(allMessages):
    """This function is to parse all the messages in the proto file, call the ParseEveryMessage to deal\
     with one message every time.\
     allMessages: all messages list in the proto file, every Message is one item in the list"""
    all_messages = allMessages
    every_message_members = []
    for every_message in allMessages:
        every_message_members.append(ParseEveryMessage(every_message))
    return every_message_members
        
def ParseEveryMessage(message):
    members_in_message = []
    for line in message:
        line = line.strip()
        if line.startswith("required") or line.startswith("repeated"):
            members_in_message.append(line)
        if line.startswith("start local message"):
            local_message
    print members_in_message
    return members_in_message

def GetEveryMemberFuncName(member_name, dotHorCpp, class_name):
    class_member_function_name = []
    class_name = class_name.split('\n')[0]  #get rid of the '\n'
    if dotHorCpp == "dotH": 
        set_function_name = PrefixSetFunctionForDotH() + member_name + EndSetFuncDeclara("dotH");
        get_function_name = PrefixGetFunctionForDotH() + member_name + EndGetFuncDeclara("dotH");
        class_member_function_name.append(set_function_name)
        class_member_function_name.append(get_function_name)
    else:
        set_function_name = PrefixSetFunctionForDotCpp(class_name) + member_name + EndSetFuncDeclara("dotCpp")
        set_function_content = SetFunctionContentForCpp(member_name)
        get_function_name = PrefixGetFunctionForDotCpp(class_name) + member_name + EndGetFuncDeclara("dotCpp")
        get_function_content = GetFunctionContentForCpp(member_name)

        class_member_function_name.append(set_function_name + set_function_content + RCurlyBraket() + NextLine()*2)
        class_member_function_name.append(get_function_name + get_function_content +RCurlyBraket() + NextLine()*2)
    return class_member_function_name

def GetEveryClassMemberFunction(WhichMessage, dotHorCpp, class_name):
    if dotHorCpp == "dotH":
        every_class_members = ParseEveryMessageStruct(FindMessageContent.GetAllMessages())
        class_member_funciton_name = []
        for member in every_class_members[WhichMessage]:
            member_name = member.split(" ")[2];
            #generate the function name based the member in the message struct
            class_member_funciton_name.append(GetEveryMemberFuncName(member_name, "dotH", class_name)) 

    else:
        every_class_members = ParseEveryMessageStruct(FindMessageContent.GetAllMessages())
        class_member_funciton_name = []
        for member in every_class_members[WhichMessage]:
            member_name = member.split(" ")[2];
            class_member_funciton_name.append(GetEveryMemberFuncName(member_name, "dotCpp", class_name)) 
    return class_member_funciton_name



        
    
