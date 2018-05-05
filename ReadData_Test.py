import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file, ColumnDataSource
from bokeh.layouts import row
from bokeh.models import HoverTool

#Get Data
df = pd.read_csv('/Users/gretastudier/PycharmProjects/PulsarDataVisualization/Data_All_Dist.csv', delim_whitespace=True)
cols = [0,2,4,5,7,8,10,11,14]
df.drop(df.columns[cols], axis=1, inplace=True)
df.columns = ['Name', 'Period', 'Frequency', 'DM','Distance', 'DistanceDM']

for i in range(0,2635):
    if (df.ix[i][4] == '*' or df.ix[i][4] == 'NaN' or
            df.ix[i][1] == '*' or df.ix[i][1] == 'NaN' or
            df.ix[i][5] == '*' or df.ix[i][5] == 'NaN' or
            df.ix[i][3] == '*' or df.ix[i][3] == 'NaN' or
            df.ix[i][2] == '*' or df.ix[i][2] == 'NaN'):
        df.drop([i], axis=0, inplace=True)

df.Distance = np.array(df.Distance)
df.Distance = df.Distance.astype(np.float)
df.Period = np.array(df.Period)
df.Period = df.Period.astype(np.float)
df.DM = np.array(df.DM)
df.DM = df.DM.astype(np.float)
df.Frequency = np.array(df.Frequency)
df.Frequency = df.Frequency.astype(np.float)

source = ColumnDataSource(df)

#Plot Data
tools = "pan,wheel_zoom,box_zoom,reset,save".split(',')
p1 = figure(x_axis_label='Distance (kpc)', y_axis_label='Period (s)', title="Period vs Distance for Known Pulsars")

c1 = p1.circle('Distance', 'Period', color='white',fill_color='#66aecc', alpha = 0.7, size=7, source = source)
hover1 = HoverTool(tooltips=[('Name', '@Name'),('Period', '@Period'),('Distance','@Distance')])

p1.background_fill_color = '#333333'
p1.xgrid.grid_line_dash = [6, 4]
p1.xgrid.grid_line_alpha = 0.5
p1.ygrid.grid_line_dash = [6, 4]
p1.ygrid.grid_line_alpha = 0.5


#p2 = figure(x_range=(0,1), y_range=(0,1),plot_width=300, plot_height=300)
#p2.image_url(url=['/Users/gretastudier/Desktop/pulsar_image.jpg'], x=0, y=1, h=1, w=1)


p2 = figure(x_axis_label='Distance (kpc)', y_axis_label='DM (pc cm^-3)', title="DM vs Distance for Known Pulsars")
c2 = p2.circle('Distance', 'DM', color='white',fill_color='#66aecc', alpha = 0.7, size=7, source = source)
hover2 = HoverTool(tooltips=[('Name', '@Name'),('DM', '@DM'),('Distance','@Distance')])

p2.background_fill_color = '#333333'
p2.xgrid.grid_line_dash = [6, 4]
p2.xgrid.grid_line_alpha = 0.5
p2.ygrid.grid_line_dash = [6, 4]
p2.ygrid.grid_line_alpha = 0.5


p3 = figure(x_axis_label='Distance (pc)', y_axis_label='Frequency (Hz)', title="Frequency vs Distance for Known Pulsars")
c3 = p3.circle('Distance', 'Frequency', color='white',fill_color='#66aecc', alpha = 0.7, size=7, source = source)
hover3 = HoverTool(tooltips=[('Name', '@Name'),('Distance', '@Distance'),('Frequency','@Frequency')])

p3.background_fill_color = '#333333'
p3.xgrid.grid_line_dash = [6, 4]
p3.xgrid.grid_line_alpha = 0.5
p3.ygrid.grid_line_dash = [6, 4]
p3.ygrid.grid_line_alpha = 0.5

p1.add_tools(hover1)
p2.add_tools(hover2)
p3.add_tools(hover3)

output_file("PulsarVisualization.html", title="PulsarVisualization.py")
#show(p1)
show(row(p1, p2, p3))

