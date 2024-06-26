share_premise = 1300
share_hypothesis = float(less_than_1300)

# the hypothesis talks about Deepak's share, which is also referred to in the premise
if share_hypothesis <= share_premise:
    # check if the hypothesis value contradicts the estimate of Deepak's share in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Deepak's share
    # any number of Deepak's share less than or equal to'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
