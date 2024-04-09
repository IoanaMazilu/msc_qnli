tower_bricks_premise = 1:3:1
tower_bricks_hypothesis = 4:3:1

# the hypothesis refers to the ratio of toy bricks used in the tower, as described in the premise
if tower_bricks_premise <= tower_bricks_hypothesis:
    # check if the estimate of 'tower_bricks_hypothesis' contradicts the ratio of toy bricks mentioned in the premise
    label = "contradiction"
elif tower_bricks_hypothesis!= tower_bricks_premise:
    # check if the ratio of toy bricks in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
