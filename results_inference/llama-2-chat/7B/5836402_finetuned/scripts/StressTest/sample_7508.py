pat_stretch_time_premise = 20
pat_stretch_time_hypothesis = 80

# the hypothesis refers to the time Pat spends stretching, which is also mentioned in the premise
if pat_stretch_time_hypothesis!= pat_stretch_time_premise:
    # check if the time Pat spends stretching in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
