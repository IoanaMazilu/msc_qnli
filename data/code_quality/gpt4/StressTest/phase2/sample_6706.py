# define ratio values for the premise and hypothesis
red_green_blue_ratio_premise = 8
red_green_blue_ratio_hypothesis = 4

# the hypothesis refers to the ratio of used toy bricks colors mentioned in the premise
if red_green_blue_ratio_hypothesis >= red_green_blue_ratio_premise:
    # check if the ratio of 'red_green_blue_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of toy bricks colors
    # any ratio less than 'red_green_blue_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
