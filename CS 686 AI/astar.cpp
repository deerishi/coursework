#include "bits/stdc++.h"
using namespace std;

int originalGraph[40][40],minimumSpanningTree[40][40];
int adjacencyMatrixForMinimumSpanningTree[40][40];
bool visited[40];
int parentsMinimumSpanningTree[40];
int verticesMinimumSpanningTree[40];
//Each time we update the vertices , we update their parents too
class TSP 
{
    public:
    
     char node;
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
            scanf("%c%d%d ",&node,&points[i][0],&points[i][1]);
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
            cout<<"updating for i= "<<i<<" with "<<originalGraph[addedVertex][i]<<"\n";
            verticesMinimumSpanningTree[i]=originalGraph[addedVertex][i];
            parentsMinimumSpanningTree[i]=addedVertex;
        }
    }
}


int buildMinimumSpanningTree(TSP problem)
{
    int i,j;
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
        cout<<"next is "<<next<<"\n";
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
            cout<<minimumSpanningTree[i][j]<<" ";
        }
        cout<<"\n";
    }
}

int main()
{
    TSP prob1;
    prob1.inputData();
    prob1.createOriginalDistanceGraph();
    buildMinimumSpanningTree(prob1);
    return 0;
    
}
     
     
     

