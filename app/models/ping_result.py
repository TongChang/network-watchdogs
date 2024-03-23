class PingResult:
    def __init__(self, timestamp, address, success, response_time=None, note=""):
        self.timestamp = timestamp
        self.address = address
        self.success = success
        self.response_time = response_time
        self.note = note
