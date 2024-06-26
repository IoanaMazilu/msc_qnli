red_bricks_premise = 3
green_bricks_premise = 3
blue_bricks_premise = 1
ratio_premise = 3/3/1
ratio_hypothesis = 4/3/1

# the hypothesis refers to the ratio of red, green, and blue toy bricks used in building the tower
# the premise mentions the ratio of red, green, and blue toy bricks used in building the tower
if ratio_hypothesis!= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
