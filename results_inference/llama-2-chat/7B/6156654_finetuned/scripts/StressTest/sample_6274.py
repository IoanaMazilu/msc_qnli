jack_lap_time_premise = 5
lee_lap_time_premise = 10
jack_lap_time_hypothesis = 6
lee_lap_time_hypothesis = 10

# the hypothesis talks about the time it takes Jack and Lee to finish a lap, which is also mentioned in the premise
if jack_lap_time_hypothesis <= jack_lap_time_premise and lee_lap_time_hypothesis <= lee_lap_time_premise:
    # check if the time it takes Jack and Lee to finish a lap in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
elif jack_lap_time_hypothesis > jack_lap_time_premise or lee_lap_time_hypothesis > lee_lap_time_premise:
    # check if the time it takes Jack and Lee to finish a lap in the hypothesis is greater than the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
