
class Pipeline:
    def __init__(self,name,Counterparty=None):
        self.name = name
        if Counterparty is None:
            self.Counterparty = None
        else:
            self.Counterparty = Counterparty
