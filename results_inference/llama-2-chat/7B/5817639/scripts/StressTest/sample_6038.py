members_premise = 59
members_hypothesis = "more than 59"

# the hypothesis refers to the number of members in the class, which is greater than the premise value
if members_hypothesis <= members_premise:
    # check if the estimate of'members_hypothesis' contradicts the number of members in the premise
    label = "contradiction"
elif members_hypothesis > members_premise:
    # the premise gives only an estimate for the number of members, and any number greater than that is consistent with the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
