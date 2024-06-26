share_premise = 600
share_hypothesis = 400

# the hypothesis talks about Greg's share, which is also mentioned in the premise
if share_hypothesis!= share_premise:
    # check if the share in the hypothesis contradicts the share in the premise
    label = "contradiction"
else:
    # if the share in the hypothesis is equal to the share in the premise, it does not entail or contradict the premise
    label = "neutral"

print(label)
