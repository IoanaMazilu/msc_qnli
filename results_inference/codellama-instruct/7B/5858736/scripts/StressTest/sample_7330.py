red_bricks_premise = 0
green_bricks_premise = 0
blue_bricks_premise = 0
red_bricks_hypothesis = 0
green_bricks_hypothesis = 0
blue_bricks_hypothesis = 0

# the hypothesis refers to the number of bricks used in the ratio of 4:3:1
if red_bricks_hypothesis + green_bricks_hypothesis + blue_bricks_hypothesis!= 4 + 3 + 1:
    # check if the hypothesis value contradicts the estimate of more than'red_bricks_premise'
    label = "contradiction"
elif red_bricks_hypothesis / (red_bricks_hypothesis + green_bricks_hypothesis + blue_bricks_hypothesis) < 3/4:
    # check if the ratio of red bricks in the hypothesis contradicts the estimate of more than'red_bricks_premise'
    label = "contradiction"
elif green_bricks_hypothesis / (red_bricks_hypothesis + green_bricks_hypothesis + blue_bricks_hypothesis) < 3/4:
    # check if the ratio of green bricks in the hypothesis contradicts the estimate of more than 'green_bricks_premise'
    label = "contradiction"
elif blue_bricks_hypothesis / (red_bricks_hypothesis + green_bricks_hypothesis + blue_bricks_hypothesis) < 1/4:
    # check if the ratio of blue bricks in the hypothesis contradicts the estimate of more than 'blue_bricks_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
