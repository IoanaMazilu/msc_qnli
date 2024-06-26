work_time_premise = 11
work_time_hypothesis = 11

# the hypothesis refers to the time Mary needs to do a piece of work, which is also mentioned in the premise
if work_time_hypothesis <= work_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
