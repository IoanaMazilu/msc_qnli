work_completion_time_premise = 12
work_completion_time_hypothesis = 22

# the hypothesis refers to the time taken by Rohit and Rohan to complete a work, as mentioned in the premise
if work_completion_time_premise > work_completion_time_hypothesis:
    # check if the time taken by Rohit and Rohan in the premise contradicts the estimate of less than 'work_completion_time_hypothesis'
    label = "contradiction"
else:
    # if the time taken by Rohit and Rohan in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
