work_completion_premise = 8
work_completion_hypothesis = 7

# the hypothesis refers to the number of days they took to complete the work, mentioned in the premise
if work_completion_premise <= work_completion_hypothesis:
    # check if the estimate of 'work_completion_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
