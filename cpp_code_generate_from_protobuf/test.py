#coding:utf-8

import FindMessageContent
import GenerateDotHFile
import GenerateDotCppFile
import MessageParser
import EnumParser

# print patt.findall(content)
# FindMessageContent.FileContentAndLineNumber()
# FindMessageContent.GetMessageNumbers()
# FindMessageContent.LineNumberMessageAt()
# FindMessageContent.GetAllMessages()

#GenerateDotHFile.GenerateDotHFile()
#GenerateDotCppFile.GenerateDotCppFile()
#EnumParser.GlobalEnumStartAndEndLineNumber()
#EnumParser.GetHowManyGlobalEnums()
#EnumParser.GetAllGlobalEnumName()
#EnumParser.GetAllGlobalEnums()
EnumParser.GetAllGlobalEnumAndMembers()
print FindMessageContent.GetAllMessageName()
print EnumParser.FindAllLocalEnums(FindMessageContent.GetAllMessages())
print EnumParser.GetLocalEnumAndMembersAllMessage(FindMessageContent.GetAllMessages())
