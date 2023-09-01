from errors import GraphNotDeclared, GraphAlreadyDeclared, VertexNotDeclared, VertexContainsEdge, EdgeNotDeclared

class SymTable():
    def __init__(self):
        self.graphs = {}
        self.other_vertices = {}
        self.graph_context = None

    def graph_exists(self, graph):
        return graph in self.graphs

    def _vertex_exists(self, vertex):
        return vertex in self.graphs[self.graph_context]["vertex"]
    
    def _has_edges(self, vertex):
        edges = self.graphs[self.graph_context]["vertex"][vertex]["edges"]
        if len(edges) > 0:
            return True
        for v in self.graphs[self.graph_context]["vertex"]:
            if vertex in self.graphs[self.graph_context]["vertex"][v]["edges"]:
                return True
        return False

    def _edge_exists(self, vertex1, vertex2):
        if vertex2 in self.graphs[self.graph_context]["vertex"][vertex1]["edges"]:
            return True
        return False

    def add_graph(self, graph):
        graph_name = graph.getText()

        if not self.graph_exists(graph_name):
            self.graphs[graph_name] = {
                "vertex": {},
            }
        else:
            raise GraphAlreadyDeclared(graph_name)

    def add_vertex(self, vertex, weight=None):
        if not self.graph_exists(self.graph_context):
            raise GraphNotDeclared(self.graph_context)
        else:
            self.graphs[self.graph_context]["vertex"][vertex] = {
                "weight" : weight,
                "edges": {}
            }

    def remove_vertex(self, vertex):
        if not self.graph_exists(self.graph_context):
            raise GraphNotDeclared(self.graph_context)
        if not self._vertex_exists(vertex):
            raise VertexNotDeclared(vertex)
        if self._has_edges(vertex):
            raise VertexContainsEdge(vertex)
        del self.graphs[self.graph_context]["vertex"][vertex]

    def _add_edge_to_graph(self, vertex1, vertex2, weight=None):
        self.graphs[self.graph_context]["vertex"][vertex1]["edges"][vertex2] = {
                "vertex": vertex2,
                "weight": weight
            }

    def add_edge(self, vertex1, vertex2, direction, weight=None):
        if not self.graph_exists(self.graph_context):
            raise GraphAlreadyDeclared(self.graph_context)
        if not self._vertex_exists(vertex1):
            raise VertexNotDeclared(vertex1)
        if not self._vertex_exists(vertex2):
            raise VertexNotDeclared(vertex2)

        if direction == ">":
            self._add_edge_to_graph(vertex1, vertex2, weight)
        elif direction == "<":
            self._add_edge_to_graph(vertex2, vertex1, weight)
        elif direction == "<>":
            self._add_edge_to_graph(vertex1, vertex2, weight)
            self._add_edge_to_graph(vertex2, vertex1, weight)

        else:
            self.graphs[self.graph_context]["vertex"][vertex1]["edges"].append(vertex2)

    def remove_edge(self, vertex1, vertex2, direction):
        if not self.graph_exists(self.graph_context):
            raise GraphNotDeclared(self.graph_context)
        if not self._vertex_exists(vertex1):
            raise VertexNotDeclared(vertex1)
        if not self._vertex_exists(vertex2):
            raise VertexNotDeclared(vertex2)
        if direction == ">":
            if not self._edge_exists(vertex1, vertex2):
                raise EdgeNotDeclared(f"{vertex1} {direction} {vertex2}")
            del self.graphs[self.graph_context]["vertex"][vertex1]["edges"][vertex2]
        elif direction == "<":
            if not self._edge_exists(vertex2, vertex1):
                raise EdgeNotDeclared(f"{vertex1} {direction} {vertex2}")
            del self.graphs[self.graph_context]["vertex"][vertex2]["edges"][vertex1]
        elif direction == "<>":
            if not self._edge_exists(vertex1, vertex2):
                raise EdgeNotDeclared(f"{vertex1} {direction} {vertex2}")
            if not self._edge_exists(vertex2, vertex1):
                raise EdgeNotDeclared(f"{vertex1} {direction} {vertex2}")
            del self.graphs[self.graph_context]["vertex"][vertex1]["edges"][vertex2]
            del self.graphs[self.graph_context]["vertex"][vertex2]["edges"][vertex1]


    def _move_graph2_to_graph1(self, graph1, graph2):
        for vertex in self.graphs[graph2]["vertex"]:
            self.graphs[graph1]["vertex"][vertex] = self.graphs[graph2]["vertex"][vertex].copy()

    def join_graph(self, graph1, graph2, vertex1, vertex2, direction):
        if not self.graph_exists(graph1):
            raise GraphNotDeclared(graph1)
        if not self.graph_exists(graph2):
            raise GraphNotDeclared(graph2)

        self._move_graph2_to_graph1(graph1, graph2)

        self.graph_context = graph1
        self.add_edge(vertex1, vertex2, direction)
        self.graph_context = None

    def attr_graph(self, graph1, graph2):
        if not self.graph_exists(graph1):
            raise GraphNotDeclared(graph1)
        if not self.graph_exists(graph2):
            raise GraphNotDeclared(graph2)

        self.graphs[graph1] = self.graphs[graph2].copy()