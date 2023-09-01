import networkx as nx
import matplotlib.pyplot as plt 

class GraphDrawer():
    def __init__(self):
        self.nx_graph = nx.DiGraph()
        self.vertex_weights = {}
        self.edge_colors = {}
        self.vertex_colors = {}

    def create_graph(self, graph):
        self.graph = graph
        self.add_nodes()

    def draw(self, graph):
        self.graph = graph
        self.add_nodes()
        self._draw()


    def _draw(self):
        pos = nx.spring_layout(self.nx_graph, seed=0)

        # Draw nodes
        nx.draw_networkx_nodes(self.nx_graph, pos, node_size=400)
        for color in self.vertex_colors:
            nx.draw_networkx_nodes(self.nx_graph, pos, nodelist=[color], node_size=400, node_color=self.vertex_colors[color])

        # Draw edges
        edge_list = [(u, v) for (u, v, d) in self.nx_graph.edges(data=True)]
        nx.draw_networkx_edges(self.nx_graph, pos, edgelist=edge_list, width=1)
        for color in self.edge_colors:
            nx.draw_networkx_edges(self.nx_graph, pos, edgelist=[color], width=1, edge_color=self.edge_colors[color])

        # Draw labels
        nx.draw_networkx_labels(self.nx_graph, pos, font_size=8, font_family="sans-serif")

        # Draw weights
        edge_labels = nx.get_edge_attributes(self.nx_graph, "weight")
        nx.draw_networkx_edge_labels(self.nx_graph, pos, edge_labels)

        plt.show()
    
    def _mount_weighted_node(self, vertex):
        if vertex in self.vertex_weights.keys():
            weight = self.vertex_weights[vertex]
            return f"{vertex}({weight})"
        else:
            return vertex

    def _add_node(self, vertex):
        vertex_weighted = self._mount_weighted_node(vertex)
        self.nx_graph.add_node(vertex_weighted)

    def _add_edge(self, vertex1, vertex2, weight):
        vertex1 = self._mount_weighted_node(vertex1)
        vertex2 = self._mount_weighted_node(vertex2)
        if weight is not None:
            self.nx_graph.add_edge(vertex1, vertex2, weight=weight)
        else: 
            self.nx_graph.add_edge(vertex1, vertex2)

    def add_nodes(self):
        for vertex in self.graph["vertex"]:
            if self.graph["vertex"][vertex]["weight"] is not None:
                self.vertex_weights[vertex] = self.graph["vertex"][vertex]["weight"]
            self._add_node(vertex)
            if len(self.graph["vertex"][vertex]["edges"]) > 0:
                for edge in self.graph["vertex"][vertex]["edges"].values():
                    weight = edge["weight"]
                    edge_node = edge["vertex"]
                    self._add_edge(vertex, edge_node, weight)

    def shortest_path(self, vertex1, vertex2):
        vertex1 = self._mount_weighted_node(vertex1)
        vertex2 = self._mount_weighted_node(vertex2)
        try:
            if len(nx.shortest_path(self.nx_graph, vertex1, vertex2)) > 0:
                return nx.shortest_path(self.nx_graph, vertex1, vertex2)

        except nx.NetworkXNoPath:
            return None

    def _set_edge_color(self, edge, color):
        self.edge_colors[edge] = color

    def _set_node_color(self, vertex, color):
        vertex = self._mount_weighted_node(vertex)
        self.vertex_colors[vertex] = color

    def _draw_shortest_path(self, shortest_path):
        for i in range(len(shortest_path) - 1):
            edge = (shortest_path[i], shortest_path[i + 1])
            self._set_edge_color(edge, "red")
            self._set_node_color(shortest_path[i], "red")

        self._set_node_color(shortest_path[0], "yellow")
        self._set_node_color(shortest_path[-1], "green")
        self._draw()

    def draw_shortest_path(self, vertex1, vertex2):
        shortest_path = self.shortest_path(vertex1, vertex2)
        if shortest_path is not None:
            self._draw_shortest_path(shortest_path)
        else:
            print("No path found")
