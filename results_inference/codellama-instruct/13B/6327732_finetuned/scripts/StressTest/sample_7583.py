share_sravan_premise = 75
share_sravan_hypothesis = 75

# the hypothesis refers to the number of days it takes for Sreedhar to do the work, which is also mentioned in the premise
if share_sravan_hypothesis <= share_sravan_premise:
    # check if the estimate of'share_sravan_hypothesis' contradicts the number of days it takes for Sreedhar to do the work in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days it takes for Sreedhar to do the work
    # any number of days greater than'share_sravan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
