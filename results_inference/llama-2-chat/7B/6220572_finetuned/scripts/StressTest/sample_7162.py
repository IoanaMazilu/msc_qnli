red_bricks_ratio_premise = 1
green_bricks_ratio_premise = 1
blue_bricks_ratio_premise = 1

red_bricks_ratio_hypothesis = 4
green_bricks_ratio_hypothesis = 3
blue_bricks_ratio_hypothesis = 1

# the hypothesis refers to the ratio of red, green, and blue bricks used in the tower
if red_bricks_ratio_hypothesis <= red_bricks_ratio_premise or green_bricks_ratio_hypothesis <= green_bricks_ratio_premise or blue_bricks_ratio_hypothesis <= blue_bricks_ratio_premise:
    # check if the ratio of red, green, and blue bricks in the hypothesis contradicts the ratio of red, green, and blue bricks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of red, green, and blue bricks
    # any ratio of red, green, and blue bricks greater than'red_bricks_ratio_premise', 'green_bricks_ratio_premise', and 'blue_bricks_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
