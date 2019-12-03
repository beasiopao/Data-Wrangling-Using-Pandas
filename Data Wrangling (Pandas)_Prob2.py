import pandas as pd
data_box={'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],
          'Dimension':['Length','Width','Height','Length','Width','Height'],
          'Value':[6,4,2,5,3,4]}

messy = pd.DataFrame(data_box,columns=['Box','Dimension','Value'])
tidy = messy.pivot_table(index='Box',columns='Dimension',values='Value').reset_index().rename_axis(None,axis=1)
AddNewCol_df = tidy.assign(Volume = tidy.Length*tidy.Width*tidy.Height) 

print('Messy dataframe:\n', messy)
print('\nTidy dataframe:\n', tidy)
print('\nTidy dataframe with new column (Volume):\n', AddNewCol_df)
