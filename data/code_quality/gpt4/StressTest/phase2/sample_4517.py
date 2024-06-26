AB_premise = 10
EC_premise = 20
AB_hypothesis = 30
EC_hypothesis = 20

# the hypothesis refers to the lengths of AB and EC mentioned in the premise
if AB_hypothesis != AB_premise:
    # check if the length of AB in the hypothesis contradicts the length of AB reported in the premise
    label = "contradiction"
elif EC_hypothesis != EC_premise:
    # check if the length of EC in the hypothesis contradicts the length of EC reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
