class BackEdgeError(Exception):
    pass

class GraphNode:
    def __init__(self, node_id):
        self.id = node_id
        self.neighbors = []
    def AddNeighbor(self, neighbor):
        self.neighbors.append(neighbor)
    def DFS(self, color):
        color[self.id] = "grey"
        for node in self.neighbors:
            if color[node.id]=="white":
                node.DFS(color)
        color[self.id] = "black"
    def IsDAG(self, color):
        color[self.id] = "grey"
        for node in self.neighbors:
            if color[node.id]=="white":
                node.IsDAG(color)
            elif color[node.id]=="grey":
                raise BackEdgeError(self.id+' -> '+node.id)
        color[self.id] = "black"
    def TopologicalSort(self, color, result):
        color[self.id] = "grey"
        for node in self.neighbors:
            if color[node.id]=="white":
                node.TopologicalSort(color, result)
            elif color[node.id]=="grey":
                raise BackEdgeError(self.id+' -> '+node.id)
        color[self.id] = "black"
        result.append(self.id)

class Graph:
    def __init__(self, node_ids, edges, directed=True):
       self.nodes = {nid: GraphNode(nid) for nid in node_ids}
       if directed:
           edges_rev = []
       else:
           edges_rev = [(trg, src) for (src, trg) in edges]
       for source, target in edges + edges_rev:
           self.nodes[source].AddNeighbor(self.nodes[target])
    def PrintEdges(self):
        for sid, snode in self.nodes.items():
            for tnode in snode.neighbors:
                print(sid, "->", tnode.id)
    def DFSFromNode(self, source):
        color = {nid: "white" for nid in self.nodes}
        self.nodes[source].DFS(color)
    def DFSFromAll(self):
        color = {nid: "white" for nid in self.nodes}
        for nid, node in self.nodes.items():
            if color[nid]=="white":
                node.DFS(color)
    def IsDAG(self):
        color = {nid: "white" for nid in self.nodes}
        try:
            for nid, node in self.nodes.items():
                if color[nid]=="white":
                    node.IsDAG(color)
        except BackEdgeError:
            return False
        return True
    def TopologicalSort(self):
        color = {nid: "white" for nid in self.nodes}
        result = []
        for nid, node in self.nodes.items():
            if color[nid]=="white":
                node.TopologicalSort(color, result)
        result.reverse()
        return result