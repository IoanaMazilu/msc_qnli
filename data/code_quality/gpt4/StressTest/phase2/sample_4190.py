karen_share_premise = 1100
karen_share_hypothesis = 1100

# the hypothesis talks about the share of Karen, also referenced in the premise
if karen_share_hypothesis > karen_share_premise:
    # check if the hypothesis value contradicts the exact amount of 'karen_share_premise'
    label = "contradiction"
elif karen_share_hypothesis < karen_share_premise:
    # check if the hypothesis value contradicts the exact amount of 'karen_share_premise'
    label = "contradiction"
else:
    # the premise gives the exact amount for Karen's share
    # an equal amount in the hypothesis can be explicitly entailed from the premise
    label = "entailment"

print(label)
