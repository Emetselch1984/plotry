from turtle import width
import plotly.graph_objects as go
fig = go.Figure()
fig.show()

# traceによるグラフ登録
# About Trace 
# register a graph

scatter_trace = go.Scatter(x=[1,2,3],y=[3,1,6])
scatter_fig = go.Figure(data=scatter_trace)
scatter_fig.show()

data = {
    'x': [1,2,3],
    'y': [4,3,1]
}
bar_tarace = go.Bar(x=data['x'],y=data['y'])
scatter_bar_fig = go.Figure(data=[scatter_trace,bar_tarace])
scatter_bar_fig.show()

# traceによるグラフ登録
# About Layout 
# adjusts a graph
data = {
    'width': 300,
    'height': 300
}
layout = go.Layout(width= data['width'],height = data['height'])
fix_size_fig = go.Figure(data=scatter_trace,layout = layout)
fix_size_fig.show()