go_time_premise = 8
go_time_hypothesis = 8

# the hypothesis refers to the time Ana goes, which is also mentioned in the premise
if go_time_hypothesis >= go_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
