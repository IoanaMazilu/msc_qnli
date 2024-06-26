well_digging_time_premise = 8
well_digging_time_hypothesis = 4

# the hypothesis refers to the time Jake, Paul and Hari take to dig a well, which is also mentioned in the premise
if well_digging_time_hypothesis != well_digging_time_premise:
    # check if the time to dig the well in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
