class Counterparty:
    # def __init__(self,name):
    #     self.name = name

    def __init__(self,name,pipelines = None):
        self.name=name
        if pipelines is None:
            self.pipelines = []
        else:
            self.pipelines = pipelines
    def add_pipeline(self,pipeline):
        self.pipelines.append(pipeline)

    def get_pipelines(self):
        for pipeline in self.pipelines:
            print('-->'+str(pipeline))
