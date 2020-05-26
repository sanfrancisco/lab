from pandas import *

class Invoice:
    ### an Invoice object for the conciliation app ###

    def __init__(self,invNum,Df = None):
        self.invNumb = invNum
        if Df is None:
            Df =DataFrame()
        else:
            self.DataFrame = Df
    def columns(self):
        pass
###The intention is to show the data that is on both files, Invoices in this case###
    def __eq__(self, o):
        pass
###The intention is to show the data that is on self and not in other, Invoices in this case###
    def __gt__(self,o):
        pass
###The intention is to show the data that is on other and not in self, Invoices in this case###
    def __lt__(self,o):
        pass
