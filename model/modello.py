from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._idMap = {}

    @staticmethod
    def getAnni():
        return DAO.getAnni()

    @staticmethod
    def getShape(anno):
        return DAO.getShape(anno)

    def buildGraph(self, anno, forma):
        self._graph.clear()
        self._idMap.clear()
        nodi = DAO.getNodi(anno, forma)
        for nodo in nodi:
            self._idMap[nodo.id] = nodo
        self._graph.add_nodes_from(nodi)
        archi = DAO.getArchi(anno, forma)
        for arco in archi:
            if arco["longitude1"] < arco["longitude2"]:
                self._graph.add_edge(self._idMap[arco["id1"]], self._idMap[arco["id2"]],
                                     weight = abs(arco["longitude2"]-arco["longitude1"]))
            else:
                self._graph.add_edge(self._idMap[arco["id2"]], self._idMap[arco["id1"]],
                                     weight=abs(arco["longitude1"] - arco["longitude2"]))

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def archiPesoMaggiore(self):
        edges = list(self._graph.edges(data = True))
        archiordinati = sorted(self._graph.edges(data = True), key = lambda x: x[2].get("weight", 0), reverse=True)
        archidef = []
        for i in range(0,5):
            archidef.append(f"{archiordinati[i][0].id} -> {archiordinati[i][1].id} | weight = {archiordinati[i][2]["weight"]}")
        return archidef