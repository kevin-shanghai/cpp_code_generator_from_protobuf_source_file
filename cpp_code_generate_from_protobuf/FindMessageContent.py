###global names for the file content and line number###
linenum_linecontent_dic = {}

def GetProtoFileName():
	return "FlatPanel.proto"

def GetProtoFilePointer():
	f = file(GetProtoFileName(), "r")
	return f

def GetMessageNumbers():
	return len(LineNumberMessageAt())

def LineNumberMessageAt():
	file_content = FileContentAndLineNumber()
	message_at_line_number = []
	for key in file_content:
		if file_content[key].startswith("message"):
			message_at_line_number.append(key)
	return message_at_line_number

def  FileContentAndLineNumber():
	global linenum_linecontent_dic
	for (line_num, line_content) in enumerate(GetProtoFilePointer()):
		linenum_linecontent_dic[line_num] = line_content
	return linenum_linecontent_dic

def GetLastLineNumber():
	return len(FileContentAndLineNumber())

def GetAllMessages():
	message_at_line = LineNumberMessageAt()
	message_at_line.append(GetLastLineNumber())
	how_many_messages = GetMessageNumbers()
	message_content = []
	single_message_content = []
	linenum_linecontent_dic = FileContentAndLineNumber()
	for i in range(how_many_messages): 
		for j in range(message_at_line[i] , message_at_line[i+1]): 
			message_line = linenum_linecontent_dic[j]
			single_message_content.append(message_line)
		message_content.append(single_message_content)
		single_message_content=[]
	return message_content

def GetAllMessageName():
	file_content = FileContentAndLineNumber()
	all_message_names = []
	for key in file_content:
		if file_content[key].startswith("message"):
			message_name = file_content[key].split(" ")[1]
			all_message_names.append(message_name)
	return all_message_names


	


	

	

			