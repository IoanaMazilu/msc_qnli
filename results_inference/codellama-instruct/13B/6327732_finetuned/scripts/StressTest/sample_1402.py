share_sravan_premise = 25
share_sravan_hypothesis = 75

# the hypothesis refers to the number of days it takes for Sreedhar to complete the work
if share_sravan_hypothesis <= share_sravan_premise:
    # check if the estimate of'share_sravan_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than'share_sravan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
