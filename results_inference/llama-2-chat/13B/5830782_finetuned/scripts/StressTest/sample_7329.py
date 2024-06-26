red_bricks_premise = 4
green_bricks_premise = 3
blue_bricks_premise = 1

red_bricks_hypothesis = 3
green_bricks_hypothesis = 3
blue_bricks_hypothesis = 1

# the hypothesis refers to the ratio of red, green, and blue toy bricks used to build the tower
if red_bricks_hypothesis > red_bricks_premise:
    # check if the ratio of red bricks in the hypothesis contradicts the ratio of red bricks in the premise
    label = "contradiction"
elif green_bricks_hypothesis!= green_bricks_premise or blue_bricks_hypothesis!= blue_bricks_premise:
    # check if the ratios of green and blue bricks in the hypothesis contradict the ratios of green and blue bricks in the premise
    label = "contradiction"
else:
    # if the ratios in the hypothesis do not contradict the ratios in the premise, we can infer entailment
    label = "entailment"

print(label)
