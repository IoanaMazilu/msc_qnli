red_green_blue_ratio_premise = 4/3/1
red_green_blue_ratio_hypothesis = 4/3/1

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Gali to build a tower
if red_green_blue_ratio_hypothesis >= red_green_blue_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis is less than the ratio given in the premise, it does not contradict the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)
