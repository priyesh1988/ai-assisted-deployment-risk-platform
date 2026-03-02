
from datetime import datetime

usage_log = []

def record_usage(tenant_id, event_type):
    usage_log.append({
        "tenant": tenant_id,
        "event": event_type,
        "timestamp": datetime.utcnow().isoformat()
    })
