red_bricks_ratio_premise = 1
green_bricks_ratio_premise = 3
blue_bricks_ratio_premise = 1
red_bricks_ratio_hypothesis = 4
green_bricks_ratio_hypothesis = 3
blue_bricks_ratio_hypothesis = 1

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Gali in the premise
if red_bricks_ratio_hypothesis <= red_bricks_ratio_premise or green_bricks_ratio_hypothesis <= green_bricks_ratio_premise or blue_bricks_ratio_hypothesis <= blue_bricks_ratio_premise:
    # check if the ratio values in the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
