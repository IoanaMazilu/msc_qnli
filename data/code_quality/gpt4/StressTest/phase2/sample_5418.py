andres_share_premise = 250
andres_share_hypothesis = 550

# the hypothesis talks about Andre's share, which is also referenced in the premise
if andres_share_premise >= andres_share_hypothesis:
    # check if the premise value contradicts the estimate of less than 'andres_share_hypothesis'
    label = "contradiction"
elif andres_share_premise == andres_share_hypothesis:
    # check if the premise value entails the hypothesis value
    label = "entailment"
else:
    # the hypothesis gives only an estimate for Andre's share
    # any share less than 'andres_share_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
