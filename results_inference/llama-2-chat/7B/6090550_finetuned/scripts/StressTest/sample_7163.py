red_bricks_premise = 4
green_bricks_premise = 3
blue_bricks_premise = 1
red_bricks_hypothesis = 4
green_bricks_hypothesis = 3
blue_bricks_hypothesis = 1

# the hypothesis refers to the ratio of red, green and blue bricks in the tower construction
if red_bricks_premise >= red_bricks_hypothesis:
    # check if the ratio of red bricks in the premise contradicts the hypothesis
    label = "contradiction"
elif green_bricks_premise!= green_bricks_hypothesis or blue_bricks_premise!= blue_bricks_hypothesis:
    # check if the ratio of green or blue bricks contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
