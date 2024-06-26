man_wall_premise = 10
man_wall_hypothesis = 10

# the premise and hypothesis refer to the same distance between the man and the wall
if man_wall_premise!= man_wall_hypothesis:
    # check if the premise and hypothesis values contradict each other
    label = "contradiction"
else:
    # the premise and hypothesis values are the same, so we can infer entailment
    label = "entailment"

print(label)
