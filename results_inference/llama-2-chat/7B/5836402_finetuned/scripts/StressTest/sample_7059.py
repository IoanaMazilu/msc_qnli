time_difference_premise = 90
time_difference_hypothesis = 20

# the hypothesis refers to the time difference between Dan's departure from City A and Cara's departure, mentioned in the premise
if time_difference_hypothesis >= time_difference_premise:
    # check if the estimate of 'time_difference_hypothesis' contradicts the time difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
