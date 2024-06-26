share_sravan_premise = 25
share_sravan_hypothesis = 75

if share_sravan_hypothesis <= share_sravan_premise:
    # check if the hypothesis value contradicts the estimate of more than'share_sravan_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
