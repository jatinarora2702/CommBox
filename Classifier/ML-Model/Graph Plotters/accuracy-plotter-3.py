from plotly.offline import plot
import plotly.graph_objs as go


def main():
	a = [0.916768416768,  0.908389295889, 0.819810744811, 0.89620980871]
	b = [0.854873829874,  0.888008750509, 0.784966422466, 0.841778591779]
	c = [0.792628205128,  0.822323972324, 0.785342897843, 0.787998575499]
	d = [0.937688237688,  0.965211640212, 0.861202686203, 0.882661782662]
	e = [0.862016687017,  0.895614570615, 0.810785510786, 0.910317460317]


	trace1 = go.Bar(
	    x=['NN', 'SVM', 'DT', 'NB'],
	    y=a,
	    name='GYRO'
	)
	trace2 = go.Bar(
	    x=['NN', 'SVM', 'DT', 'NB'],
	    y=b,
	    name='ACC'
	)
	trace3 = go.Bar(
	    x=['NN', 'SVM', 'DT', 'NB'],
	    y=c,
	    name='COMP'
	)
	trace4= go.Bar(
	    x=['NN', 'SVM', 'DT', 'NB'],
	    y=d,
	    name='GYRO + COMP'
	)

	trace5= go.Bar(
	    x=['NN', 'SVM', 'DT', 'NB'],
	    y=e,
	    name='ACC + GYRO'
	)

	data = [trace1, trace2, trace3, trace4, trace5]
	layout = go.Layout(
	    title='Evaluation 3 Shots',
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
	        titlefont=dict(
	            family='Courier New, monospace',
	            size=18,
	            color='#7f7f7f'
	        )
	    ),
	    barmode='group'
	)
	fig = go.Figure(data=data, layout=layout)

	plot(fig, filename='3-shots.html')


if __name__ == '__main__':
	main()
