#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#define TrainSize 1000
using namespace std;
int main(int argc, char *argv[])
{
	string K;
	while(1){
		if(!(argc<2)){
			K=(argv[1]);
			break;
		}
		else{
			cout<<"Sorry Please drag and drop the file you want to call into this program\n";
			cin.get();
			return -1;
		}
	}
	ofstream output("aa.srt",ios::trunc|ios::out);
	ifstream input(argv[1],ios::in);
	char a[TrainSize];
	while(!input.eof()){
		input.getline(a,TrainSize);
		output<<a<<endl;
	}
	input.close();
	output.close();
	system("runProgram.exe");
	cin.get();
	return 0;
}
