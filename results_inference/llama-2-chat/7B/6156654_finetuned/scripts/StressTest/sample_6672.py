total_time_premise = 1 + 3 = 4
total_time_hypothesis = 5

if total_time_premise!= total_time_hypothesis:
    # check if the total time in the hypothesis contradicts the total time in the premise
    label = "contradiction"
else:
    # if the total time in the hypothesis matches the total time in the premise, we can infer entailment
    label = "entailment"

print(label)
