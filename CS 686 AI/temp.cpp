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
	vector<string>  v1;
	MyQueue<ai> q1;
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
    v1.push_back("a");
    v1.push_back("B");
    v1.push_back("A");
    v1.push_back("b");
    vector<s
    sort(v1.begin(),v1.end());
    vector<string> v2;
    v2=v1;
    cout<<"the next array is \n";
    vector<string>::iterator it;
    for(it=v2.begin();it!=v2.end();it++)
    {
        cout<<"it is "<<(*it)<<"\n";
    }  
	return 0;
}
