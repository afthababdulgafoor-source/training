<<<<<<< HEAD
from repository.detection_repository import Detector
import json
from utils.validator import validator
print("1. Add a Vehicle Detection \n " \
       "2. View All Detections \n " \
"3. Search a Vehicle \n " \
"4. Update a Detection \n " \
"5. Delete a Detection \n " \
"6. Count Total Detections \n " \
"7. Show High-Confidence Detections \n " 
"8. Find Duplicate Vehicle Detections"
)
var=int(input("choice variable"))

match var:
    case 1:
        vehicle_no=str(input("vehicle number:"))
        slot_no=int(input("slot no:"))
        date=str(input("time"))
        confidence_score=int(input("score:"))
        try:
            validator.vehicle_detection_add(vehicle_no,slot_no,date,confidence_score)
        except Exception as e:
            print("invalid_input",e)
    case 2:
        r=Detector.listallvehicle()
        results=[]
        for vehicle_no,slot_no,dateandtime,confidence_score in r:
            result=Detector.display_output(vehicle_no,slot_no,dateandtime,confidence_score)
            results.append(result)
            result=json.dumps(result)
            print(result)
        with open("myfile.json","a") as f:
            json.dump(results,f,indent=5)
    case 3:
        try:
            vehicle_no=str(input("vehicle number"))
            if Detector.numbervalidation(vehicle_no)==True:
                pass
            else:
                print("invalid vehicle number")
        except Exception as e:
            print("invalid input")
        for vehicle_no,slot_no,dateandtime,confidence_score in Detector.listbyvehicleno(vehicle_no):
            result=Detector.display_output(vehicle_no,slot_no,dateandtime,confidence_score)
            result=json.dumps(result)
            print(result)
    case 4:
        try:
            vehicle_no=str(input("vehicle number"))
            confidence_score=int(input("score:"))
            if Detector.numbervalidation(vehicle_no)==True and Detector.scorecheck(confidence_score)==True:
                pass
            else:
                print("invalid vehicle number")
        except Exception as e:
            print("invalid input")
        Detector.updatescore(confidence_score,vehicle_no,)
        print("value updated")
    case 5:
        try:
            vehicle_no=str(input("vehicle number"))
            if Detector.numbervalidation(vehicle_no)==True:
                pass
            else:
                print("invalid vehicle number")
        except Exception as e:
            print("invalid input")
        Detector.deletebyvehicleno(vehicle_no)
        print("RECORD DELETED")
        
    case 6:
        print("total detections:",Detector.totaldetections()[0][0])
    case 7:
        r=Detector.listvehicleonscore()
        results=[]
        for vehicle_no,slot_no,dateandtime,confidence_score in r:
            result=Detector.display_output(vehicle_no,slot_no,dateandtime,confidence_score)
            #print(result)
            results.append(result)
        for i in results:
            print(i)
    case 8:
        Detector.deleteonvehiclecount()
        print("deleted successfully")
# with open('myfile.json', 'r') as file:
#     data = json.load(file)
=======
from Detection import Detector
import json
print("1. Add a Vehicle Detection \n " \
       "2. View All Detections \n " \
"3. Search a Vehicle \n " \
"4. Update a Detection \n " \
"5. Delete a Detection \n " \
"6. Count Total Detections \n " \
"7. Show High-Confidence Detections \n " 
"8. Find Duplicate Vehicle Detections"
)
var=int(input("choice variable"))

match var:
    case 1:
        try:
            vehicle_no=str(input("vehicle number:"))
            if Detector.vehicle_check(vehicle_no)==[]:
                if Detector.numbervalidation(vehicle_no)==True:
                    slot_no=int(input("slot no:"))
                    date=str(input("time"))
                    confidence_score=int(input("score:"))
                    if Detector.crosscheck(vehicle_no,date)==[]:
                        Detector.insertvalues(vehicle_no,slot_no,date,confidence_score)
                    else:
                        print("value exists")
                else:
                    print("invalid vehicle number")
            else:
                print("vehicle number exists")
        except Exception as e:
            print("invalid_input",e)
    case 2:
        r=Detector.listallvehicle()
        results=[]
        for vehicle_no,slot_no,dateandtime,confidence_score in r:
            result=Detector.display_output(vehicle_no,slot_no,dateandtime,confidence_score)
            results.append(result)
            result=json.dumps(result)
            print(result)
        with open("myfile.json","a") as f:
            json.dump(results,f,indent=5)
    case 3:
        try:
            vehicle_no=str(input("vehicle number"))
            if Detector.numbervalidation(vehicle_no)==True:
                pass
            else:
                print("invalid vehicle number")
        except Exception as e:
            print("invalid input")
        for vehicle_no,slot_no,dateandtime,confidence_score in Detector.listbyvehicleno(vehicle_no):
            result=Detector.display_output(vehicle_no,slot_no,dateandtime,confidence_score)
            result=json.dumps(result)
            print(result)
    case 4:
        try:
            vehicle_no=str(input("vehicle number"))
            confidence_score=int(input("score:"))
            if Detector.numbervalidation(vehicle_no)==True and Detector.scorecheck(confidence_score)==True:
                pass
            else:
                print("invalid vehicle number")
        except Exception as e:
            print("invalid input")
        Detector.updatescore(confidence_score,vehicle_no,)
        print("value updated")
    case 5:
        try:
            vehicle_no=str(input("vehicle number"))
            if Detector.numbervalidation(vehicle_no)==True:
                pass
            else:
                print("invalid vehicle number")
        except Exception as e:
            print("invalid input")
        Detector.deletebyvehicleno(vehicle_no)
        print("RECORD DELETED")
        
    case 6:
        print("total detections:",Detector.totaldetections()[0][0])
    case 7:
        r=Detector.listvehicleonscore()
        results=[]
        for vehicle_no,slot_no,dateandtime,confidence_score in r:
            result=Detector.display_output(vehicle_no,slot_no,dateandtime,confidence_score)
            #print(result)
            results.append(result)
        for i in results:
            print(i)
    case 8:
        Detector.deleteonvehiclecount()
        print("deleted successfully")
# with open('myfile.json', 'r') as file:
#     data = json.load(file)
>>>>>>> 9b22f89b6302a6d3b77cb2e9d653c968e0e4a447
# print(json.dumps(data, indent=4))