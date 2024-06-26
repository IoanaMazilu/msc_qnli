red_bricks_premise = 4
green_bricks_premise = 3
blue_bricks_premise = 1

red_bricks_hypothesis = 4
green_bricks_hypothesis = 3
blue_bricks_hypothesis = 1

if red_bricks_hypothesis >= red_bricks_premise and green_bricks_hypothesis >= green_bricks_premise and blue_bricks_hypothesis >= blue_bricks_premise:
    label = "entailment"
elif red_bricks_hypothesis < red_bricks_premise or green_bricks_hypothesis < green_bricks_premise or blue_bricks_hypothesis < blue_bricks_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
