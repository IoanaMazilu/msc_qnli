red_green_blue_ratio_premise = 4/3/1
red_green_blue_ratio_hypothesis = 8/3/1

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Yali to build a tower
if red_green_blue_ratio_hypothesis <= red_green_blue_ratio_premise:
    # check if the hypothesis ratio contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)
