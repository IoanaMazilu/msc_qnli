red_green_blue_ratio_premise = 3/3/1
red_green_blue_ratio_hypothesis = 4/3/1

# the hypothesis talks about the ratio of red, green and blue toy bricks in the tower, referenced also in the premise
if red_green_blue_ratio_hypothesis <= red_green_blue_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than'red_green_blue_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
