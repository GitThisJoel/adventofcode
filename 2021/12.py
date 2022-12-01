import sys

def create_graph(inp):
    graph = {}
    for v,w in map(lambda e: e.split('-'), inp):
        if v in graph:
            graph[v].append(w)
        else:
            graph[v] = [w]

        if w in graph:
            graph[w].append(v)
        else:
            graph[w] = [v]
    return graph

def p1(g, n = 'start'):
    v = set()

    return

def p2():
    return

if __name__ == "__main__":
    inp = [l.strip() for l in sys.stdin]
    g = create_graph(inp)
    p1(g)
