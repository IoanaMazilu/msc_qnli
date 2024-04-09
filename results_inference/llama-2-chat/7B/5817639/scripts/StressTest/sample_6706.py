ratio_premise = 8/3/1
ratio_hypothesis = 4/3/1

# the hypothesis talks about the ratio of toy bricks used in the tower, referenced also in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio closer to 4:3:1 than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
