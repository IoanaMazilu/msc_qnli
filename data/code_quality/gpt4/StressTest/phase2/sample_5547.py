mary_age_diff_premise = 12
mary_age_diff_hypothesis = 82

# the hypothesis speaks about the age difference between Mary and Albert, which is also mentioned in the premise
if mary_age_diff_hypothesis < mary_age_diff_premise:
    # check if the hypothesis value contradicts the age difference in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, then it is either entailed by or neutral to the premise
    # in this case, since the age difference in the hypothesis is greater than or equal to the one in the premise, the relation is entailment
    label = "entailment"

print(label)
