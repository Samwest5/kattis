#include <unordered_set>
#include <iostream>

using namespace std;

int main(){
  int cd;
  int jackN;
  int jillN;
  cin >> jackN;
  cin >> jillN;
  while(jackN > 0 || jillN > 0){
    unordered_set<int>set;
    for(int i = 0; i < jackN; i++){
      cin >> cd;
      set.insert(cd);
    }
    int count = 0;
    for(int i = 0; i < jillN; i++){
      cin >> cd;
      if(set.count(cd)) count += 1;
      
    }
    cout << count << endl;
    cin >> jackN;
    cin >> jillN;
  }
}
