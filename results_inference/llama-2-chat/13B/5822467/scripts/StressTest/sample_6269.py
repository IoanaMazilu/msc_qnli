deaths_premise = 10
remainder_premise = 20
deaths_hypothesis = 15

# the hypothesis refers to the percentage of people who died and the remainder who left the village
if deaths_hypothesis > deaths_premise:
    # check if the estimate of 'deaths_hypothesis' contradicts the percentage of people who died in the premise
    label = "contradiction"
elif remainder_premise!= remainder_hypothesis:
    # check if the number of people who left the village in the hypothesis contradicts the number of people who left the village reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
