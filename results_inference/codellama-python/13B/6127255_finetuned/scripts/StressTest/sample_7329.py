red_green_blue_ratio_premise = [4, 3, 1]
red_green_blue_ratio_hypothesis = [3, 3, 1]

# the hypothesis refers to the ratio of red, green, and blue toy bricks used in the tower mentioned in the premise
if red_green_blue_ratio_hypothesis >= red_green_blue_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
