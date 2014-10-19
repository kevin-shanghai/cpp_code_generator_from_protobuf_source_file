import FindMessageContent
import MessageParser
from common_def import *

##Following code is for parse the global enum and it's specific line numbers
def GlobalEnumStartAndEndLineNumber():
	""" This function is to get the start line and the end line number for every global enum,\
	Note: every global enum must start with "start global enum ..." and end with\
	"end with global enum..." """
	file_content = FindMessageContent.FileContentAndLineNumber()
	global_enum_start_line_number = []
	global_enum_end_line_number = []
	enum_start_prefix = GlobalEnumStartPrefix()
	enum_end_prefix = GlobalEnumEndPrefix()
	for key in file_content:
		if file_content[key].startswith(enum_start_prefix):
			global_enum_start_line_number.append(key + 1)
		if file_content[key].startswith(enum_end_prefix):
			global_enum_end_line_number.append(key - 1)
	assert len(global_enum_start_line_number) == len(global_enum_end_line_number)
	#print  global_enum_start_line_number, global_enum_end_line_number
	return global_enum_start_line_number, global_enum_end_line_number

def GetAllGlobalEnums():
	""" This funciton is to get the content for every global enums"""
	enum_start_line_numer, enum_end_line_number = GlobalEnumStartAndEndLineNumber()
	single_global_enum_content = []
	total_global_enum_content = {}
	linenum_linecontent_dic = FindMessageContent.FileContentAndLineNumber()
	AllGlobalEnumName = GetAllGlobalEnumName()
	for i in range(GetHowManyGlobalEnums()): 
		for j in range(enum_start_line_numer[i] , enum_end_line_number[i]): 
			enum_line_content = linenum_linecontent_dic[j]
			single_global_enum_content.append(enum_line_content)
		total_global_enum_content[AllGlobalEnumName[i]] = single_global_enum_content
		single_global_enum_content = []
	#print total_global_enum_content
	return total_global_enum_content

def GetAllGlobalEnumAndMembers():
	total_global_enum_content = GetAllGlobalEnums()
	single_global_enum_members = []
	totoal_global_enum_name_members = {}
	for key in total_global_enum_content:
		for members in total_global_enum_content[key]:
			if Equal() not in members:
				pass
			else:
				members = members.strip()
				single_global_enum_members.append(members.split("=")[0].strip())
				totoal_global_enum_name_members[key] = single_global_enum_members
		single_global_enum_members = []
	print totoal_global_enum_name_members
	return totoal_global_enum_name_members


def GetHowManyGlobalEnums():
	return len(GetAllGlobalEnumName())

def GetAllGlobalEnumName():
	file_content = FindMessageContent.FileContentAndLineNumber()
	enum_start_line_numer, enum_end_line_number = GlobalEnumStartAndEndLineNumber()
	AllGlobalEnumName = []
	for i in enum_start_line_numer:
		if file_content[i].startswith("enum"):
			global_enum_name = file_content[i].split(" ")[1].split("\n")[0];
			AllGlobalEnumName.append(global_enum_name)
	print AllGlobalEnumName
	return AllGlobalEnumName

###Following is for parse the local enums for every messages####
def FindAllLocalEnums(allMessages):
    """This function is to parse all the messages in the proto file, call the ParseEveryMessage to deal\
     with one message every time.\
     allMessages: all messages list in the proto file, every Message is one item in the list"""
    all_messages = allMessages
    all_message_enum_and_members = []
    for every_message in allMessages:
        all_message_enum_and_members.append(GetEveryMessageLocalEnums(every_message))
    return all_message_enum_and_members

def GetEveryMessageLocalEnums(message):
	all_global_enum_names = GetAllGlobalEnumName()
	enum_name_sequence_in_message = []
	for i in range(len(message)):
		enum_name_line = []
		line = message[i].strip()
		if line.startswith("enum"):
			enum_name = line.split(" ")[1]
			if enum_name not in all_global_enum_names:
				enum_name_line.append(i)
				enum_name_line.append(enum_name)
				enum_name_sequence_in_message.append(enum_name_line)
			else:
				pass
		if (line.startswith("required") or\
			line.startswith("repeated") or\
			line.startswith("optional") ) and\
			len(enum_name_sequence_in_message) != 0:
			last_local_enum_line = i
			enum_name_sequence_in_message.append([last_local_enum_line, "local_enum_end_line"])
			break
	return enum_name_sequence_in_message

def GetLocalEnumAndMembersAllMessage(allmessages):
	all_message_local_enum_lines = FindAllLocalEnums(allmessages)
	#all_message_names = GetAllMessageName()
	all_message_local_enum_members = []
	which_message = -1
	for every_message_enum_name_line_list in all_message_local_enum_lines:
		which_message += 1
		single_message_local_enum_members = []
		if len(every_message_enum_name_line_list):
			for i in range(len(every_message_enum_name_line_list)-1):
				single_message_every_local_enum_members = []
				start_line = every_message_enum_name_line_list[i][0]
				end_line = every_message_enum_name_line_list[i+1][0]
				for line in range(start_line, end_line):
					line_in_whichMessage = allmessages[which_message][line]
					if "=" in line_in_whichMessage:
						member = line_in_whichMessage.strip().split(" ")[0]
						single_message_every_local_enum_members.append(member)
					else:
						pass
				single_message_local_enum_members.append(single_message_every_local_enum_members)
		else:
			pass
		all_message_local_enum_members.append(single_message_local_enum_members)	
	return all_message_local_enum_members
					
		

def GetHowManyLocalEnumsInOneMessage(message):
	print len(ParseEveryMessageLocalEnums())
	return len(ParseEveryMessageLocalEnums())




