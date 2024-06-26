red_bricks_ratio_premise = 4/3
red_bricks_ratio_hypothesis = 4/3
green_bricks_ratio_premise = 1
green_bricks_ratio_hypothesis = 1
blue_bricks_ratio_premise = 1
blue_bricks_ratio_hypothesis = 1

# the hypothesis talks about the ratio of red, green, and blue toy bricks used in building the tower
# the premise gives a specific ratio for the red, green, and blue bricks
if red_bricks_ratio_hypothesis >= red_bricks_ratio_premise:
    # check if the hypothesis estimate contradicts the ratio of red bricks reported in the premise
    label = "contradiction"
elif green_bricks_ratio_hypothesis!= green_bricks_ratio_premise or blue_bricks_ratio_hypothesis!= blue_bricks_ratio_premise:
    # check if the ratio of green and blue bricks in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of green and blue bricks
    # any ratio of red, green, and blue bricks less than'red_bricks_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
