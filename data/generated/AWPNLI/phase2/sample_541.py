# Premise: Sandy has 26.0 pet fish and her cat ate 6.0.
# Hypothesis: Sandy has 22.0 now.
# Golden Label: contradiction

initial_fish_premise = 26.0
eaten_fish_premise = 6.0
remaining_fish_hypothesis = 22.0

# the hypothesis refers to the number of remaining fish, which can be deduced from the premise
# compute the remaining number of fish in the premise
remaining_fish_premise = initial_fish_premise - eaten_fish_premise
if remaining_fish_hypothesis != remaining_fish_premise:
    # check if the number of remaining fish in the hypothesis contradicts the number of remaining fish from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

