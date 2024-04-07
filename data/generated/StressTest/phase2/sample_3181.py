# Premise: more than 5970, then what will be the share of Sameer in the profit?
# Hypothesis: 6970, then what will be the share of Sameer in the profit?
# Golden Label: neutral

share_premise = 5970
share_hypothesis = 6970

# the hypothesis talks about the share of Sameer in the profit, which is also referenced in the premise
if share_hypothesis <= share_premise:
    # check if the hypothesis value contradicts the estimate of more than 'share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the share
    # any share greater than 'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

