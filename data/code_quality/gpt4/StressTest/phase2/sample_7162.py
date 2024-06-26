red_green_blue_ratio_premise = (1, 3, 1)
red_green_blue_ratio_hypothesis = (4, 3, 1)

# the hypothesis talks about the ratio of red, green and blue toy bricks, referenced also in the premise
if red_green_blue_ratio_hypothesis[0] <= red_green_blue_ratio_premise[0] or \
   red_green_blue_ratio_hypothesis[2] <= red_green_blue_ratio_premise[2]:
    # check if the hypothesis ratio contradicts the estimate of more than '1:3:1'
    label = "contradiction"
elif red_green_blue_ratio_hypothesis[1] != red_green_blue_ratio_premise[1]:
    # check if the number of green bricks in the hypothesis contradicts the number of green bricks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the bricks
    # any ratio of bricks greater than '1:3:1' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
