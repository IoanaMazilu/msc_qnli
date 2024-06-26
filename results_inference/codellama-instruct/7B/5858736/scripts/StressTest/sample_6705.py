red_bricks_premise = 4
green_bricks_premise = 3
blue_bricks_premise = 1
red_bricks_hypothesis = 8
green_bricks_hypothesis = 3
blue_bricks_hypothesis = 1

# the hypothesis refers to the ratio of red, green, and blue bricks mentioned in the premise
if red_bricks_hypothesis / green_bricks_hypothesis / blue_bricks_hypothesis > red_bricks_premise / green_bricks_premise / blue_bricks_premise:
    # check if the ratio of the hypothesis contradicts the ratio of the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of red, green, and blue bricks
    # any ratio greater than the premise's estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
