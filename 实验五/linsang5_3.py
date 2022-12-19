def get_keys(d, value):
    return [k for k,v in d.items() if v == value]

def getDegrees(oreintedGraph,node):
    outDegree=len(oreintedGraph.get(node,[]))
    for i in oreintedGraph.get(node,[]):
         print(node,'-->',i)
    inDegree=sum(1 for v in oreintedGraph.values() if node in v)
    aList=[v for v in oreintedGraph.values() if node in v]
    for v in aList:
        key=get_keys(oreintedGraph,v)
        for i in key:
            print(i,'-->',node)

    return (inDegree,outDegree)

graph={'a':set('bcdf'),'b':set('cfe'),'c':set('de'),'d':set('e'),'e':set('f'),'f':set('cgh'),
       'g':set('fhi'),'h':set('efgi'),'i':set('h')}
node=input('请输入你要查询的结点：')
io=getDegrees(graph,node)
print('入度：',io[0],'出度：',io[1])