jack_lap_time_premise = 6
lee_lap_time_premise = 10
jack_lap_time_hypothesis = 5
lee_lap_time_hypothesis = 10

# the hypothesis refers to the time Jack and Lee take to finish each lap, mentioned in the premise
if jack_lap_time_hypothesis!= jack_lap_time_premise:
    # check if the time Jack takes to finish a lap in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
elif lee_lap_time_hypothesis!= lee_lap_time_premise:
    # check if the time Lee takes to finish a lap in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
