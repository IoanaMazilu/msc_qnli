red_green_blue_ratio_premise = (4, 3, 1)
red_green_blue_ratio_hypothesis = (1, 3, 1)

# the hypothesis refers to the ratio of red, green, and blue toy bricks used to build a tower by Gali, mentioned also in the premise
if red_green_blue_ratio_hypothesis[0] >= red_green_blue_ratio_premise[0]:
    # check if the ratio of red bricks to the others in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise provides a specific ratio for the toy bricks
    # any ratio with less red bricks than 'red_green_blue_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
