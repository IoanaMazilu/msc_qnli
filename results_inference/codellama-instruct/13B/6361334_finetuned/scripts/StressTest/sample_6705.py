red_bricks_premise = 4
green_bricks_premise = 3
blue_bricks_premise = 1

red_bricks_hypothesis = 8
green_bricks_hypothesis = 3
blue_bricks_hypothesis = 1

# the hypothesis refers to the ratio of red, green, and blue bricks used in the tower
if red_bricks_hypothesis <= red_bricks_premise:
    # check if the hypothesis value contradicts the number of red bricks in the premise
    label = "contradiction"
elif green_bricks_hypothesis!= green_bricks_premise:
    # check if the number of green bricks in the hypothesis contradicts the number of green bricks reported in the premise
    label = "contradiction"
elif blue_bricks_hypothesis!= blue_bricks_premise:
    # check if the number of blue bricks in the hypothesis contradicts the number of blue bricks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
