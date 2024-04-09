fish_initial_premise = 212.0
fish_moved_premise = 68.0
fish_left_hypothesis = 144.0

# the hypothesis refers to the number of fish left, which can be calculated from the premise
# compute the number of fish left in the premise
fish_left_premise = fish_initial_premise - fish_moved_premise
if fish_left_hypothesis!= fish_left_premise:
    # check if the number of fish left in the hypothesis contradicts the number of fish left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
