red_bricks_premise = 4
green_bricks_premise = 3
blue_bricks_premise = 1
ratio_premise = 4/3/1
red_bricks_hypothesis = 4
green_bricks_hypothesis = 3
blue_bricks_hypothesis = 1
ratio_hypothesis = 4/3/1

# the hypothesis refers to the ratio of red, green, and blue bricks in the construction of the tower, which is also mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif red_bricks_hypothesis!= red_bricks_premise or green_bricks_hypothesis!= green_bricks_premise or blue_bricks_hypothesis!= blue_bricks_premise:
    # check if the number of red, green, or blue bricks in the hypothesis contradicts the number of each kind of bricks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
