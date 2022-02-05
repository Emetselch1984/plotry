import plotly.graph_objects as go
scatter_trace = go.Scatter(x=[1,2,3],y=[3,1,6])
scatter_fig = go.Figure(data=scatter_trace)
scatter_fig.show()
