red_bricks_premise = 4
green_bricks_premise = 3
blue_bricks_premise = 1
red_bricks_hypothesis = 8
green_bricks_hypothesis = 3
blue_bricks_hypothesis = 1

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Yali in the premise
if red_bricks_hypothesis >= red_bricks_premise:
    # check if the ratio of red bricks in the hypothesis contradicts the ratio of red bricks in the premise
    label = "contradiction"
elif green_bricks_hypothesis >= green_bricks_premise or blue_bricks_hypothesis >= blue_bricks_premise:
    # check if the ratio of green or blue bricks in the hypothesis contradicts the ratio of green or blue bricks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
