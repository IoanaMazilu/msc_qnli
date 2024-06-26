work_completion_time_premise = 30
work_completion_time_hypothesis = 50

# the hypothesis refers to the time taken by Ram, Krish and Bhim to complete a work, which is also mentioned in the premise
if work_completion_time_hypothesis!= work_completion_time_premise:
    # check if the time taken in the hypothesis contradicts the time taken reported in the premise
    label = "contradiction"
else:
    # if the time taken in the hypothesis does not contradict the time taken in the premise, we can infer entailment
    label = "entailment"

print(label)
