from plotly.offline import plot
import plotly.graph_objs as go


def main():
	a = [0.856018340036, 0.862756240927,0.748130157144,0.81080440732]
	b = [0.805962863806, 0.809440125176,0.744270015786,0.838877819027]
	c = [0.765146121384, 0.694962181608,0.684451484575,0.756845275775]
	d = [0.862449283295, 0.89574799505,0.759306858476,0.834557907554]
	e = [0.817534292378, 0.844487744223,0.791132528974,0.867160967135]


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
	    title='Evaluation 5 Shots',
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

	plot(fig, filename='5-shots.html')


if __name__ == '__main__':
	main()
