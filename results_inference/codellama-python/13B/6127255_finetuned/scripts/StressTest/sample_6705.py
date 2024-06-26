red_green_blue_ratio_premise = [4, 3, 1]
red_green_blue_ratio_hypothesis = [8, 3, 1]

# the hypothesis refers to the ratio of red, green, and blue toy bricks used in building a tower, which is also mentioned in the premise
if red_green_blue_ratio_hypothesis[0] <= red_green_blue_ratio_premise[0]:
    # check if the ratio of red toy bricks in the hypothesis contradicts the ratio of red toy bricks in the premise
    label = "contradiction"
elif red_green_blue_ratio_hypothesis[1]!= red_green_blue_ratio_premise[1]:
    # check if the ratio of green toy bricks in the hypothesis contradicts the ratio of green toy bricks in the premise
    label = "contradiction"
elif red_green_blue_ratio_hypothesis[2]!= red_green_blue_ratio_premise[2]:
    # check if the ratio of blue toy bricks in the hypothesis contradicts the ratio of blue toy bricks in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
