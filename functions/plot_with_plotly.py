import plotly.plotly as py
import plotly.graph_objs as go


def plot(generation, std, avg, mins, maxes, number_of_iterations, number_of_items,
         mutate_probability, cross_over_probability, the_population_cardinality):
    trace_std = go.Scatter(
        x=generation,
        y=std,
        name="Standard deviation"
    )
    trace_avg = go.Scatter(
        x=generation,
        y=avg,
        name="Average"
    )
    trace_min = go.Scatter(
        x=generation,
        y=mins,
        name="Min"
    )
    trace_max = go.Scatter(
        x=generation,
        y=maxes,
        name="Max"
    )

    layout = go.Layout(
        title='Genetic algorithm statistics iter= ' +
              repr(number_of_iterations) + ', items= ' + repr(number_of_items) +
              ", Mutation probability= " + repr(mutate_probability / 10) + "%, " +
              "Crossing over probability= " + repr(cross_over_probability) + "%." +
              "<br></br>Population cardinality= " + repr(the_population_cardinality) + "."
        ,
        xaxis=dict(
            title='generation',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    data = [trace_std, trace_avg, trace_min, trace_max]
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='GeneticAlgorithm')
