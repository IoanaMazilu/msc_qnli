jack_lap_premise = 6
jack_lap_hypothesis = 5
lee_lap_premise = 10
lee_lap_hypothesis = 10

# the hypothesis refers to the time it takes for Jack and Lee to finish each lap
if jack_lap_hypothesis <= jack_lap_premise and lee_lap_hypothesis <= lee_lap_premise:
    # the hypothesis values are consistent with the premise values
    label = "neutral"
elif jack_lap_hypothesis > jack_lap_premise or lee_lap_hypothesis > lee_lap_premise:
    # the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the hypothesis values do not contradict the premise values, but we cannot infer entailment
    label = "entailment"

print(label)
