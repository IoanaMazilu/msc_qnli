coins_iron_premise = 5
coins_iron_hypothesis = 5
coins_copper_premise = 5
coins_copper_hypothesis = 5

# the hypothesis refers to the number of coins of each kind that Matt has
if coins_iron_premise!= coins_iron_hypothesis:
    # check if the number of iron coins in the hypothesis contradicts the number of iron coins in the premise
    label = "contradiction"
elif coins_copper_premise!= coins_copper_hypothesis:
    # check if the number of copper coins in the hypothesis contradicts the number of copper coins in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
