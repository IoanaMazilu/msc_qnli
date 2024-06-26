members_premise = 59
members_hypothesis = 59

# the hypothesis refers to the number of members in the school class mentioned in the premise
if members_hypothesis <= members_premise:
    # check if the hypothesis value contradicts the number of members in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
