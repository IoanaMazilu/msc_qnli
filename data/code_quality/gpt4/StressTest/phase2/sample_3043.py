parents_participating_premise = 34
parents_participating_hypothesis = 44

# the hypothesis speaks about the number of parents participating in the Smithville PTA, also mentioned in the premise
if parents_participating_hypothesis <= parents_participating_premise:
    # check if the number of parents in the hypothesis contradicts the estimate of more than 'parents_participating_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of parents
    # any number of parents greater than 'parents_participating_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
