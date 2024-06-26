work_completion_time_premise = 30
work_completion_time_hypothesis = 50

# the hypothesis refers to the time taken by Ram, Krish and Bhim to complete a work, mentioned in the premise
if work_completion_time_premise > work_completion_time_hypothesis:
    # check if the time taken in the premise contradicts the time taken in the hypothesis
    label = "contradiction"
elif work_completion_time_premise < work_completion_time_hypothesis:
    # check if the time taken in the premise is less than the time taken in the hypothesis
    label = "entailment"
else:
    # if the time taken in the premise is equal to the time taken in the hypothesis, we can infer neutrality
    label = "neutral"

print(label)
