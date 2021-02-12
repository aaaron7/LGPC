
class Status:
    def __init__(self, code = 0, msg = ""):
        self.code = code
        self.msg = msg
    

def OkStatus():
    return Status()

def ParameterInvalidStatus():
    return Status(-1, "function pamameter is not valid");