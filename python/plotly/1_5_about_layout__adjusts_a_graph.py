import plotly.graph_objects as go
# traceによるグラフ登録
# About Layout 
# adjusts a graph
scatter_trace = go.Scatter(x=[1,2,3],y=[3,1,6])
scatter_fig = go.Figure(data=scatter_trace)
data = {
    'width': 300,
    'height': 300
}
layout = go.Layout(width= data['width'],height = data['height'])
fix_size_fig = go.Figure(data=scatter_trace,layout = layout)
fix_size_fig.show()