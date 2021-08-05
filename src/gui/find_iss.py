'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


import pandas as pd
import plotly.express as px

# Store variables
url = 'http://api.open-notify.org/iss-now.json'
df = pd.read_json(url)

# Change order of data frame
df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)

df = df.drop(['index', 'message'], axis=1) # Remove index

fig = px.scatter_geo(df, lat='latitude', lon='longitude') # Plot information
fig.show() # Open map in browser
