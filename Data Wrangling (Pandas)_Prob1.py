import pandas as pd
data_math={'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
data_elec={'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
data_geas={'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
data_esat={'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}

Math = pd.DataFrame(data_math,columns=['Student','Math'])
Electronics = pd.DataFrame(data_elec,columns=['Student','Electronics'])
GEAS = pd.DataFrame(data_geas,columns=['Student','GEAS'])
ESAT = pd.DataFrame(data_esat,columns=['Student','ESAT'])

m1 = pd.merge(Math,Electronics,how='left',on='Student')
m2 = pd.merge(m1,GEAS,how='left',on='Student')
m3 = pd.merge(m2,ESAT,how='left',on='Student')

longformat_1 = pd.melt(m3,id_vars='Student',value_vars=['Math','Electronics','GEAS','ESAT'])
longformat_2 = longformat_1.rename(columns={'variable':'Subject','value':'Grades'})
longformat_3 = longformat_2.sort_values('Student').reset_index().drop(columns=['index'])

print('Summary of Math scores of the We Bare Bears cast in the ECE Board Exam:\n',Math)
print('\nSummary of Electronics scores of the We Bare Bears cast in the ECE Board Exam:\n',Electronics)
print('\nSummary of GEAS scores of the We Bare Bears cast in the ECE Board Exam:\n',GEAS)
print('\nSummary of ESAT scores of the We Bare Bears cast in the ECE Board Exam:\n',ESAT)
print('\nThe resulting dataframe from four dataframes (math,electronics,geas,and esat) using pd.merge:\n',m3)
print('\nThe long format of the summary of scores of the We Bare Bears cast in the ECE Board Exam:\n',longformat_3)
