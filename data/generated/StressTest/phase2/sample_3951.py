# Premise: 6970, then what will be the share of Sameer in the profit?
# Hypothesis: more than 2970, then what will be the share of Sameer in the profit?
# Golden Label: entailment

sameer_share_premise = 6970
sameer_share_hypothesis = 2970

# the hypothesis talks about the share of Sameer in profit, referenced also in the premise
if sameer_share_hypothesis >= sameer_share_premise:
    # check if the hypothesis value contradicts the estimate of 'sameer_share_premise'
    label = "contradiction"
elif sameer_share_hypothesis == sameer_share_premise:
    # check if the number of Sameer's share in the hypothesis contradicts the number of Sameer's share reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the share of Sameer
    # any share of Sameer less than 'sameer_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

