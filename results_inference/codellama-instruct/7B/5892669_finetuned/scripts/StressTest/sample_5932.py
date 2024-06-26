herd_division_premise_min = 4
herd_division_premise_max = 6
herd_division_premise_not = 9

herd_division_hypothesis_min = 5
herd_division_hypothesis_max = 6
herd_division_hypothesis_not = 9

# the hypothesis refers to the number of equal parts Antony can divide his herd into, as mentioned in the premise
if herd_division_hypothesis_min < herd_division_premise_min or herd_division_hypothesis_max > herd_division_premise_max or herd_division_hypothesis_not == herd_division_premise_not:
    # check if the hypothesis contradicts the premise's limits for dividing the herd
    label = "contradiction"
elif herd_division_hypothesis_min > herd_division_premise_min and herd_division_hypothesis_max < herd_division_premise_max:
    # check if the hypothesis is within the premise's limits but not equal
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
