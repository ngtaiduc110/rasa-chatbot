# custom_tracker_store.py
from rasa.core.tracker_store import PostgreSQLTrackerStore
from rasa.shared.core.trackers import DialogueStateTracker
from typing import Optional, Text, Dict, Any, List
from rasa.shared.core.events import Event, UserUttered, BotUttered

class CustomPostgreSQLTrackerStore(PostgreSQLTrackerStore):
    def __init__(self, url, **kwargs):
        print("=== CustomPostgreSQLTrackerStore: KHỞI TẠO THÀNH CÔNG ===")
        super().__init__(url, **kwargs)
    
    def save(self, tracker: DialogueStateTracker) -> None:
        filtered_events = []
        events_to_keep = []
        
        for event in tracker.events:
            if isinstance(event, (UserUttered, BotUttered)):
                filtered_events.append(event)
                events_to_keep.append(event)
        
        print(f"=== Đang lưu {len(filtered_events)} events của conversation {tracker.sender_id} ===")
        
        if not filtered_events:
            print("Không có events cần lưu, bỏ qua")
            return
            
        filtered_tracker = DialogueStateTracker(
            sender_id=tracker.sender_id,
            slots=tracker.slots,
        )
        
        for event in events_to_keep:
            filtered_tracker.update(event)
        
        super().save(filtered_tracker)
