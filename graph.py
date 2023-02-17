class Graph:
    def __init__(self, node_count: int, edge_count: int = 0, adj_list: list[list[int]] = []) -> None:
        self.node_count = node_count
        self.edge_count = edge_count
        self.adj_list = adj_list
        self.nodes = []
        if adj_list == []:
            for _ in range(self.node_count):
                self.adj_list.append([])

    def add_directed_edge(self, u: int, v: int):
        if u < 0 or u >= len(self.adj_list) or v < 0 or v >= len(self.adj_list):
            print(f"Node u={u} or v={v} is out of allowed range (0, {self.node_count - 1})")
        self.adj_list[u].append(v)
        self.edge_count += 1

    def imprime(self):
        repr = ""
        for adj in self.adj_list:
            repr += str(adj) + "\n"
        print(repr)

    def is_vizinho(self, u, v):
        if v not in self.adj_list[u]:
            return False
        return True
        
    def unvisted_neighbor(self, u, desc: list[int]):
        for i in self.adj_list[u]:
            if i < len(desc) and desc[i] == 0:
                return i
        else:
            return -1

    
    def dfs(self, s, t):
        desc=[]
        for u in range(self.node_count): # desc[0 for _ in range(self.node_count)]
            desc.append(0)
        S=[s]
        R=[s]
        desc[s] = 1
        while len(S) != 0:
            u = S.pop() 
            S.append(u)
            v = self.unvisted_neighbor(u, desc)
            if(v != - 1):
                S.append(v)
                R.append(v)
                desc[v] = 1
                if v == t:
                    return S # Caminho entre s e t
            else:
                S.pop()
        return R
    

    

    