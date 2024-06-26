ratio_premise = [4, 3, 1]
ratio_hypothesis = [4, 3, 1]

# The hypothesis refers to the ratio of red, green, and blue toy bricks used by Gali in building a tower, which is also mentioned in the premise.
if ratio_hypothesis <= ratio_premise:
    # Check if the ratio in the hypothesis contradicts the ratio in the premise.
    label = "contradiction"
else:
    # The premise gives the exact ratio of the bricks.
    # Any ratio less than the 'ratio_premise' is consistent with the hypothesis, but cannot be explicitly entailed from the premise.
    label = "neutral"

print(label)
