deepak_share_premise = 1000
deepak_share_hypothesis = 1300

# the hypothesis talks about the number of roses in a vase, referenced also in the premise
if deepak_share_hypothesis <= deepak_share_premise:
    # check if the hypothesis value contradicts the estimate of more than 'deepak_share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'deepak_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
