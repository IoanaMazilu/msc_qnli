parents_premise = 42
parents_hypothesis = 42

# the hypothesis talks about the number of parents participating in the Smithville PTA, referenced also in the premise
if parents_hypothesis >= parents_premise:
    # check if the hypothesis value contradicts the estimate of less than 'parents_hypothesis'
    label = "contradiction"
else:
    # the premise gives a specific number for the parents
    # any number of parents less than 'parents_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)