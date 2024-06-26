bond_denomination_premise = [50, 100]
bond_denomination_hypothesis = [70, 100]

# the hypothesis refers to the denomination of bonds that Robert purchased, which is also mentioned in the premise
if bond_denomination_hypothesis[0] < bond_denomination_premise[0]:
    # check if the denomination of bonds in the hypothesis contradicts the premise
    label = "contradiction"
elif bond_denomination_hypothesis[1]!= bond_denomination_premise[1]:
    # check if the denomination of bonds in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
