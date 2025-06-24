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
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ SELECT distinctrow s.shape
                    FROM sighting s
                    where s.shape is not NULL and YEAR(s.datetime) = %s
                    order by s.shape asc"""
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(row["shape"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(anno, forma):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ SELECT distinctrow *
                    FROM sighting s
                    where s.shape = %s and YEAR(s.datetime) = %s
                    order by s.shape asc"""
        cursor.execute(query, (forma, anno,))
        for row in cursor:
            result.append(Sighting(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(anno, forma):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ select tb1.id1, tb1.longitude1, tb2.id2, tb2.longitude2
                    from(select s.id as id1,s.state as state1, s.longitude as longitude1
	                     from sighting s 
	                     where s.shape = %s and year(s.`datetime`) = %s) tb1, 
	                    (select s.id as id2,s.state as state2, s.longitude as longitude2
						 from sighting s 
						 where s.shape = %s and year(s.`datetime`) = %s) tb2
                    where tb1.state1 = tb2.state2 and tb1.id1 < tb2.id2 and tb1.longitude1 != tb2.longitude2 """
        cursor.execute(query, (forma, anno, forma, anno))
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result