pie_baking_time_premise = 5
pie_baking_time_hypothesis = 5

# the hypothesis talks about the time Alice needs to bake a pie, which is also mentioned in the premise
if pie_baking_time_hypothesis > pie_baking_time_premise:
    # check if the hypothesis time contradicts the exact time mentioned in the premise
    label = "contradiction"
elif pie_baking_time_hypothesis == pie_baking_time_premise:
    # if the hypothesis time matches the premise time, we can infer entailment
    label = "entailment"
else:
    # any time less than 'pie_baking_time_premise' is consistent with the premise
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
