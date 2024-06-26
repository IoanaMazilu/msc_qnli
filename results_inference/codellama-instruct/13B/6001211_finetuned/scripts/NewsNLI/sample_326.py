sailors_hurt_premise = 15
sailors_hurt_hypothesis = 15
vessels_damaged_premise = 2
vessels_damaged_hypothesis = 2

# the hypothesis mentions the number of sailors hurt and the number of vessels damaged, which are also mentioned in the premise
if sailors_hurt_hypothesis!= sailors_hurt_premise:
    # check if the number of hurt sailors in the hypothesis contradicts the number of hurt sailors reported in the premise
    label = "contradiction"
elif vessels_damaged_hypothesis!= vessels_damaged_premise:
    # check if the number of damaged vessels from the hypothesis contradicts the number of damaged vessels in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
