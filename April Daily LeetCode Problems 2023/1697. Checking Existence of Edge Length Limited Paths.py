class Solution:
    def find(self,p,par):
        if p!=par[p]:par[p]=self.find(par[p],par)
        return par[p]
    def union(self,a,b,par,rank):
        a,b=self.find(a,par),self.find(b,par)
        if a==b:return True
        if rank[a]>rank[b]:
            rank[a]+=1
            par[b]=a
        else:
            rank[b]+=1
            par[a]=b
        return False
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList=sorted([(k,i,j) for i,j,k in edgeList])
        queries=sorted([(k,i,j,ind) for ind,(i,j,k) in enumerate(queries)])
        res=[False]*len(queries)
        ind=0
        par=[i for i in range(n)]
        rank=[0]*n
        for k,i,j,idx in queries:
            while ind<len(edgeList) and edgeList[ind][0]<k:
                self.union(edgeList[ind][1],edgeList[ind][2],par,rank)
                ind+=1
            res[idx]= self.find(i,par)==self.find(j,par)
        return res