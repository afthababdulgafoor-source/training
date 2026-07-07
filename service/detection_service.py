from datetime import datetime
import re
class buisness_logic:
    def __init__(self):
        pass
    def process_data(self, data):
        processed_data = data  
        return processed_data
    def display_output(vehicle_no,slot_no,dateandtime,confidence_score):
        result={"vehicle_no":vehicle_no,"slotno":slot_no,"dateandtime":dateandtime.strftime('%d-%m-%Y %H:%M:%S'),
                "confidence_score":confidence_score}
        return result
