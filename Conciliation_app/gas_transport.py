from Pipeline import *
from Analista import *
from Counterparty import *

fco = Analista('Francisco Santiago')
Mno = Analista("Mariano Albor")

pipe1 = Pipeline('Pipeline One')
pipe2 = Pipeline('Pipeline Two')

ctprty1 = Counterparty('Counterparty One')
ctprty2 = Counterparty('Counterparty Two')

print(ctprty1.get_pipelines())
ctprty1.add_pipeline(pipe1)
print(ctprty1.get_pipelines())
ctprty1.add_pipeline(pipe2)
print(ctprty1.get_pipelines())
