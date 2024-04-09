ratio_red_green_blue_premise = 8/3/1
ratio_red_green_blue_hypothesis = 4/3/1

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Yali, also mentioned in the premise
if ratio_red_green_blue_hypothesis >= ratio_red_green_blue_premise:
    # check if the ratio in the hypothesis contradicts the estimate of less than 'ratio_red_green_blue_premise'
    label = "contradiction"
elif ratio_red_green_blue_hypothesis == ratio_red_green_blue_premise:
    # check if the ratio in the hypothesis matches exactly the ratio given in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the ratio of red, green, and blue toy bricks
    # any ratio less than 'ratio_red_green_blue_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
