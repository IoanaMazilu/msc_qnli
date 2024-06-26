share_premise = 600
share_hypothesis = 500

# the hypothesis refers to the share mentioned in the premise
if share_premise <= share_hypothesis:
    # check if the premise share is less than or equal to the hypothesis share
    label = "neutral"
elif share_premise > share_hypothesis:
    # check if the premise share is greater than the hypothesis share
    label = "entailment"
else:
    # if the hypothesis share is less than the premise share, it contradicts the premise
    label = "contradiction"

print(label)
