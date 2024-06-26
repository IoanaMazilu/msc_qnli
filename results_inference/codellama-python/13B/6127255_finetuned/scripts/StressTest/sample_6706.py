red_green_blue_ratio_premise = [8, 3, 1]
red_green_blue_ratio_hypothesis = [4, 3, 1]

# the hypothesis refers to the ratio of red, green, and blue toy bricks used in Yali's tower, which is also mentioned in the premise
if red_green_blue_ratio_hypothesis[0] / red_green_blue_ratio_hypothesis[1] >= red_green_blue_ratio_premise[0] / red_green_blue_ratio_premise[1]:
    # check if the ratio of red to green toy bricks in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif red_green_blue_ratio_hypothesis[2]!= red_green_blue_ratio_premise[2]:
    # check if the ratio of blue to green toy bricks in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of red, green, and blue toy bricks
    # any ratio less than'red_green_blue_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
