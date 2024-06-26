brick_ratio_premise = 1/3/1
brick_ratio_hypothesis = 4/3/1

# the hypothesis talks about the ratio of toy bricks used by Gali to build a tower, referenced also in the premise
if brick_ratio_hypothesis <= brick_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'brick_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of toy bricks
    # any ratio greater than 'brick_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
