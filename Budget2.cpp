#include<iostream>
#include <math.h>
#include <vector>
#include <stdlib.h>
#include <utility>
#include <map>
using namespace std;


void do_compute(int &ans,int temp,vector<bool> T,vector<vector<int > > &graph,int n,int k,vector<int> &A,vector<int> &B,map<vector<bool>,bool> &mp,int &count)
{
	if(mp.find(T)!=mp.end()) return ;
	if(k<0) return;
	mp[T]=true;
	ans=max(ans,temp);
	if(k==0) return;
	for(int i=0;i<n;i++)
	{
        count+=1;
		if(T[i]==false)
		{

			bool flag=true;
			int ppl=A[i];
			int Bud=B[i];
			vector<bool> temp_T=T;
			temp_T[i]=true;
			for(int j=0;j<graph[i].size();j++)
			{
				ppl+=A[graph[i][j]];
				Bud+=B[graph[i][j]];
				temp_T[graph[i][j]]=true;
				if(T[graph[i][j]]==true || Bud>k)
				{
					flag=false;
					break;
				}

			}
			if(flag)
				do_compute(ans,temp+ppl,temp_T,graph,n,k-Bud,A,B,mp,count);

		}
		
	}
	return;
}
int main()
{
	int n,K;
	cin>>n>>K;
	vector<int> A(n);
	vector<int> B(n);
	for(int i=0;i<n;i++)
		cin>>A[i];

	for(int i=0;i<n;i++)
		cin>>B[i];

	vector<vector<int > > graph(n,vector<int> (0));
	int S;
	cin>>S;
	for(int i=0;i<S;i++)
	{
		int r;
		cin>>r;
		vector<int> arr(r);
		for(int j=0;j<r;j++)
			cin>>arr[j];
		for(int j=0;j<r-1;j++)
			graph[arr[j]-1].push_back(arr[j+1]-1);
	}
	map<vector<bool>,bool> mp;
	vector<bool> T(n,false);
	int ans=0;
	int temp=0;
    int count=0;
	do_compute(ans,temp,T,graph,n,K,A,B,mp,count);
	cout<<ans<<" "<<count<<endl;
	return 0;

}