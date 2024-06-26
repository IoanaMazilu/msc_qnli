total_hours_premise = 4
total_hours_hypothesis = 3

# the hypothesis refers to the total hours of jogging and walking mentioned in the premise
if total_hours_hypothesis >= total_hours_premise:
    # check if the estimate of 'total_hours_hypothesis' contradicts the number of total hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)