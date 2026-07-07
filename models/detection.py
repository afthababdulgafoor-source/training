
import re
# from config import host,user,password,database

class Display:
    def __init__(self,vehicle_no,slot_no,time,confidence_score):
        self.vehicle_no=vehicle_no
        self.slot_no=slot_no
        self.time=time
        self.confidence_score=confidence_score
        pass
    
class Detector:
    
    f=open("myfile.json", "w")
    def insertvalues(vehicle_no,slot,date,confidence_score):
        mycursor = Detector.my_db.cursor()
        query="INSERT INTO VEHICLE_DETECTION(vehicle_number,camera_id,detection_time,confidence_score) VALUES(%s,%s,%s,%s)"
        val=(vehicle_no,slot,date,confidence_score)
        mycursor.execute(query,val)
        Detector.my_db.commit()
    def listallvehicle():
        mycursor = Detector.my_db.cursor()
        mycursor.execute("SELECT * FROM VEHICLE_DETECTION")
        return mycursor.fetchall()
    def listbyvehicleno(vehicle_no):
        mycursor = Detector.my_db.cursor()
        query="SELECT * FROM VEHICLE_DETECTION WHERE VEHICLE_NUMBER=%s"
        mycursor.execute(query,(vehicle_no,))
        return mycursor.fetchall()
    def updatescore(confidence_score,vehicle_no):
        mycursor = Detector.my_db.cursor()
        query="UPDATE VEHICLE_DETECTION SET CONFIDENCE_SCORE=%s WHERE VEHICLE_NUMBER=%s"
        mycursor.execute(query,(confidence_score,vehicle_no,))
        Detector.my_db.commit()
    def deletebyvehicleno(vehicle_no):
        mycursor = Detector.my_db.cursor()()
        query="DELETE FROM VEHICLE_DETECTION WHERE VEHICLE_NUMBER=%s"
        mycursor.execute(query,(vehicle_no,))
        Detector.my_db.commit()
        return mycursor.fetchall()
    def totaldetections():
        mycursor = Detector.my_db.cursor()
        query="SELECT COUNT(*) AS TOTAL_DETECTIONS FROM VEHICLE_DETECTION"
        mycursor.execute(query)
        return mycursor.fetchall()
    def listvehicleonscore():
        mycursor = Detector.my_db.cursor()
        query="SELECT * FROM VEHICLE_DETECTION WHERE CONFIDENCE_SCORE>90"
        mycursor.execute(query)
        return mycursor.fetchall()
    def deleteonvehiclecount():
        mycursor = Detector.my_db.cursor()
        query="DELETE FROM VEHICLE_DETECTION WHERE VEHICLE_NUMBER IN (SELECT VEHICLE_NUMBER FROM (SELECT VEHICLE_NUMBER FROM VEHICLE_DETECTION GROUP BY VEHICLE_NUMBER HAVING COUNT(*) > 1) as T )"
        mycursor.execute(query)
        detector.my_db.commit()
    def vehicle_check(vehicle_no):
        mycursor = Detector.my_db.cursor()
        query="SELECT * FROM VEHICLE_DETECTION WHERE VEHICLE_NUMBER=%s"
        mycursor.execute(query,(vehicle_no,))
        return mycursor.fetchall()
    