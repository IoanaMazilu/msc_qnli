hours_premise = 40
hours_hypothesis = 40

# the hypothesis refers to the number of hours of work mentioned in the premise
if hours_hypothesis >= hours_premise:
    # check if the estimate of 'hours_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
