#include "bits/stdc++.h"
using namespace std;
class ai
{
    public: 
        int a;
        int b;
    bool operator<(ai other) const
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
	//cout<<"\nchecking for a=10 "<<q1.find(&ob4).a<<"\n";
	
	cout<<"the original array is \n";
   // vector<pair<int,int> >::iterator it;    
    while(!q1.empty())
    {
        
        cout<<q1.top().a<<" "<<q1.top().b<<"\n";
        q1.pop();
    }
    v1.push_back(0);
    v1.push_back(1);
    v1.push_back(2);
    v1.push_back(3);
    vector<int> v2;
    v2.push_back(0);
    v2.push_back(1);
    v2.push_back(2);
    v2.push_back(3);
    sort(v1.begin(),v1.end());
    unordered_map<vector<int>,int> m1;
    m1[v1]=10;
    
    cout<<"v1==v2 "<<m1[v1]<<"\n";
    
    
	return 0;
}
