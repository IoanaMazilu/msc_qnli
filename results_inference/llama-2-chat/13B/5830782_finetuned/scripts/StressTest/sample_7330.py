ratio_premise = 3/3/1
ratio_hypothesis = 4/3/1

# the hypothesis talks about the ratio of the toy bricks used in building the tower, referenced also in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the toy bricks
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
