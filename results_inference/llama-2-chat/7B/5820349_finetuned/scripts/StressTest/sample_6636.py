work_completion_time_premise = 30
work_completion_time_hypothesis = 50

# the hypothesis refers to the time taken by Ram, Krish and Bhim to complete a work, which is also mentioned in the premise
if work_completion_time_hypothesis < work_completion_time_premise:
    # check if the hypothesis value contradicts the time taken in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
