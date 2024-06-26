jack_time_premise = 6
lee_time_premise = 10
jack_time_hypothesis = 5
lee_time_hypothesis = 10

# the hypothesis refers to the time taken by Jack and Lee to finish each lap, which is also mentioned in the premise
if jack_time_hypothesis!= jack_time_premise:
    # check if the time taken by Jack in the hypothesis contradicts the time taken by Jack in the premise
    label = "contradiction"
elif lee_time_hypothesis!= lee_time_premise:
    # check if the time taken by Lee in the hypothesis contradicts the time taken by Lee in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
