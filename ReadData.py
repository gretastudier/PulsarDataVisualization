import pandas as pd
import numpy as np

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin

df = pd.read_csv('/Users/gretastudier/PycharmProjects/PulsarDataVisualization/Data_All.csv', delim_whitespace=True)
cols = [0,2,4,5,7,8,10,11]
df.drop(df.columns[cols], axis=1, inplace=True)
df.columns = ['Name', 'Period', 'Frequency', 'DM','Distance']
print df.head()

#df.drop([0,1], axis=0,inplace=True)
for i in range(0,2635):
    if (df.ix[i][4] == '*' or df.ix[i][4] == 'NaN' or df.ix[i][1] == '*'):
        df.drop([i], axis=0, inplace=True)
#print df.head()

#df.drop([2500,:], axis=0, implace=True)
#print df.head()

#Plot Data:
# n = 50000
# x = np.random.standard_normal(n)
# y = np.random.standard_normal(n)
r=np.array(df.Distance)
r = r.transpose()
r=r.astype(np.float)

p = np.array(df.Period)
p = p.transpose()
p = p.astype(np.float)
x = r
y = p

p = figure(title="Manual hex bin for 50000 points", tools="wheel_zoom,reset",
           match_aspect=True, background_fill_color='#440154')
p.grid.visible = False

bins = hexbin(x, y, 0.1)

p.hex_tile(q="q", r="r", size=0.1, line_color=None, source=bins,
           fill_color=linear_cmap('counts', 'Viridis256', 0, max(bins.counts)))

output_file("hex_tile.html")
show(p)