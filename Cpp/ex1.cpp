#include<unordered_map>
#include<vector>
#include<stack>
#include <iostream>

using namespace std;


vector<int> solution(vector<int> &T) {
//   struct Results res;
//   int * A = (int*)malloc(sizeof(int)*(M-1));
//   res.A = A;
//   res.N = M-1;
    int M = T.size(); 
    vector<int> A(M-1, 0); 
  vector<int> map[M];
  int capital = -1;

  for (int i = 0; i < M; ++i) {
    if (T[i] == i) capital = i;
    else {
	  int q = T[i];
	  map[q].push_back(i);
    }
  }
  
  if (capital == -1) {
    cout << "Cannot find the capital";
  }

  //cout << capital << endl;

  stack<int> mystack;
  mystack.push(capital);
  for (int i = 0; i < M-1; ++i) {
    A[i] = 0;
  }
	
  int distances[M];
  for (int i = 0; i < M; ++i) {
    distances[i] = 0;
  }

  while (!mystack.empty()) {
    int x = mystack.top();
    mystack.pop();
    vector<int> v = map[x];
    // cout << "Map " << x << endl;
    for (vector<int>::iterator it = v.begin(); it != v.end(); ++it) {
    //   cout << *it << endl;
      distances[*it] = distances[x]+1;
      mystack.push(*it);
    }
  }
  for (int i = 0; i < M; ++i) {
    A[distances[i]-1]++;
  }

  return A; 
}

int main() {
  int arr[] = {9, 1 , 4, 9, 0, 4, 8, 9, 0, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
 
    vector<int> T(arr, arr + n);

  vector<int> result = solution(T);

  for (int i = 0; i < result.size(); ++i) {
    cout << result[i] << endl;
  }

  return 0;
}
