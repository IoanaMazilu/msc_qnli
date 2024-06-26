jog_walk_time_premise = 3
jog_walk_time_hypothesis = 4

# the hypothesis refers to the same situation as the premise, but changes the total time
if jog_walk_time_hypothesis != jog_walk_time_premise:
    # check if the total time in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the total time in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
