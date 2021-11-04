class Response:
    success = False
    payload = None
    errorMessage = ""

    def __init__(self, success, payload, errorMessage):
        self.success = success
        self.payload = payload
        self.errorMessage = errorMessage