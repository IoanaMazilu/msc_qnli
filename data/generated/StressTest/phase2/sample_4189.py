# Premise: less than 8100 and Karen's share is Rs.
# Hypothesis: 1100 and Karen's share is Rs.
# Golden Label: neutral

karen_share_premise = 8100
karen_share_hypothesis = 1100

# the hypothesis talks about Karen's share which is also mentioned in the premise
if karen_share_hypothesis >= karen_share_premise:
    # check if the hypothesis value contradicts the estimate of less than 'karen_share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Karen's share
    # any share less than 'karen_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

