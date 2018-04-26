import pandas as pd
import numpy as np
from bokeh.io import output_file, show
from bokeh.models import HoverTool
from bokeh.plotting import figure

df = pd.read_csv('/Users/gretastudier/PycharmProjects/PulsarDataVisualization/Data_All.csv', delim_whitespace=True)
cols = [0,2,4,5,7,8,10,11]
df.drop(df.columns[cols], axis=1, inplace=True)
df.columns = ['Name', 'Period', 'Frequency', 'DM','Distance']
print df.head()

#df.drop([0,1], axis=0,inplace=True)
for i in range(0,2635):
    if (df.ix[i][4] == '*' or df.ix[i][4] == 'NaN' or df.ix[i][1] == '*'):
        df.drop([i], axis=0, inplace=True)
print df.tail(40)

#df[:-500]
#df.drop(df.rows[cols], axis=0, implace=True)
#print df.tail()


# n = 500
# x = 2 + 2*np.random.standard_normal(n)
# y = 2 + 2*np.random.standard_normal(n)
r=np.array(df.Distance)
r = r.transpose()
r=r.astype(np.float)

p = np.array(df.Period)
p = p.transpose()
p = p.astype(np.float)

x = r
y = p

p = figure(title="Hexbin for 500 points", match_aspect=True,
           tools="wheel_zoom,reset", background_fill_color='#440154')
p.grid.visible = False

r, bins = p.hexbin(x, y, size=0.5, hover_color="pink", hover_alpha=0.8)

p.circle(x, y, color="white", size=0.01)

hover = HoverTool(tooltips=[("count", "@c"), ("(q,r)", "(@q, @r)")],
                  mode="mouse", point_policy="follow_mouse", renderers=[r])

p.add_tools(hover)

output_file("hexbin.html")

show(p)