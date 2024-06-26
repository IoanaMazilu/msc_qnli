total_time_premise = 3
total_time_hypothesis = 4

# the hypothesis refers to the total time for jogging and walking, which is also mentioned in the premise
if total_time_hypothesis <= total_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
