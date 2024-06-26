work_completion_time_premise = 8
work_completion_time_hypothesis = 7

# the hypothesis refers to the time of work completion mentioned in the premise
if work_completion_time_premise <= work_completion_time_hypothesis:
    # check if the estimate of 'work_completion_time_hypothesis' contradicts the time of work completion in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
