jogging_hours_premise = 3
jogging_hours_hypothesis = 4

# the hypothesis refers to the total number of hours Aaron spends jogging and walking, which is also mentioned in the premise
if jogging_hours_hypothesis >= jogging_hours_premise:
    # check if the estimate of 'jogging_hours_hypothesis' contradicts the number of hours Aaron spends jogging and walking in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
