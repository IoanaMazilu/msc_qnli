ratio_premise = 4/3
ratio_hypothesis = 4

# the hypothesis refers to the ratio of toy bricks used in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the estimate of 'ratio_hypothesis' contradicts the ratio of toy bricks in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio of toy bricks, and the hypothesis value cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
