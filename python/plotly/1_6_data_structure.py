import plotly.graph_objects as go
fig = go.Figure()
fig.to_json()[:80]
fig.to_json()[80:]
fig.to_json()[:]