import pandas as pd
import glob

#show only 1 cell
for i in glob.iglob('data/*csv'):
    df=pd.read_csv(i)
    val = df['name'].values[0]

    print(val)
    print(df[['date','tweet']])
    df.to_html('a.html')
