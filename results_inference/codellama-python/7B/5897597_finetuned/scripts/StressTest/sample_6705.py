red_green_blue_ratio_premise = [4, 3, 1]
red_green_blue_ratio_hypothesis = [8, 3, 1]

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Yali to build a tower, mentioned in the premise
if red_green_blue_ratio_hypothesis[0] <= red_green_blue_ratio_premise[0] and red_green_blue_ratio_hypothesis[1] == red_green_blue_ratio_premise[1] and red_green_blue_ratio_hypothesis[2] == red_green_blue_ratio_premise[2]:
    # check if the ratio of red, green, and blue toy bricks in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif red_green_blue_ratio_hypothesis[0] < red_green_blue_ratio_premise[0] and red_green_blue_ratio_hypothesis[1] == red_green_blue_ratio_premise[1] and red_green_blue_ratio_hypothesis[2] == red_green_blue_ratio_premise[2]:
    # if the ratio of red, green, and blue toy bricks in the hypothesis is less than the ratio in the premise, we can infer entailment
    label = "entailment"
else:
    # if the ratio of red, green, and blue toy bricks in the hypothesis does not contradict or entail the ratio in the premise, we infer neutrality
    label = "neutral"

print(label)
