red_bricks_premise = 8
green_bricks_premise = 3
blue_bricks_premise = 1

red_bricks_hypothesis = 4
green_bricks_hypothesis = 3
blue_bricks_hypothesis = 1

# the hypothesis refers to the ratio of red, green, and blue bricks used in the tower
if red_bricks_hypothesis <= red_bricks_premise and green_bricks_hypothesis <= green_bricks_premise and blue_bricks_hypothesis <= blue_bricks_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio of red, green, and blue bricks used in the tower
    # any ratio of bricks greater than the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
