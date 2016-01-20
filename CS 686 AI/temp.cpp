#include "bits/stdc++.h"
using namespace std;
bool compare(const pair<int,int> v1, const pair<int,int> v2)
{
  
    return v1.second<v2.second;
}
int main()
{
	vector<pair<int,int> > v1;
	for(int i=1;i<10;i++)
	{
	    v1.push_back(make_pair(i,10-i));
	}
	cout<<"the original array is \n";
    vector<pair<int,int> >::iterator it;
    for(it=v1.begin();it!=v1.end();it++)
    {
        cout<<(*it).first<<" "<<(*it).second<<"\n";
    }
    sort(v1.begin(),v1.end(),compare);
    cout<<"the sorted array is\n";
    for(it=v1.begin();it!=v1.end();it++)
    {
        cout<<(it->first)<<" "<<(it->second)<<"\n";
    }
	return 0;
}
