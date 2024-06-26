red_bricks_premise = 4
green_bricks_premise = 3
blue_bricks_premise = 1

red_bricks_hypothesis = 3
green_bricks_hypothesis = 2
blue_bricks_hypothesis = 1

# the hypothesis refers to the ratio of red, green, and blue bricks used in the tower
if red_bricks_hypothesis > red_bricks_premise or green_bricks_hypothesis > green_bricks_premise or blue_bricks_hypothesis > blue_bricks_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the hypothesis values are less than the premise values, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
