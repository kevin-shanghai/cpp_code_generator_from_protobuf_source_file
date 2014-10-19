#This project is used to generate the cpp class header and source file from the specific protobuf source file

example:
1. the protobuf source file "flatpanel.h" is as following:
message A
{
    required int32 deviceid = 1;  //device id
    required int32 kevin = 2; //motion enable
    repeated int32 test = 3;
}


and run the test.py, that will generate two files according to the protobuf
source file name, one is cpp file "flatpanel.cpp" and the other is the header file "flatpanel.h"l. and the content for the two file is somewhat like this:

flatpanel.h
___________________________________________
#ifndef __H_FLATPANEL__H
#define __H_FLATPANEL__H
class A
{
public:
	A();

	~A();
public:
	void set_deviceid(int32_t value);

	int32_t get_deviceid(void);

	void set_kevin(int32_t value);

	int32_t get_kevin(void);

	void set_test(int32_t value);

	int32_t get_test(void);


};


"flatpanel.cpp"
___________________________________________
void A::set_deviceid(int32_t value)
{
	deviceid = value;
}

int32_t A::get_deviceid(void)
{
	return deviceid;
}

void A::set_kevin(int32_t value)
{
	kevin = value;
}

int32_t A::get_kevin(void)
{
	return kevin;
}

void A::set_test(int32_t value)
{
	test = value;
}

int32_t A::get_test(void)
{
	return test;
}

