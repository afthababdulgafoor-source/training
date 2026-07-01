from detection import detector
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
        vehicle_no=str(input("vehicle number:"))
        slot_no=int(input("slot no:"))
        date=str(input("time"))
        confidence_score=int(input("score:"))
        detector.one(vehicle_no,slot_no,date,confidence_score)
    case 2:
        r=detector.two()
        results=[]
        for vehicle_no,slot_no,dateandtime,confidence_score in r:
            result={"vehicle_no":vehicle_no,"slotno":slot_no,"dateandtime":dateandtime.strftime('%d-%m-%Y %H:%M:%S'),
                    "confidence_score":confidence_score}
            results.append(result)
            result=json.dumps(result)
            print(result)
        with open("myfile.json","a") as f:
            json.dump(results,f,indent=5)
    case 3:
        vehicle_no=str(input("vehicle number"))
        for vehicle_no,slot_no,dateandtime,confidence_score in detector.three(vehicle_no):
            result={"vehicle_no":vehicle_no,"slotno":slot_no,"dateandtime":dateandtime.strftime('%d-%m-%Y %H:%M:%S'),
                    "confidence_score":confidence_score}
            result=json.dumps(result)
            print(result)
    case 4:
        vehicle_no=str(input("vehicle number"))
        confidence_score=int(input("score:"))
        detector.four(confidence_score,vehicle_no,)
        print("value updated")
    case 5:
        vehicle_no=str(input("vehicle number"))
        detector.five(vehicle_no)
        print("RECORD DELETED")
        
    case 6:
        print("total detections:",detector.six()[0][0])
    case 7:
        r=detector.seven()
        results=[]
        for vehicle_no,slot_no,dateandtime,confidence_score in r:
            result={"vehicle_no":vehicle_no,"slotno":slot_no,"dateandtime":dateandtime.strftime('%d-%m-%Y %H:%M:%S'),
            "confidence_score":confidence_score}
            #print(result)
            results.append(result)
        for i in results:
            print(i)
    case 8:
        detector.eight()
        print("deleted successfully")
# with open('myfile.json', 'r') as file:
#     data = json.load(file)
# print(json.dumps(data, indent=4))