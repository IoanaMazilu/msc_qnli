parents_premise = 88
parents_hypothesis = 38

# the hypothesis talks about the number of participating parents in the Smithville PTA, referenced also in the premise
if parents_hypothesis >= parents_premise:
    # check if the hypothesis value contradicts the estimate of less than 'parents_premise'
    label = "contradiction"
elif parents_hypothesis < parents_premise:
    # the premise gives only an estimate for the number of parents
    # any number of parents less than 'parents_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
