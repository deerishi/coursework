#include "bits/stdc++.h"
using namespace std;

int originalGraph[40][40],minimumSpanningTree[40][40];
int adjacencyMatrixForMinimumSpanningTree[40][40];
bool visited[40];
int parentsMinimumSpanningTree[40];
int verticesMinimumSpanningTree[40];

vector<pair<int,int> > extendedList; //node ,path length to it. 

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


int buildMinimumSpanningTree(vertex<int> unvisited)
{
    unvisited.push_back()
}

int main()
{
    TSP prob1;
    prob1.inputData();
    prob1.createOriginalDistanceGraph();
    buildMinimumSpanningTree(prob1);
    return 0;
    
}
     
     
     

