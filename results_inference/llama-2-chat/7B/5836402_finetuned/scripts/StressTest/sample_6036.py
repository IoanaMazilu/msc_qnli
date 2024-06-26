members_premise = 59
members_hypothesis = 19

# the hypothesis refers to the number of members in Lourdes school class, which is also mentioned in the premise
if members_hypothesis < members_premise:
    # check if the number of members in the hypothesis contradicts the number of members in the premise
    label = "contradiction"
elif members_hypothesis > members_premise:
    # check if the number of members in the hypothesis exceeds the maximum number of members in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
