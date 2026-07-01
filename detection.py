import mysql.connector
class detector:
    my_db=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='Koko@20092002',
                                  database='vehicle_detection')
    # mycursor = my_db.cursor()
    f=open("myfile.json", "w")
    def one(vehicle_no,slot,date,confidence_score):
        mycursor = detector.my_db.cursor()
        query="INSERT INTO VEHICLE_DETECTION(vehicle_number,camera_id,detection_time,confidence_score) VALUES(%s,%s,%s,%s)"
        val=(vehicle_no,slot,date,confidence_score)
        mycursor.execute(query,val)
        detector.my_db.commit()
    def two():
        mycursor = detector.my_db.cursor()
        mycursor.execute("SELECT * FROM VEHICLE_DETECTION")
        return mycursor.fetchall()
    def three(vehicle_no):
        mycursor = detector.my_db.cursor()
        query="SELECT * FROM VEHICLE_DETECTION WHERE VEHICLE_NUMBER=%s"
        mycursor.execute(query,(vehicle_no,))
        return mycursor.fetchall()
    def four(confidence_score,vehicle_no):
        mycursor = detector.my_db.cursor()
        query="UPDATE VEHICLE_DETECTION SET CONFIDENCE_SCORE=%s WHERE VEHICLE_NUMBER=%s"
        mycursor.execute(query,(confidence_score,vehicle_no,))
        detector.my_db.commit()
    def five(vehicle_no):
        mycursor = detector.my_db.cursor()
        query="DELETE FROM VEHICLE_DETECTION WHERE VEHICLE_NUMBER=%s"
        mycursor.execute(query,(vehicle_no,))
        detector.my_db.commit()
        return mycursor.fetchall()
    def six():
        mycursor = detector.my_db.cursor()
        query="SELECT COUNT(*) AS TOTAL_DETECTIONS FROM VEHICLE_DETECTION"
        mycursor.execute(query)
        return mycursor.fetchall()
    def seven():
        mycursor = detector.my_db.cursor()
        query="SELECT * FROM VEHICLE_DETECTION WHERE CONFIDENCE_SCORE>90"
        mycursor.execute(query)
        return mycursor.fetchall()
    def eight():
        mycursor = detector.my_db.cursor()
        query="DELETE FROM VEHICLE_DETECTION WHERE VEHICLE_NUMBER IN (SELECT VEHICLE_NUMBER FROM (SELECT VEHICLE_NUMBER FROM VEHICLE_DETECTION GROUP BY VEHICLE_NUMBER HAVING COUNT(*) > 1) as T )"
        mycursor.execute(query)
        detector.my_db.commit()
