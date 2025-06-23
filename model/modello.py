from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}

    @staticmethod
    def getAnni():
        return DAO.getAnni()

    @staticmethod
    def getShape(anno):
        return DAO.getShape(anno)

    def buildGraph(self, anno, stato):
        pass

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()