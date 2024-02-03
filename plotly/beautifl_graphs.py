import plotly.express as plotly
import plotly.graph_objs as graph
import plotly.graph_objects as go

""" drow bar char"""

# plot=plotly.bar(x=['D1','D2','D3'], y=[1,2,3])
# plot.show()

"""drow scatter chart"""

# plot = plotly.scatter(x=[2, 2, -2], y=[2, -2, 2])
# plot.show()

""" Drow Pie chart"""

# plot = plotly.pie(labels=['D1','D2','D3'], values=[1,2,3])
# plot.show()

""" Drow Histogram"""
# plot = plotly.histogram(y=[1, 2, 3])
# plot.show()

"""Drow Box Plot"""

# plot = plotly.box(x=[1, 2, 3])
# plot.show()

"""Drow Finnance CadLestrics Chart"""
import plotly.graph_objects as go

plot = go.Figure(
    data=[go.Candlestick(x=[1, 2, 3], open=[1, 2, 3], high=[1, 2, 3], low=[1, 2, 3], close=[1, 2, 3])]
)
plot.show()

