#include <iostream>
using namespace std;


int main() {
string data;
int count = 0;


cout << "Enter binary data: ";
cin >> data;


cout << "Stuffed Data: ";


for (int i = 0; i < data.length(); i++) {
if (data[i] == '1') {
count++;
cout << '1';
if (count == 5) {
cout << '0';
count = 0;
}
} else {
cout << '0';
count = 0;
}
}
return 0;
}
