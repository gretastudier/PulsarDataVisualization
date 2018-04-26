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
#print df.head()

#df.drop([0,1], axis=0,inplace=True)
for i in range(0,2635):
    if (df.ix[i][4] == '*' or df.ix[i][4] == 'NaN' or df.ix[i][1] == '*' or df.ix[i][1] == 'NaN' or df.ix[i][5] == '*' or df.ix[i][5] == 'NaN'):
        df.drop([i], axis=0, inplace=True)
#print df.tail(40)

print df.Name

#Plot Data
n = np.array(df.Name)

r = np.array(df.Distance)
r = r.astype(np.float)

p = np.array(df.Period)
p = p.astype(np.float)

x = r
y = p
N = 2572
# N = 4000
# x = np.random.random(size=N) * 100
# y = np.random.random(size=N) * 100
radii = 0.3 #np.random.random(size=N) * 1.5
# colors = [
#     "#%02x%02x%02x" % (int(r), int(g), 180) for r, g in zip(50+2*x, 30+2*y)   #"#d25582"
# ]

#TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
tools = "pan,wheel_zoom,box_zoom,reset,save".split(',')
hover = HoverTool(tooltips=[
    ("name", "@Name"),
    ("Distance", "@x"),
    ("Period", "@y")
])
tools.append(hover)

#p = figure(tools=tools, toolbar_location="above", logo="grey", plot_width=1200, title=TITLE)
p1 = figure(tools=tools, x_axis_label='Distance (kpc)', y_axis_label='Period (s)', title="Distance vs Period for Known Pulsars") #tools=TOOLS)

#"@foo{($ 0.00 a)}" # formats 1230974 as: $ 1.23 m

#p1.add_tools(HoverTool( tooltips=[('Index', '$index'),('Pulsar', '@n'),("Distance (kpc)", "@x"), ("Period (s)", "@y")]))

#c1 = p.circle(x=x, y=y, color='white', fill_color="#0099ff", alpha = 0.5, size=6)
c1 = p1.circle(x=x, y=y, color='white',fill_color='#66aecc', alpha = 0.8, size=7)

#p.add_tools(HoverTool(renderers=[c1], tooltips=[("Years", "@x"),("Women", "@y"),]))
#p.scatter(x, y, radius=radii, color = 'green', #fill_color='white', fill_alpha=0.5, line_color=None)

p1.background_fill_color = '#333333'
#p1.background_fill_alpha = 0.99
p1.xgrid.grid_line_dash = [6, 4]
p1.xgrid.grid_line_alpha = 0.5
p1.ygrid.grid_line_dash = [6, 4]
p1.ygrid.grid_line_alpha = 0.5

#p1.grid.grid_line_color = "#404040"

#p.image_url(url=['/Users/gretastudier/Desktop/pulsar_image.jpg'], x=42, y=8.5, h=2, w=15)


p2 = figure(x_range=(0,1), y_range=(0,1),plot_width=300, plot_height=300)
p2.image_url(url=['/Users/gretastudier/Desktop/pulsar_image.jpg'], x=0, y=1, h=1, w=1)

output_file("color_scatter.html", title="color_scatter.py example")

show(row(p1, p2))





















# import pandas as pd
#
# from bokeh.io import output_file, show
# from bokeh.layouts import row, widgetbox
# from bokeh.models import Select
# from bokeh.palettes import Spectral5
# from bokeh.plotting import curdoc, figure
# from bokeh.sampledata.autompg import autompg_clean as df
#
# df = df.copy()
#
# SIZES = list(range(6, 22, 3))
# COLORS = Spectral5
#
# # data cleanup
# df.cyl = df.cyl.astype(str)
# df.yr = df.yr.astype(str)
# del df['name']
#
# columns = sorted(df.columns)
# discrete = [x for x in columns if df[x].dtype == object]
# continuous = [x for x in columns if x not in discrete]
# quantileable = [x for x in continuous if len(df[x].unique()) > 20]
#
# def create_figure():
#     xs = df[x.value].values
#     ys = df[y.value].values
#     x_title = x.value.title()
#     y_title = y.value.title()
#
#     kw = dict()
#     if x.value in discrete:
#         kw['x_range'] = sorted(set(xs))
#     if y.value in discrete:
#         kw['y_range'] = sorted(set(ys))
#     kw['title'] = "%s vs %s" % (x_title, y_title)
#
#     p = figure(plot_height=600, plot_width=800, tools='pan,box_zoom,reset', **kw)
#     p.xaxis.axis_label = x_title
#     p.yaxis.axis_label = y_title
#
#     if x.value in discrete:
#         p.xaxis.major_label_orientation = pd.np.pi / 4
#
#     sz = 9
#     if size.value != 'None':
#         groups = pd.qcut(df[size.value].values, len(SIZES))
#         sz = [SIZES[xx] for xx in groups.codes]
#
#     c = "#31AADE"
#     if color.value != 'None':
#         groups = pd.qcut(df[color.value].values, len(COLORS))
#         c = [COLORS[xx] for xx in groups.codes]
#     p.circle(x=xs, y=ys, color=c, size=sz, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5)
#
#     return p
#
#
# def update(attr, old, new):
#     layout.children[1] = create_figure()
#
#
# x = Select(title='X-Axis', value='mpg', options=columns)
# x.on_change('value', update)
#
# y = Select(title='Y-Axis', value='hp', options=columns)
# y.on_change('value', update)
#
# size = Select(title='Size', value='None', options=['None'] + quantileable)
# size.on_change('value', update)
#
# color = Select(title='Color', value='None', options=['None'] + quantileable)
# color.on_change('value', update)
#
# controls = widgetbox([x, y, color, size], width=200)
# layout = row(controls, create_figure())
#
# curdoc().add_root(layout)
# curdoc().title = "Crossfilter"
#
# output_file("test.html")
# #show(create_figure())