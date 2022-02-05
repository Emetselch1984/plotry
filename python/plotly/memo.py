import plotly.graph_objects as go
fig = go.Figure()
fig.show()

# traceによるグラフ登録
# About Trace 
# register a graph

scatter_trace = go.Scatter(x=[1,2,3],y=[3,1,6])
scatter_fig = go.Figure(data=scatter_trace)
scatter_fig.show