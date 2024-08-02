import plotly.graph_objects as go
import numpy as np

def pointpos(x, xsignal):
    if x[xsignal]==1:
        return x['High']+1e-4
    elif x[xsignal]==2:
        return x['Low']-1e-4
    else:
        return np.nan

def plot_with_signal(dfpl):

    fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                    open=dfpl['Open'],
                    high=dfpl['High'],
                    low=dfpl['Low'],
                    close=dfpl['Close'])])

    fig.update_layout(
        autosize=False,
        width=1000,
        height=800,
        paper_bgcolor='black',
        plot_bgcolor='black')
    fig.update_xaxes(gridcolor='black')
    fig.update_yaxes(gridcolor='black')
    fig.add_scatter(x=dfpl.index, y=dfpl['pointpos'], mode="markers",
                    marker=dict(size=8, color="MediumPurple"),
                    name="Signal")
    fig.show()

def plot_graph(dfpl):

    fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                    open=dfpl['Open'],
                    high=dfpl['High'],
                    low=dfpl['Low'],
                    close=dfpl['Close'])])

    fig.update_layout(
        autosize=False,
        width=1000,
        height=800,
        paper_bgcolor='black',
        plot_bgcolor='black')
    fig.update_xaxes(gridcolor='black')
    fig.update_yaxes(gridcolor='black')
    fig.show()


#data['pointpos'] = data.apply(lambda row: pointpos(row,"rejection"), axis=1)
#plot_with_signal(data[10:110])