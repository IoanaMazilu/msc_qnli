red_green_blue_ratio_premise = 3/3/1
red_green_blue_ratio_hypothesis = 4/3/1

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Hali in building a tower
if red_green_blue_ratio_hypothesis <= red_green_blue_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only a lower bound for the ratio
    # any ratio greater than'red_green_blue_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)