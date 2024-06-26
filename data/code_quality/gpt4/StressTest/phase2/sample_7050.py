share_premise = 1300
share_hypothesis = 4300

# the hypothesis talks about Deepak's share, mentioned also in the premise
if share_hypothesis <= share_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # since the hypothesis only gives an estimate of Deepak's share without a specific number, 
    # any amount greater than 'share_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
