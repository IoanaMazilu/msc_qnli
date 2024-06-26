red_bricks_premise = 1
green_bricks_premise = 3
blue_bricks_premise = 1

red_bricks_hypothesis = 4
green_bricks_hypothesis = 3
blue_bricks_hypothesis = 1

# the hypothesis refers to the ratio of red, green, and blue bricks in the tower
if red_bricks_hypothesis / green_bricks_hypothesis / blue_bricks_hypothesis > red_bricks_premise / green_bricks_premise / blue_bricks_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of red, green, and blue bricks
    # any ratio greater than the premise ratio is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
