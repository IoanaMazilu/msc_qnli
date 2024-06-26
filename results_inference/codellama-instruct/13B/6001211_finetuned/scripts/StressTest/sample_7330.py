red_green_blue_ratio_premise = 3/3/1
red_green_blue_ratio_hypothesis = 4/3/1

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Hali to build a tower, which is also mentioned in the premise
if red_green_blue_ratio_hypothesis <= red_green_blue_ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimate of more than'red_green_blue_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of red, green, and blue toy bricks
    # any ratio greater than'red_green_blue_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
