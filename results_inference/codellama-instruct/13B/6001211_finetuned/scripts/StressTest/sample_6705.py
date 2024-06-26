red_green_blue_ratio_premise = [4, 3, 1]
red_green_blue_ratio_hypothesis = [8, 3, 1]

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Yali to build a tower, which is also mentioned in the premise
if red_green_blue_ratio_hypothesis <= red_green_blue_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio given in the premise, we can infer entailment
    label = "entailment"

print(label)
