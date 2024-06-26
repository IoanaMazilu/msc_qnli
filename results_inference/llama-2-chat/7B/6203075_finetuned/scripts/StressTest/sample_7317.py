jim_stretch_time_premise = 18
jim_stretch_time_hypothesis = 78

# the hypothesis refers to the time Jim takes to stretch, which is also mentioned in the premise
if jim_stretch_time_hypothesis <= jim_stretch_time_premise:
    # check if the hypothesis value contradicts the time Jim takes to stretch in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
