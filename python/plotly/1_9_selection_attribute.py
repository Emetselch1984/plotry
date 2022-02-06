# selection attribute
import numpy
import plotly.graph_objects as go
numpy.random.seed(1)
data1 = numpy.random.randn(200,200)
data2 = numpy.random.randn(200,200)+1
config1 = {
    "x": data1[0],
    "y": data1[1],
    "name": "A",
    "mode": "markers" 
}
config2 = {
    "x": data2[0],
    "y": data2[1],
    "name": "B",
    "mode": "markers" 
}
scatter_a = go.Scatter(
    x=config1["x"],
    y=config1["y"],
    name=config1["name"],
    mode=config1["mode"])
scatter_b = go.Scatter(
    x=config2["x"],
    y=config2["y"],
    name=config2["name"],
    mode=config2["mode"])
fig = go.Figure()
fig.add_traces([scatter_a,scatter_b])
fig.show()