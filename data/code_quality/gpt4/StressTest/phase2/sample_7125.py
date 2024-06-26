total_hours_premise = 3
total_hours_hypothesis = 1

# the hypothesis refers to the total jogging and walking hours mentioned in the premise
if total_hours_hypothesis >= total_hours_premise:
    # check if the estimate of 'total_hours_hypothesis' contradicts the total hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)