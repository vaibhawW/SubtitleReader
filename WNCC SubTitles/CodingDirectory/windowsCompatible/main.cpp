//Header declarations
#include <iostream>
#include <string>
#include <string.h>
#include <map>
#include <ctime>
#include <fstream>
#include <windows.h>
using namespace std;

//Define variables globally just to remove complexities
ifstream file("aa.srt");
char arr[100];
string stringTemp;
unsigned long long  sec,secEnd;
map<unsigned long long int, string> cap;
map<int,int> endTime;
map<unsigned long long int,string> subs;

//Made some fucntions for compiling the srt files...

unsigned long long secondsCount(){		//Function used to count start and end time
	file.getline(arr,100,':');
	sec=secEnd=0;
	sec+=stoi(arr)*3600;
	file.getline(arr,100,':');
	sec+=stoi(arr)*60;
	file.getline(arr,100,'>');
	sec+=stoi(arr);
	file.getline(arr,100,':');
	secEnd+=stoi(arr)*3600;
	file.getline(arr,100,':');
	secEnd+=stoi(arr)*60;
	file.getline(arr,100);
	secEnd+=stoi(arr);
	return 0;
}
 
void getString(void){					//Function to get the whole string
	stringTemp="\0";
	while(!file.eof()){
		file.getline(arr,100);
		if(!strlen(arr)) break;
		stringTemp+=arr;
		stringTemp+="\n";
	}
	return;
}
int main(int argc,char** argv){
	cout<<"Compiling srt file please wait...\n";
	//Compilation begins
	while(!file.eof()){
		file.getline(arr,100);
		secondsCount();
		getString();
		cap[sec]=stringTemp;
		endTime[sec]=secEnd;
	}
	auto VV=endTime.begin();
	for(int i=0;i<VV->first;i++) subs[i]="\0";
	for(map<int,int>::iterator i=endTime.begin();i!=endTime.end();i++){
		for(int j=(i->first);j<=(i->second);j++){
			subs[j]+=cap[i->first];
		}
	}
	//compiling done! 
	//Now doing subs :)
	system("CLS");
	cout<<"Ok, now I am all set. Press any key when you are ready :)\n";
	system("pause");
	//Printing started
	time_t initial=time(0);
	for(unsigned long long int i=0;i<secEnd;i++){
		system("cls");
		cout<<subs[i++];
		while(difftime(time(0),initial)<i);
	}
	//All printing done!
	file.close();
	system("cls");
	cout<<"Printing done!\n\n\nThanks for using Vaibhaw's simple product:)\n";
	return 0;
}