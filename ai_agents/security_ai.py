import hashlib
import os
from datetime import datetime

class SecurityAI:
    def __init__(self):
        self.integrity_log = []

    def hash_file(self, filepath):
        h = hashlib.sha256()
        if not os.path.exists(filepath):
            return None
        with open(filepath, "rb") as f:
            h.update(f.read())
        return h.hexdigest()

    def check_integrity(self, filepath):
        digest = self.hash_file(filepath)
        entry = {
            "file": filepath,
            "hash": digest,
            "timestamp": datetime.utcnow()
        }
        self.integrity_log.append(entry)
        return entry

    def firewall_decision(self, ip):
        bad = ["192.", "10.0", "169."]
        if ip.startswith(tuple(bad)):
            return "BLOCK"
        return "ALLOW"
