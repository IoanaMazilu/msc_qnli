red_green_blue_ratio_premise = [4, 3, 1]
red_green_blue_ratio_hypothesis = [3, 3, 1]

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Hali in building a tower, mentioned in the premise
if red_green_blue_ratio_premise[0] <= red_green_blue_ratio_hypothesis[0]:
    # check if the ratio of red to green and blue bricks in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif red_green_blue_ratio_premise[1]!= red_green_blue_ratio_hypothesis[1] or red_green_blue_ratio_premise[2]!= red_green_blue_ratio_hypothesis[2]:
    # check if the ratio of green to blue bricks in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
