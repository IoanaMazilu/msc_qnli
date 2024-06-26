red_bricks_premise = 1
green_bricks_premise = 3
blue_bricks_premise = 1
red_bricks_hypothesis = 4
green_bricks_hypothesis = 3
blue_bricks_hypothesis = 1

# the hypothesis talks about the ratio of red, green, and blue toy bricks in the tower, which is also mentioned in the premise
if red_bricks_hypothesis <= red_bricks_premise and green_bricks_hypothesis <= green_bricks_premise and blue_bricks_hypothesis <= blue_bricks_premise:
    # check if the ratio of red, green, and blue toy bricks in the hypothesis is less than or equal to the ratio in the premise
    label = "entailment"
elif red_bricks_hypothesis!= red_bricks_premise or green_bricks_hypothesis!= green_bricks_premise or blue_bricks_hypothesis!= blue_bricks_premise:
    # check if the ratio of red, green, and blue toy bricks in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values are the same as the premise values, but with different ratios, we can't infer entailment or contradiction
    label = "neutral"

print(label)
