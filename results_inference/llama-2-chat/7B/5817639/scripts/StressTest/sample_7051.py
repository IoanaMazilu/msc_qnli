less_than_4300_premise = 4300
deepak_share_premise = None

# the premise gives a number (4300) and a blank for Deepak's share
# the hypothesis gives a number (1300) for Deepak's share

if deepak_share_premise is None:
    # if the premise does not provide a value for Deepak's share, we cannot make any comparison
    label = "neutral"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    if deepak_share_hypothesis < deepak_share_premise:
        label = "entailment"
    # if the hypothesis value is greater than or equal to the premise value, we can infer contradiction
    elif deepak_share_hypothesis >= deepak_share_premise:
        label = "contradiction"
    # if the hypothesis value is null or missing, we cannot make any comparison
    else:
        label = "neutral"

print(label)
