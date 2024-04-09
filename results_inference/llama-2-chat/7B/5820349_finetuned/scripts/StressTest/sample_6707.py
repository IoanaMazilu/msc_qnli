red_green_blue_ratio_premise = 4/3/1
red_green_blue_ratio_hypothesis = 4/3/1

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Yali to build the tower
if red_green_blue_ratio_hypothesis >= red_green_blue_ratio_premise:
    # check if the hypothesis value contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
