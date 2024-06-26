work_completion_premise = 20
work_completion_hypothesis = 10

# the hypothesis refers to the completion time of work by Kamal, as mentioned in the premise
if work_completion_hypothesis >= work_completion_premise:
    # check if the estimate of 'work_completion_hypothesis' contradicts the time frame in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
