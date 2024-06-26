fish_premise = 212.0
fish_moved_premise = 68.0
fish_left_hypothesis = 144.0

# the hypothesis refers to the number of fish left in the first tank, which is also mentioned in the premise
# compute the number of fish left in the first tank in the premise
fish_left_premise = fish_premise - fish_moved_premise
if fish_left_hypothesis!= fish_left_premise:
    # check if the number of fish left in the first tank in the hypothesis contradicts the number of fish left in the first tank from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
