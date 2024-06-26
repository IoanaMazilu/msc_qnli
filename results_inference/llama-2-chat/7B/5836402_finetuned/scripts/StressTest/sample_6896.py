days_walked_premise = 3
days_walked_hypothesis = 6

# the hypothesis refers to the number of days Alice walked, mentioned in the premise
if days_walked_premise!= days_walked_hypothesis:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
