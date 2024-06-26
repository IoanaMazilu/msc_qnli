tower_bricks_premise = 3
tower_bricks_hypothesis = 4
red_bricks_premise = tower_bricks_premise * 3 // 4
red_bricks_hypothesis = tower_bricks_hypothesis * 3 // 4
green_bricks_premise = tower_bricks_premise * 3 // 4
green_bricks_hypothesis = tower_bricks_hypothesis * 3 // 4
blue_bricks_premise = tower_bricks_premise * 1 // 4
blue_bricks_hypothesis = tower_bricks_hypothesis * 1 // 4

# check if the hypothesis values contradict the premise values
if red_bricks_hypothesis!= red_bricks_premise or green_bricks_hypothesis!= green_bricks_premise or blue_bricks_hypothesis!= blue_bricks_premise:
    label = "contradiction"
elif red_bricks_hypothesis == red_bricks_premise and green_bricks_hypothesis == green_bricks_premise and blue_bricks_hypothesis == blue_bricks_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
