licorice_sticks_premise = 25
licorice_sticks_hypothesis = 25

# the hypothesis refers to the number of licorice sticks Sally bought, mentioned also in the premise
if licorice_sticks_hypothesis < licorice_sticks_premise:
    # the hypothesis states that Sally bought less than 'licorice_sticks_premise' licorice sticks
    # this is consistent with the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"
elif licorice_sticks_hypothesis > licorice_sticks_premise:
    # check if the number of licorice sticks in the hypothesis contradicts the number of licorice sticks in the premise
    label = "contradiction"
else:
    # if the hypothesis value and the premise value are exactly the same, we can infer entailment
    label = "entailment"

print(label)
