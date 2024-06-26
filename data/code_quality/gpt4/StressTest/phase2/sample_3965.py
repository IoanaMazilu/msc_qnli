parents_participating_premise = 41
parents_participating_hypothesis = 41

# the hypothesis talks about the number of parents participating in the committees, which is also referenced in the premise
if parents_participating_hypothesis >= parents_participating_premise:
    # check if the hypothesis value contradicts the estimate of less than 'parents_participating_premise'
    label = "contradiction"
else:
    # the premise gives the exact number of parents participating
    # any number of parents less than 'parents_participating_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
