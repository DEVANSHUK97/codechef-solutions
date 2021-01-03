#include<iostream>
using namespace std;
int main(){
  int t;
  cin >> t;
  while(t--){
    int n, k, d;
    cin >>n >> k >>d;
    int sum = 0;
    int x;
    while(n--){
      cin>>x;
      sum += x;
    }
    cout<<min(d,sum/k)<<endl;
  }
  return 0;
}
