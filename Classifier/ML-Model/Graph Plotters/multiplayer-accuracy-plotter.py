from plotly.offline import plot
import plotly.graph_objs as go


def main():
	a = [0.415019762846, 0.494071146245,0.466403162055,0.332015810277]
	b = [0.466666666667, 0.452380952381,0.238095238095,0.485714285714]

	trace1 = go.Bar(
	    x=['NN', 'SVM', 'DT', 'NB'],
	    y=a,
	    name='TRAIN-1 TEST-2',
	    marker=dict(line=dict(width=0.7))
	)
	trace2 = go.Bar(
	    x=['NN', 'SVM', 'DT', 'NB'],
	    y=b,
	    name='TRAIN-2 TEST-1',
	    marker=dict(line=dict(width=0.7))
	)

	data = [trace1, trace2]
	layout = go.Layout(
	    title='Multiplayer Evaluation 3 Shots',
	    xaxis=dict(
	        title='Classifiers',
	        titlefont=dict(
	            family='Courier New, monospace',
	            size=18,
	            color='#7f7f7f'
	        )
	    ),
	    yaxis=dict(
	        title='Accuracy',
	        range=[0,1],
	        titlefont=dict(
	            family='Courier New, monospace',
	            size=18,
	            color='#7f7f7f'
	        )
	    ),
	    barmode='group'
	)
	fig = go.Figure(data=data, layout=layout)

	plot(fig, filename='multiplayer-3-shots.html')


if __name__ == '__main__':
	main()
