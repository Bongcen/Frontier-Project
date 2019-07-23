# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv(
	'frameAnnotationsBULB.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Frontier-Project'

colors = {
    'background': '#fffff',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
		html.H1(
			children='Traffic Light Analysis',
			style={
				'textAlign': 'center',
				'color': colors['text']
			}
		),
		
	html.Div([	
		dcc.RangeSlider(
			id='day-slider',
			min=df['day'].min(),
			max=df['day'].max(),
			step=1,
			marks={
				1: 'Day 1',
				2: 'Night 1',
				3: 'Day 2',
				4: 'Night 2'
			},
			value=[df['day'].min(), df['day'].max()],
		)
	], style={'marginBottom': '3em', 'marginLeft': '1em', 'marginRight': '50em'}, className="row"
	),
	
	html.Div([
		html.Div([
			dcc.Graph(
				id='clustering',
			)  
		])		
	], className="row"),
	
	html.Div([
		html.Div([
			dcc.RadioItems(
				id='RI',
				options=[
					{'label' : i, 'value': i} for i in ['Annotation','RandomForest','kNN','AdaBoost']
					# {'label': 'Random Forest', 'value': 'rf'},
					# {'label': 'kNN', 'value': 'knn'},
					# {'label': 'AdaBoost', 'value': 'ab'}
				],
				value='Annotation',
				labelStyle={'display': 'inline-block'}
			)  
		], style={'width': '25%', 'float': ''}
		)
	], className="row"),
		
	html.Div([
		dcc.Graph(id='bar_plot',
			figure=go.Figure
			(
				data=[
					go.Bar(name='Actual', x=df['Annotation'], y=df['tAnnotation']),
					go.Bar(name='RandomForest', x=df['RandomForest'], y=df['tRandomForest'], text=df['RF']),
					go.Bar(name='kNN', x=df['kNN'], y=df['tkNN'], text=df['RF']),
					go.Bar(name='AdaBoost', x=df['AdaBoost'], y=df['tAdaBoost'], text=df['RF'])
					],
					layout=go.Layout(barmode='group'
						#yaxis = go.layout.YAxis(tickformat = '%')
					)
			
			)
		)
	], className="row")

])

@app.callback(
	Output('clustering', 'figure'),
	[Input('RI', 'value'),
	 Input('day-slider', 'value')])
def update_graph(selected_methods, r_slider):
	
	dff=df[df['day'].isin(r_slider)]
	return {
		'data': [
			go.Scatter(
				x=dff[dff[selected_methods] == i]['No'],
				y=dff[dff[selected_methods] == i][selected_methods],
				text=dff[dff[selected_methods] == i]['day'],
				mode='markers',
				opacity=0.7,
				marker={
					'size': 15,
					'line': {'width': 0.5, 'color': 'white'}
				},
				name = i
			) for i in dff.Annotation.unique()
		],
		'layout': go.Layout(
			xaxis={'type': 'log', 'title': 'Number of Data'},
			yaxis={'title': selected_methods},
			margin={'l': 100, 'b': 100, 't': 25, 'r': 100},
			legend={'x': 0, 'y': 1},
			hovermode='closest'
		)
	}
			
if __name__ == '__main__':
    app.run_server(debug=True)