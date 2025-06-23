from database.DB_connect import DBConnect
from model.sighting import Sighting
from model.state import State


class DAO:


    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ SELECT distinct YEAR(s.datetime)
                    FROM sighting s
                    order by YEAR(s.datetime) desc"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["YEAR(s.datetime)"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getShape(anno):
        pass