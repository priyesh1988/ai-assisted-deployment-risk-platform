
import hashlib
import json
from datetime import datetime

last_hash = None

def audit_log(payload):
    global last_hash
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "payload": payload,
        "previous_hash": last_hash
    }
    encoded = json.dumps(record, sort_keys=True).encode()
    current_hash = hashlib.sha256(encoded).hexdigest()
    record["hash"] = current_hash
    last_hash = current_hash
    return record
