pairs_premise = 70
pairs_hypothesis = 10

# the hypothesis talks about the number of pairs of matched socks, which is also mentioned in the premise
if pairs_hypothesis >= pairs_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif pairs_hypothesis < pairs_premise:
    # check if the hypothesis value is less than the premise value, which means it is consistent with the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
