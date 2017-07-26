#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

//This was a hard challange and was fun to solve. Link for challenge is:
// https://www.hackerrank.com/challenges/crush

int main() {
    long int N, K;
    long int firstIndex, secondIndex, valueToAdd;
    long int max = 0, sum = 0;
    
    cin >> N >> K;
    
    long int *array = new long int[N+1]();
    
    for(int i = 0; i < K; i++){
    	cin >> firstIndex >> secondIndex >> valueToAdd;
    	
    	array[firstIndex] += valueToAdd;
    	if(secondIndex + 1 <= N) array[secondIndex + 1] -= valueToAdd; 
	}
	
	for(int i = 1; i <= N; i++){
		sum += array[i];
		if(max < sum) max = sum;
	}
	
	cout << max;
	    
	return 0;
	
}
