#include "bits/stdc++.h"
using namespace std;

class ai
{
    public: 
        int a;
        int b;
    bool operator <(ai other) const
    {
        return this->b > other.b;
    }

   
};


bool compare( ai v1,  ai v2)
{
  
    return v1.b<v2.b;
}
#include <queue>


int main()
{
	vector<int>  v1;
	priority_queue<ai> q1;
	ai ob1,ob2,ob3,ob;
	ob1.a=1;
	ob1.b=5;
	ob2.a=10;
	ob2.b=12;
	ob3.a=13;
	ob3.b=1;
	q1.push(ob1);
	q1.push(ob2);
	q1.push(ob3);
	ai ob4;
	ob4.a=10;
    priority_queue<char> q2;
    q2.push('A');
    q2.push('a');
    q2.push('B');
	
	cout<<"the original array is \n";

    while(!q2.empty())
    {
        cout<<" "<<q2.top()<<"\n";
        q2.pop();
    }
    
    sort(v1.begin(),v1.end());
    //unordered_map<vector<int>,int,container_hash<vector<int> >> m1;
    //m1[v1]=10;
    
    //cout<<"v1==v2 "<<m1[v1]<<"\n";
    
    
	return 0;
}   // vector<pair<int,int> >::iterator it;    
