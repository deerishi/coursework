#include "bits/stdc++.h"
using namespace std;
  
int originalGraph[40][40],minimumSpanningTree[40][40];
int adjacencyMatrixForMinimumSpanningTree[40][40];
bool visited[40];
int parentsMinimumSpanningTree[40];
int verticesMinimumSpanningTree[40];
unordered_map<string,int> mstMap;

//Each time we update the vertices , we update their parents too

class Node
{
    public:
        int citynum;
        string pathSoFar;
        int citiesNotVisited;
        char name;
        int cost;
        vector<int> citiesLeft;
        bool operator <(Node  other) const
        {
            return  this->cost > other.cost;
        }
        
        Node(int citynum,string pathSoFar,int citiesNotVisited,char name,int cost,vector<int> citiesLeft)
        {
            this->citynum=citynum;
            this->pathSoFar+=pathSoFar;
            this->citiesLeft=citiesLeft;
            this->cost=cost;
            this->name=name;
            this->citiesLeft=citiesLeft;
        }
        
    
}City[50000];
int nodeTrack=0;

priority_queue<Node> astar;
class TSP 
{
    public:
    
     char node[3];
     int points[40][2],numCities;
     //TSP(int i,int j) : x(i),y(j){}
     
     void inputData()
     {
        
        scanf("%d",&numCities);
        int i=0;
        getc_unlocked(stdin);
        //double distance;
        while(i<numCities)
        {
            scanf("%s%d%d ",node,&points[i][0],&points[i][1]);
            i++;
        }
        cout<<"n the data entered is \n";
        for(i=0;i<numCities;i++)
        {
            cout<<"x= "<<points[i][0]<<" n y= "<<points[i][1]<<" i= "<<i<<"\n";
        }
        
        
     }
     
     int CalculateDistance(int x1,int y1,int x2,int y2)
     {
        return int(sqrt(pow(x1-x2,2)+pow(y1-y2,2)));
     }
     void createOriginalDistanceGraph()
     {
        int i,j;
        for(i=0;i<numCities;i++)
        {
            originalGraph[i][i]=0;
            adjacencyMatrixForMinimumSpanningTree[i][i]=0;
            for(j=i+1;j<numCities;j++)
            {
                originalGraph[i][j]=CalculateDistance(points[i][0],points[i][1],points[j][0],points[j][1]);
                originalGraph[j][i]=originalGraph[i][j];
                // This is a Symmetric TSP
                adjacencyMatrixForMinimumSpanningTree[i][j]=0;
                adjacencyMatrixForMinimumSpanningTree[j][i]=0;
                minimumSpanningTree[i][j]=INT_MAX;
                minimumSpanningTree[j][i]=INT_MAX;
            }
        }
        
        cout<<"the original matrix is \n";
        for(i=0;i<(this->numCities);i++)
        {
            for(j=0;j<(this->numCities);j++)
            {
                cout<<originalGraph[i][j]<<" ";
            }
            cout<<"\n";
        }
     }
     
     
};

int distance(int city1,int city2)
{
    return originalGraph[city1][city2];
}

int findMinimumVertex(int numOfCities)
{
    int i;
    int minValue=INT_MAX,minIndex;
    
    for(i=0;i<numOfCities;i++)
    {
        if(visited[i]==true)
        {
            continue;
        }
        if(verticesMinimumSpanningTree[i]<minValue)
        {
            minValue=verticesMinimumSpanningTree[i];
            minIndex=i;
        }
        
    }
    return minIndex;
}

int updateAdjacentWeights(int addedVertex,int numOfCities)
{
    int i;
    for(i=0;i<numOfCities;i++)
    {
        if(originalGraph[addedVertex][i]<verticesMinimumSpanningTree[i] and visited[i]==false)
        {
            //Now we update that adjacent edge and also we update the parents of the adjacent edge to the addedVertex
            //cout<<"updating for i= "<<i<<" with "<<originalGraph[addedVertex][i]<<"\n";
            verticesMinimumSpanningTree[i]=originalGraph[addedVertex][i];
            parentsMinimumSpanningTree[i]=addedVertex;
        }
    }
}


int buildMinimumSpanningTree2(vector<int> vertices,vector<char> nodesLeft)
{
    int size=vertices.size();
    if(size==1)
    {
        return 0;
    }
    
    
    int pcity[40],pdist[40],minDistance=INT_MAX;
    vector<int>::iterator it1;
    vector<char>::iterator it2;
    int i=0;
    string cities;
    sort(nodesLeft.begin(),nodesLeft.end());
    for(it1=vertices.begin(),it2=nodesLeft.begin();it1!=vertices.end(),it2!=nodesLeft.end();it1++,it2++)
    {
        pcity[i]=*it1; //parent city 
        pdist[i]=INT_MAX; //parent distance;
        i++;
        cities+=*it2;
    }
    
    unordered_map<string,int>:: iterator mit;//iterator for the hash map for the MST
    //So that we don't have to calculate the MST length again and again for each path.
    mit=mstMap.find(cities);
    if(mit!=mstMap.end())
    {
        return mit->second;
    }
    
    int newCity=pcity[size-1];//i.e we are making the last city as the newCity for finding the MST
    int thisDistance;
    int length=0,minIndex;
    for(int m=size-1;m>0;m--)
    {
        minDistance=INT_MAX;
        for(int j=0;j<m;j++)
        {
            thisDistance=distance(pcity[j],newCity);
            //cout<<"newCity is "<<newCity<<" j = "<<j<<" and their distance is "<<thisDistance<<"\n";
            if(thisDistance < pdist[j]) pdist[j]=thisDistance;
            if(pdist[j]<minDistance) minDistance=pdist[j],minIndex=j;
        }
        newCity=pcity[minIndex];
        length+=minDistance;
        //cout<<"length right now  is "<<length<<"\n";
        pcity[minIndex]=pcity[m-1];
        pdist[minIndex]=pdist[m-1];   
    }
    mstMap[cities]=length;
    return length;
    
}

int calculateHeuristic(vector<int> vertices,vector<char> nodesLeft,int currentCityForExpansion)
{
    int size=vertices.size();
    if(size==1)
    {
        return 0;
    }
    
    
    int pcity[40],pdist[40],minDistance=INT_MAX;
    vector<int>::iterator it1;
    vector<char>::iterator it2;
    int i=0;
    string cities;
    sort(nodesLeft.begin(),nodesLeft.end());
    for(it1=vertices.begin();it1!=vertices.end();it1++)
    {
        pcity[i]=*it1; //parent city 
        pdist[i]=INT_MAX; //parent distance;
        i++;
    }
    int mst=buildMinimumSpanningTree2(vertices,nodesLeft);
    int nearestUnvisitedCityDistance=INT_MAX,nearestToSource=INT_MAX,thisDistance1,thisDistance2;
    for(i=0;i<size;i++)
    {
        thisDistance1=distance(pcity[i],currentCityForExpansion);// this is the distancefrom the unvisited city to the currentCityForExpansion
        thisDistance2=distance(pcity[i],0); //this is the distance from the source
        if(thisDistance1<nearestUnvisitedCityDistance) nearestUnvisitedCityDistance=thisDistance1;
        
        if(thisDistance2<nearestToSource) nearestToSource=thisDistance2;
        
    }
    int hn=mst+nearestToSource+nearestUnvisitedCityDistance;
    return hn;
}


int buildMinimumSpanningTree(TSP problem) //change to only nodes in the graph
{
    int i,j;

    //
    
    
    for(i=0;i<problem.numCities;i++)
    {
        visited[i]=false;
        verticesMinimumSpanningTree[i]=INT_MAX;
    }
    verticesMinimumSpanningTree[0]=0;
    parentsMinimumSpanningTree[0]=-1;
    int numVertices=0;
    
    int current=0,next;

    
    
    int minVal,minIndex;
    while(numVertices<problem.numCities)
    {
        //1) find the minimum vertex
        next=findMinimumVertex(problem.numCities);
        //cout<<"next is "<<next<<"\n";
        //2)add that vertex to the he MST and update its weights
        visited[next]=true;
        updateAdjacentWeights( next,problem.numCities);
        numVertices++;
    }
    //3)Now we can build the adjacency matrix for the MST we just built
    for(i=1;i<problem.numCities;i++)
    {
        adjacencyMatrixForMinimumSpanningTree[i][parentsMinimumSpanningTree[i]]=1;
        adjacencyMatrixForMinimumSpanningTree[parentsMinimumSpanningTree[i]][i]=1; 
        minimumSpanningTree[i][parentsMinimumSpanningTree[i]]=originalGraph[i][parentsMinimumSpanningTree[i]];
        minimumSpanningTree[parentsMinimumSpanningTree[i]][i]=originalGraph[i][parentsMinimumSpanningTree[i]];       
    }
        
        
    
    
    cout<<" the adjacency matrix for the minimum spanning tree looks like \n";
    for(i=0;i<problem.numCities;i++)
    {
        for(j=0;j<problem.numCities;j++)
        {
            cout<<adjacencyMatrixForMinimumSpanningTree[i][j]<<" ";
        }
        cout<<"\n";
    }
    
    cout<<" the minimum spanning tree looks like \n";
    
    for(i=0;i<problem.numCities;i++)
    {
        for(j=0;j<problem.numCities;j++)
        {
            if(minimumSpanningTree[i][j]==INT_MAX)
            {
                cout<<"X ";
                continue;
            
            }
               cout<<minimumSpanningTree[i][j]<<" ";
        }
        cout<<"\n";
    }
}

int startSearch()
{
    Node current;
    while(!astar.empty())
    {
        current=astar.top();
        cout<<"current heuristic is "<<current->cost<<"\n";
        astar.pop();
    }
}

int main()
{
    TSP prob1;
    int i;
    prob1.inputData();
    prob1.createOriginalDistanceGraph();// Till now we have the orginal Distance Graph
    int numCities=prob1.numCities;
    buildMinimumSpanningTree(prob1);
    //Now we have the number of cities and the orignal graph
    vector<int> v1;
    vector<char> v2;
    cout<<"now we are finding the MST for the following nodes\n";
    for( i=1;i<numCities;i++)
    {
        v1.push_back(i);
        if(i>25)
        {
            v2.push_back('a'+i-26);
        }
        else
        {
            v2.push_back('A'+i);
        }
        cout<<i<<" ";
    }
    vector<char>:: iterator it=v2.begin();
    cout<<"\n v2 is \n";
    for(it=v2.begin();it!=v2.end();it++)
    {
        cout<<*it<<" ";
    }
    int initialHeuristic=calculateHeuristic(v1,v2,0);
    cout<<"initialHeuristic is "<<initialHeuristic<<"\n";
    City[nodeTrack++]= Node(0,"A",numCities-1,'A',initialHeuristic,v1);
    City[nodeTrack++]= Node(0,"AB",numCities-1,'B',initialHeuristic+400,v1);
    astar.push(City[0]);
    astar.push(City[1]);
    startSearch();
    
    int lengthMst = buildMinimumSpanningTree2(v1,v2);
    cout<<"\n the length of the MST is "<<lengthMst<<"\n";
    return 0;   
}
     
     
     

