class Response:
    '''A class that is used to add structure to the output of 
    auth and database functions. It acts as a wrapper that contains
    whether the function succeeded in doing its job, any associated 
    data, and an error message'''

    success = False
    data = None
    errorMessage = ""

    def __init__(self, success, data, errorMessage):
        self.success = success
        self.data = data
        self.errorMessage = errorMessage