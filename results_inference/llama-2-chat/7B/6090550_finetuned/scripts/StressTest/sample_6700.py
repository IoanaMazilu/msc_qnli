share_premise = 6500
share_hypothesis = 4500

# the hypothesis talks about the share of Tony, which is also mentioned in the premise
if share_hypothesis >= share_premise:
    # check if the hypothesis value contradicts the estimate of less than'share_premise'
    label = "contradiction"
elif share_hypothesis < share_premise:
    # the premise gives an estimate of less than'share_premise'
    # the hypothesis value is less than this estimate, so it's consistent with the premise
    label = "entailment"
else:
    # if the hypothesis value is exactly'share_premise', it's neutral
    label = "neutral"

print(label)
