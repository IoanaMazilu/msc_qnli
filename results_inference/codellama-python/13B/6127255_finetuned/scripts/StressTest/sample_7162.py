red_green_blue_ratio_premise = [1, 3, 1]
red_green_blue_ratio_hypothesis = [4, 3, 1]

# the hypothesis refers to the ratio of red, green, and blue toy bricks used in building a tower, which is also mentioned in the premise
if red_green_blue_ratio_hypothesis[0] <= red_green_blue_ratio_premise[0] or red_green_blue_ratio_hypothesis[1] <= red_green_blue_ratio_premise[1] or red_green_blue_ratio_hypothesis[2] <= red_green_blue_ratio_premise[2]:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of red, green, and blue toy bricks
    # any ratio greater than'red_green_blue_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
