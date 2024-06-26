work_completion_premise = 30
work_completion_hypothesis = 50

# the hypothesis refers to the time taken by Ram, Krish and Bhim to complete a work, mentioned in the premise
if work_completion_premise >= work_completion_hypothesis:
    # check if the estimate of 'work_completion_hypothesis' contradicts the time taken in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
