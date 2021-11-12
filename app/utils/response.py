class Response:
    success = False
    data = None
    errorMessage = ""

    def __init__(self, success, payload, errorMessage):
        self.success = success
        self.data = payload
        self.errorMessage = errorMessage