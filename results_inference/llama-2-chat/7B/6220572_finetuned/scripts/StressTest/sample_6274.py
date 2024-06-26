lap_time_premise = 5
lap_time_hypothesis = 6
lap_time_lee_premise = 10
lap_time_lee_hypothesis = 10

# the hypothesis refers to the time taken by Jack and Lee to finish a lap, also mentioned in the premise
if lap_time_hypothesis <= lap_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'lap_time_premise'
    label = "contradiction"
elif lap_time_lee_hypothesis!= lap_time_lee_premise:
    # check if the number of laps in the hypothesis contradicts the number of laps reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
