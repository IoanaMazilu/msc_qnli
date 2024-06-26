parents_premise = 22
parents_hypothesis = 42

# the hypothesis talks about the number of parents in the PTA, referenced also in the premise
if parents_hypothesis <= parents_premise:
    # check if the hypothesis value contradicts the estimate of more than 'parents_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of parents
    # any number of parents greater than 'parents_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
