share_sravan_premise = 0
share_sravan_hypothesis = 75

# the hypothesis talks about the share of Sravan, referenced also in the premise
if share_sravan_hypothesis <= share_sravan_premise:
    # check if the hypothesis value contradicts the estimate of'share_sravan_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the share of Sravan
    # any share of Sravan greater than'share_sravan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
