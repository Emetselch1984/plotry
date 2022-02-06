import plotly.graph_objects as go
# Interactive operation
# インタラクティブな操作
data1 = {
    "x": [1,2,3],
    "y": [1,5,3],
    "hovertext": ["A社","B社","C社"],
    "name": "bar"
}
scatter = go.Scatter(
    x=data1['x'],y=data1['y'],
    hovertext=data1['hovertext'],
    name=data1['name'])
data2 = {
    "x": [1,2,3],
    "y": [1,2,3],
    "name": "line"
}
bar = go.Bar(x=data2['x'],y=data2['y'],name=data2['name'])
fig3 = go.Figure()
fig3.add_traces([scatter,bar])
fig3.show()