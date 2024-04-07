# Premise: 1100 and Karen's share is Rs.
# Hypothesis: less than 8100 and Karen's share is Rs.
# Golden Label: entailment

karen_share_premise = 1100
karen_share_hypothesis = 8100

# the hypothesis talks about Karen's share, which is also mentioned in the premise
if karen_share_premise >= karen_share_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif karen_share_hypothesis > karen_share_premise:
    # the premise provides the exact amount for Karen's share
    # any amount greater than 'karen_share_premise' is not explicitly mentioned in the premise, therefore it is neutral
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise value, then it is an entailment
    label = "entailment"

print(label)

