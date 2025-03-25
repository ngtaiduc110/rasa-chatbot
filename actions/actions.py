from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json
import requests
from datetime import datetime, timedelta

class ValidateBookingForm(Action):
    def name(self) -> Text:
        return "validate_booking_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slots_to_validate = ["name", "date", "time", "address", "phone_number"]
        validated_slots = []

        for slot in slots_to_validate:
            value = tracker.get_slot(slot)
            if not value:
                return [SlotSet(slot, None)] 
        
        # Nếu tất cả các slot đã được điền, không cần yêu cầu thêm
        return []

class ActionSubmitBooking(Action):
    def name(self) -> Text:
        return "action_submit_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Lấy thông tin từ slots
        name = tracker.get_slot("name")
        date = tracker.get_slot("date")
        time = tracker.get_slot("time")
        address = tracker.get_slot("address")
        phone_number = tracker.get_slot("phone_number")
        
        # TODO: Gửi thông tin đến API đặt lịch
        # response = requests.post("your_booking_api_url", json={
        #     "name": name,
        #     "date": date,
        #     "time": time,
        #     "address": address,
        #     "phone_number": phone_number
        # })
        
        dispatcher.utter_message(text=f"Cảm ơn bạn {name}! Lịch khám của bạn đã được đặt vào {date} lúc {time}.")
        return []

class ActionEmergencyHandling(Action):
    def name(self) -> Text:
        return "action_emergency_handling"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        severity = tracker.get_slot("severity")
        symptoms = tracker.get_slot("symptoms")
        
        if severity == "Nặng":
            dispatcher.utter_message(text="Đây là tình huống khẩn cấp! Vui lòng gọi ngay số điện thoại cấp cứu: 115")
            dispatcher.utter_message(text="Các triệu chứng của bạn: " + ", ".join(symptoms))
        else:
            dispatcher.utter_message(text="Tôi sẽ giúp bạn tìm bác sĩ phù hợp để khám.")
        
        return []

class ActionProvideMedicalAdvice(Action):
    def name(self) -> Text:
        return "action_provide_medical_advice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        symptoms = tracker.get_slot("symptoms")
        severity = tracker.get_slot("severity")
        medical_history = tracker.get_slot("medical_history")
        allergies = tracker.get_slot("allergies")
        
        # TODO: Tích hợp với API tư vấn y tế
        # response = requests.post("your_medical_advice_api_url", json={
        #     "symptoms": symptoms,
        #     "severity": severity,
        #     "medical_history": medical_history,
        #     "allergies": allergies
        # })
        

        advice = "Dựa trên thông tin bạn cung cấp, tôi khuyên bạn nên:"
        if severity == "Nặng":
            advice += "\n- Đến bệnh viện ngay lập tức"
        else:
            advice += "\n- Đặt lịch khám với bác sĩ chuyên khoa"
            advice += "\n- Uống đủ nước và nghỉ ngơi"
            advice += "\n- Theo dõi các triệu chứng"
        
        dispatcher.utter_message(text=advice)
        return []

class ActionSearchDoctor(Action):
    def name(self) -> Text:
        return "action_search_doctor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        doctor_name = tracker.get_slot("doctor_name")
        department = tracker.get_slot("department")
        
        # TODO: Tích hợp với API tìm kiếm bác sĩ
        # response = requests.get("your_doctor_search_api_url", params={
        #     "name": doctor_name,
        #     "department": department
        # })
        
        dispatcher.utter_message(text=f"Thông tin về bác sĩ {doctor_name}:")
        dispatcher.utter_message(text="- Chuyên khoa: " + department)
        dispatcher.utter_message(text="- Kinh nghiệm: 10 năm")
        dispatcher.utter_message(text="- Lịch khám: Thứ 2 - Thứ 6")
        
        return []

class ActionSearchDepartment(Action):
    def name(self) -> Text:
        return "action_search_department"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        department = tracker.get_slot("department")
        
        # TODO: Tích hợp với API tìm kiếm khoa
        # response = requests.get("your_department_search_api_url", params={
        #     "department": department
        # })
        
        dispatcher.utter_message(text=f"Thông tin về khoa {department}:")
        dispatcher.utter_message(text="- Số lượng bác sĩ: 5")
        dispatcher.utter_message(text="- Thời gian làm việc: 24/7")
        dispatcher.utter_message(text="- Các dịch vụ: Khám bệnh, Xét nghiệm, Chẩn đoán hình ảnh")
        
        return []

class ActionCheckInsurance(Action):
    def name(self) -> Text:
        return "action_check_insurance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        insurance_type = tracker.get_slot("insurance_type")
        
        # TODO: Tích hợp với API kiểm tra bảo hiểm
        # response = requests.get("your_insurance_check_api_url", params={
        #     "insurance_type": insurance_type
        # })
        
        dispatcher.utter_message(text=f"Thông tin về bảo hiểm {insurance_type}:")
        dispatcher.utter_message(text="- Tỷ lệ chi trả: 80%")
        dispatcher.utter_message(text="- Phạm vi: Khám bệnh, Xét nghiệm, Thuốc")
        dispatcher.utter_message(text="- Thời gian xử lý: 3-5 ngày")
        
        return []

class ActionScheduleFollowUp(Action):
    def name(self) -> Text:
        return "action_schedule_follow_up"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        last_appointment = tracker.get_slot("date")
        if last_appointment:
            follow_up_date = datetime.strptime(last_appointment, "%Y-%m-%d") + timedelta(days=7)
            dispatcher.utter_message(text=f"Tôi sẽ đặt lịch tái khám cho bạn vào ngày {follow_up_date.strftime('%Y-%m-%d')}")
        else:
            dispatcher.utter_message(text="Tôi không tìm thấy lịch khám trước đó của bạn.")
        
        return []
