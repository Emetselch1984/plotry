# traceによるグラフ登録
# About Trace 
# register a graph
import plotly.graph_objects as go
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