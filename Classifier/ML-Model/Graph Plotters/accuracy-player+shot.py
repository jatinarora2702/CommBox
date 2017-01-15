from plotly.offline import plot
import plotly.graph_objs as go


def main():
	a = [0.882178750429, 0.906965276103,0.758056908105,0.815274391011]

	trace1 = go.Bar(
	    x=['NN', 'SVM', 'DT', 'NB'],
	    y=a,
	    name='PLAYER+SHOT',
	    marker=dict(line=dict(width=0.25))
	)

	data = [trace1]
	layout = go.Layout(
	    title='PLayer + Shot Evaluation 3 Shots',
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

	plot(fig, filename='player+shot-3-shots.html')


if __name__ == '__main__':
	main()
