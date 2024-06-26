red_green_blue_ratio_premise = [4, 3, 1]
red_green_blue_ratio_hypothesis = [4, 3, 1]

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Yali, which is also mentioned in the premise
if red_green_blue_ratio_hypothesis >= red_green_blue_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis is less than the ratio in the premise, it can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)
