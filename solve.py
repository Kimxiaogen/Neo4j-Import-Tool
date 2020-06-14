from py2neo import Database, Graph, Node, Relationship

def insert(url,username,password,arr):
    graph = Graph(url,auth=(username, password))
    tx = graph.begin();
    nodes = None
    map = {}    # Key : name ; Value : Node
    count = 0
    for a in arr:
        count += 1
        l = len(a)
        sub = None
        if(l == 1):
            sub = SubgraphNodeOne(graph,map,a)
        elif(l == 2):
            sub = SubgraphNodeDouble(graph,map,a)
        elif(l == 3):
            sub = SubgraphNodeDoubleWithRelationship(graph,map,a)
        else:
            continue
        if(nodes is None):
            nodes = sub
        else:
            nodes |= sub
        if(count % 100 == 0):
            print(count)
    tx.create(nodes)
    tx.commit()

#单节点实体#
def SubgraphNodeOne(graph,map,arr):
    n = getInMapOrDataBase(graph,map, arr[0])
    return n


#双节点空关系实体#
def SubgraphNodeDouble(graph,map,arr):
    n1 = getInMapOrDataBase(graph,map, arr[0])
    n2 = getInMapOrDataBase(graph,map, arr[1])
    r = Relationship(n1, None, n2)
    return n1 | n2 | r


#双节点有关系实体#
def SubgraphNodeDoubleWithRelationship(graph,map,arr):
    n1 = getInMapOrDataBase(graph,map, arr[0])
    n2 = getInMapOrDataBase(graph,map, arr[1])
    r = Relationship(n1, arr[2], n2)
    return n1 | n2 | r

#检查map或数据库中是否有同name属性实体，若都没有，则创建新实体#
def getInMapOrDataBase(graph,map,name):
    if (map.__contains__(name)):
        n = map.get(name)
    else:
        m = graph.nodes.match('Entity').where('_.name = \'' + name + '\'')
        n = m.first()
        if(n is None):
            n = Node('Entity', name=name)
        map[name] = n
    return n