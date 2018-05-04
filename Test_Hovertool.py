import pandas as pd
import numpy as np
from bokeh.plotting import figure, ColumnDataSource
from bokeh.io import output_file, show
from bokeh.models import HoverTool

df = pd.read_csv('/Users/gretastudier/PycharmProjects/PulsarDataVisualization/Data_All_Dist.csv', delim_whitespace=True)
cols = [0,2,4,5,7,8,10,11,14]
df.drop(df.columns[cols], axis=1, inplace=True)
df.columns = ['Name', 'Period', 'Frequency', 'DM','Distance', 'DistanceDM']

#df.drop([0,1], axis=0,inplace=True)
for i in range(0,2635):
    if (df.ix[i][4] == '*' or df.ix[i][4] == 'NaN' or df.ix[i][1] == '*' or df.ix[i][1] == 'NaN' or df.ix[i][5] == '*' or df.ix[i][5] == 'NaN'):
        df.drop([i], axis=0, inplace=True)

df.Distance = np.array(df.Distance)
df.Distance = df.Distance.astype(np.float)
df.Period = np.array(df.Period)
df.Period = df.Period.astype(np.float)

source = ColumnDataSource(df)

# Create the figure: p
p = figure()

# Add circle glyphs to the figure p
p.circle('Distance', 'Period', source=source)
hover = HoverTool(tooltips=[('Name', '@Name'),('Distance','@Distance'),('Period', '@Period')])
#show(p)

p.add_tools(hover)
show(p)