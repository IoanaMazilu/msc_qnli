red_bricks_ratio_premise = 8
red_bricks_ratio_hypothesis = 4
green_bricks_ratio_premise = 3
green_bricks_ratio_hypothesis = 3
blue_bricks_ratio_premise = 1
blue_bricks_ratio_hypothesis = 1

# the hypothesis refers to the ratio of red, green, and blue toy bricks used by Yali
if red_bricks_ratio_premise <= red_bricks_ratio_hypothesis:
    # check if the ratio of red bricks in the hypothesis contradicts the ratio of red bricks in the premise
    label = "contradiction"
elif green_bricks_ratio_premise!= green_bricks_ratio_hypothesis or blue_bricks_ratio_premise!= blue_bricks_ratio_hypothesis:
    # check if the ratio of green or blue bricks in the hypothesis contradicts the ratio of green or blue bricks in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
