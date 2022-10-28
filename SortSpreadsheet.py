import pandas as pd
import math


name = input('File Name: ')
page = input('Page: ')
columnName = input('Column to base the sorting on: ')

df = pd.read_excel(name, page)

column = df[columnName]

functionName = input('Function to sort(none, squared, sine, cossine): ')
def f(functionName):
    if(functionName == 'sine'):
        return math.sin
    if(functionName == 'cossine'):
        return math.cos
    if(functionName == 'square'):
        return lambda x: x*x
    if(functionName == 'none'):
        return lambda x: x

    raise NotImplemented('Function not supported')


result = df.sort_values(by=columnName, key=f(functionName))

nomePlanilhaSaida = input('Exit File Name: ')
nomePaginaPlanilha = input('Page: ')
writer = pd.ExcelWriter(nomePlanilhaSaida, engine='xlsxwriter')
result.to_excel(writer, sheet_name= nomePaginaPlanilha)
writer.close()



