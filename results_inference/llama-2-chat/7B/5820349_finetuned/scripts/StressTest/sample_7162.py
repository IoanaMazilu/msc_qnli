ratio_red_green_blue_premise = 1
ratio_red_green_blue_hypothesis = 4

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Gali, mentioned also in the premise
if ratio_red_green_blue_hypothesis <= ratio_red_green_blue_premise:
    # check if the ratio in the hypothesis contradicts the estimate of more than 'ratio_red_green_blue_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of red, green, and blue toy bricks
    # any ratio greater than 'ratio_red_green_blue_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
