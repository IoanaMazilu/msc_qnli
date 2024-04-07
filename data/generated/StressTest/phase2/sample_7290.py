# Premise: 600 and Greg's share is Rs.
# Hypothesis: more than 500 and Greg's share is Rs.
# Golden Label: entailment

greg_share_premise = 600
greg_share_hypothesis = 500

# the hypothesis talks about Greg's share, referenced also in the premise
if greg_share_premise <= greg_share_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'greg_share_premise'
    label = "contradiction"
elif greg_share_premise > greg_share_hypothesis:
    # check if 'greg_share_premise' is greater than 'greg_share_hypothesis', which infers entailment
    label = "entailment"
else:
    # any other case is considered neutral
    label = "neutral"

print(label)

