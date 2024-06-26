work_time_premise = 11
work_time_hypothesis = 81

# the hypothesis refers to the time Mary needs to do a piece of work, which is also mentioned in the premise
if work_time_premise >= work_time_hypothesis:
    # check if the estimate of 'work_time_hypothesis' contradicts the time needed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
