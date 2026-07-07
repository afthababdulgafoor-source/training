import datetime
from models.detection import Detector
class validator:
    def numbervalidation(vehicle_no):
        vehicle_no=str(vehicle_no)
        pattern = r"^KL[- ]?(0[1-9]|[1-9][0-9])[- ]?[A-Z]{1,3}[- ]?[0-9]{1,4}$"
        if re.match(pattern,vehicle_no):
            return True
        else:
            return False
    def scorecheck(score):
        if score>=0 and score<=100:
            return True
        else:
            return False
    def crosscheck(vehicle_no,date):
        mycursor = Detector.my_db.cursor()
        date=datetime(date)
        date=datetime.strptime(date,"%Y-%m-%d %H:%M:%S").date()
        query="SELECT * FROM vehicle_detection WHERE vehicle_number = '%s' AND" \
               " DATE(detection_time) = '%s'"
        mycursor.execute(query,(vehicle_no,date))
        return mycursor.fetchall()
    def vehicle_detection_add(vehicle_no, slot_no, date, confidence_score):
        if validator.numbervalidation(vehicle_no) and validator.scorecheck(confidence_score):
            if validator.crosscheck(vehicle_no,date)==[]:
                Detector.insertvalues(vehicle_no,slot_no,date,confidence_score)
            else:
                return "value exists"
        else:
            return "invalid vehicle number or confidence score"
        pass
